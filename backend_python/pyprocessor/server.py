from flask import Flask, request, jsonify
import requests
import json
from EasyOCR import EasyOCR
from URL2JSON import URL2JSON

ocr_reader = EasyOCR()
app = Flask(__name__)

from threading import Semaphore

semaphore = Semaphore(1)

@app.route('/', methods=['POST'])
def handle_request():
    with semaphore:
        try:
            data = request.data.decode('utf-8')
            URL = json.loads(data)['URL']
            with open('LOGS.txt', 'a') as f:
                f.write(URL + '\n')
                f.flush()
            url2json = URL2JSON(ocr_reader)
            result_jsonlist = url2json.get_jsonlist(URL)

            for result in result_jsonlist:
                data = url2json.convert_to_ActivityInfo(str(result))
                url = 'http://localhost:8080/api/activity'
                headers = {'Content-Type': 'application/json'}
                with open('LOGS.txt', 'a') as f:
                    f.write(str(data) + '\n')
                    f.flush()
                r = requests.put(url, data=json.dumps(data), headers=headers)

            info = "success"
        except Exception as e:
            print(e)
            if str(e) == "GPTProcessor Error":
                info = "error"
            elif str(e) == "Repeated Content":
                info = "repeated"
            elif str(e) == "invalid URL":
                info = "invalid"
            elif str(e) == "Connection Error":
                info = "connection URL error"
            elif str(e) == "TOO EARLY":
                info = "too early"
            elif str(e) == "Not an Activity":
                info = "not an activity"
            else:
                info = str(e)
        with open('LOGS.txt', 'a') as f:
            f.write("info: " + info + '\n')
            f.flush()
        return jsonify({'info': info})

        
@app.route('/nocheck', methods=['POST'])
def handle_request_nocheck():
    with semaphore:
        try:
            data = request.data.decode('utf-8')
            URL = json.loads(data)['URL']
            with open('LOGS.txt', 'a') as f:
                f.write(URL + '\n')
                f.flush()
            url2json = URL2JSON(ocr_reader)
            result_jsonlist = url2json.get_jsonlist(URL, check_repeated=False)

            for result in result_jsonlist:
                data = url2json.convert_to_ActivityInfo(str(result))
                url = 'http://localhost:8080/api/activity'
                headers = {'Content-Type': 'application/json'}
                with open('LOGS.txt', 'a') as f:
                    f.write(str(data) + '\n')
                    f.flush()
                r = requests.put(url, data=json.dumps(data), headers=headers)

            info = "success"
        except Exception as e:
            print(e)
            if str(e) == "GPTProcessor Error":
                info = "error"
            elif str(e) == "Repeated Content":
                info = "repeated"
            elif str(e) == "invalid URL":
                info = "invalid"
            elif str(e) == "Connection Error":
                info = "connection URL error"
            elif str(e) == "TOO EARLY":
                info = "too early"
            elif str(e) == "Not an Activity":
                info = "not an activity"
            else:
                info = str(e)
        with open('LOGS.txt', 'a') as f:
            f.write("info: " + info + '\n')
            f.flush()
        return jsonify({'info': info})

if __name__ == "__main__":
    app.run(host="localhost", port=9001)

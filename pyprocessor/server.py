from flask import Flask, request, jsonify
import requests
import json
from URL2JSON import URL2JSON

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_request():
    try:
        data = request.data.decode('utf-8')
        URL = json.loads(data)['URL']
        url2json = URL2JSON()
        result_jsonlist = url2json.get_jsonlist(URL , check_repeated = False)

        for result in result_jsonlist:
            data = url2json.convert_to_ActivityInfo(str(result))
            url = 'http://localhost:8080/api/admin/activity'
            headers = {'Content-Type': 'application/json'}
            r = requests.post(url, data=json.dumps(data), headers=headers)

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

    return jsonify({'info': info})

if __name__ == "__main__":
    app.run(host="localhost", port=9001)

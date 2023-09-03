import socket
import requests
import json
from URL2JSON import URL2JSON





if __name__ == "__main__":
    url2json = URL2JSON()
    socket_server = socket.socket()

    socket_server.bind(("localhost", 9001))
    socket_server.listen(10)
    print("服务器启动")

    while True:
        result = socket_server.accept()
        conn = result[0]  # 客户端连接对象
        address = result[1]  # 客户端地址信息

        data = conn.recv(1024)
        URL = str(data).split("'")[1]
        try:
            result_jsonlist = url2json.get_jsonlist(URL)
        except Exception as e:
            assert isinstance(e, Exception)
            assert str(e) == "Repeated Content"
            info = "repeated"
            conn.send(info.encode())
            print("Message sent")
            conn.close()
            continue
        # print(str(data).split("'")[1])
        for result in result_jsonlist:
            data = url2json.convert_to_ActivityInfo(str(result))
            # print(data)
            url = 'http://localhost:8080/api/admin/activity'
            headers = {'Content-Type': 'application/json'}
            print("result_data = ",data)
            r = requests.post(url, data=json.dumps(data), headers=headers)
            print("Post请求发送")

        info = "success"
        conn.send(info.encode())
        print("Message sent")
        conn.close()

    socket_server.close()

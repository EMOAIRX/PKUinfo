import socket
from get_content import ContentGetter
from GPT_processor import GPTProcessor


class URL2JSON:
    def __init__(self):
        self.content_getter = ContentGetter()
        self.processor = GPTProcessor()

    def get_jsonlist(self, url):
        import json
        content = self.content_getter.get_fulltext(url)
        jsondata_list = self.processor.Text_to_JSON(content)
        result_list = []
        for jsondata in jsondata_list:
            jsondata["url"] = url
            jsondata = json.dumps(jsondata)
            result_list.append(jsondata)
        return result_list

    def convert_to_ActivityInfo(self, json_data):
        import json
        import datetime
        # print("JSON数据:")
        # print(json_data)
        json_data = json.loads(json_data)
        activityInfo = {}
        activityInfo["title"] = json_data["event_name"]
        activityInfo["address"] = json_data["location"]
        activityInfo["startDate"] = json_data["data"]
        activityInfo["endDate"] = json_data["data"]
        activityInfo["startTime"] = json_data["time"]
        activityInfo["endTime"] =  json_data["time"]
        activityInfo["description"] = json_data["event_summary"]
        activityInfo["college"] = json_data["organizational_unit"]
        activityInfo["accountLink"] = json_data["url"]
        activityInfo["extraInfo"] = json_data["event_time"]
        return activityInfo


if __name__ == "__main__":
    url2json = URL2JSON()
    # result_jsonlist = url2json.get_jsonlist(str('https://mp.weixin.qq.com/s/LUsA5qG5ysC77sugGcLjOA'))
    # import json
    # pps = {'event_name': '文化中国·水立方杯中文歌曲大赛（北京赛区）决赛', 'data': '2023-07-09', 'time': '19:00:00', 'event_time': "['2023-07-09T19:00:00']", 'location': '北京大学百周年纪念讲堂李莹厅', 'organizational_unit': '共青团北京大学委员会', 'event_summary': '在2023年7月9日晚19:00 , 北京大学百周年纪念讲堂李莹厅将举办文化中国·水立方杯中文歌曲大赛(北京赛区)决赛。这个盛夏七月的活动旨在展示世界青年的积极、乐观、自信的精神风貌 ,并推动文明交流互鉴。领票时间是2023年7月8日15:00, 地点是北京大学学生会办公室（新太阳学生中心北侧）。', 'url': 'https://mp.weixin.qq.com/s/LUsA5qG5ysC77sugGcLjOA'}
    # result_jsonlist = [
    #     json.dumps(pps),
    # ]
    # print(result_jsonlist)
    # for result in result_jsonlist:
    #     act = url2json.convert_to_ActivityInfo(str(result))
    #     print(act)
    #     act = json.dumps(act)
    #     print(act)
    # print('result = ', result)
    socket_server = socket.socket()

    socket_server.bind(("localhost", 9001))
    socket_server.listen(10)
    print("服务器启动")

    while True:
        result = socket_server.accept()
        conn = result[0]  # 客户端连接对象
        address = result[1]  # 客户端地址信息

        data = conn.recv(1024)

        result_jsonlist = url2json.get_jsonlist(str(data).split("'")[1])
        # print(str(data).split("'")[1])
        for result in result_jsonlist:
            data = url2json.convert_to_ActivityInfo(str(result))
            # print(data)
            import requests
            import json
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

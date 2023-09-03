from ContentGetter import ContentGetter
from GPTProcessor import GPTProcessor
from WebContent import WebContent
import requests
import json

# 这个函数改async有点难啊
def check_is_repeated(content : WebContent) -> bool:
    url = 'http://localhost:8080/api/admin/check'
    headers = {'Content-Type': 'application/json'}
    data = {}
    data["title"] = content.title
    data["author"] = content.author
    data["publish_time"] = content.publish_time #到底是publish_time还是update_time，好像一开始改的就是错的？这个是create_time
    print("result_data = ",data)
    r = requests.post(url, json.dumps(data), headers=headers)
    print("查重请求发送")
    response_data = json.loads(r.text) #code来存这个东西真的好吗，code最好是200OK,
    if response_data['code'] == 1: return True
    else: 
        url = 'http://localhost:8080/api/admin/record'
        r = requests.post(url, json.dumps(data), headers=headers) #啊啊
        print("记录请求发送")
        return False
    # 好浪费啊，通过网络来回传递很慢的，这个最好还是在java端解决吧
    # 交互传输的代价就很大啊。。。


class URL2JSON:
    def __init__(self):
        self.content_getter = ContentGetter()
        self.processor = GPTProcessor()

    def get_jsonlist(self, url):
        import json
        #通过url爬取网页内容
        content = self.content_getter.get_fullcontent(url)
        assert isinstance(content, WebContent)
        #进行查重，重复则报错
        if check_is_repeated(content):
            raise Exception("Repeated Content")

        #通过gpt将网页内容转为标准化json
        jsondata_list = self.processor.Text_to_JSON(content.text)
        print("JSON数据:")
        print(jsondata_list)
        result_list = []
        for jsondata in jsondata_list:
            jsondata["url"] = url
            jsondata = json.dumps(jsondata)
            result_list.append(jsondata)
        print("JSON数据:")
        print(result_list)
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


if __name__ == '__main__':
    #https://mp.weixin.qq.com/template/article/1693726858/index.html
    url = 'https://mp.weixin.qq.com/s/CLxcCN0FhcuswCKYR-ITpA'
    url2json = URL2JSON()
    print(url2json.get_jsonlist(url))

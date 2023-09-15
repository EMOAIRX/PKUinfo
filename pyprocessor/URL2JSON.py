from ContentGetter import ContentGetter
from GPTProcessor import GPTProcessor
from WebContent import WebContent
from EasyOCR import EasyOCR
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
        self.ocr_reader = EasyOCR()

    def get_jsonlist(self, url, check_repeated = True):
        import json
        #通过url爬取网页内容
        try:
            content = self.content_getter.get_fullcontent(url)
        except Exception as e:
            raise e
        assert isinstance(content, WebContent)
        #进行查重，重复则报错
        if check_repeated:
            if check_is_repeated(content):
                raise Exception("Repeated Content")
        #if time < 2023.08.01 raise TOO EARLY
        # POSTER TIME BE LIKE "2023-05-25 23:39" as a str
        post_time = content.publish_time
        if (post_time[3] == '2') or (post_time[6] < '8'):
           raise Exception("TOO EARLY") 

        #通过gpt将网页内容转为标准化json
        if not self.processor.first_guess(content.title, content.text):
            print("Not an Activity")
            raise Exception("Not an Activity")

        processed_text = content.title + '\n 文章发布发布时间(并非活动时间):' + content.publish_time + '\n' + content.author + '\n' + content.text
        # for img_link in content.img_url:
        #     txt_tmp = self.ocr_reader.ocr(img_link)
        #     processed_text += '\n' + txt_tmp 
        
        jsondata_list = None
        for i in range(1):
            try:
                jsondata_list = self.processor.Text_to_JSON(processed_text)
                print("JSON_SUCCESS")
                break
            except Exception as e:
                print(e)
                continue
        if jsondata_list is None:
            Log = open("log.txt", "a")
            # Log.write("URL2JSON.py: " + str(e) + "\n")
            Log.write("appending " + url + " Failed\n")
            raise Exception("GPTProcessor Error")

        print("JSON数据:")
        print(jsondata_list)
        result_list = []
        for jsondata in jsondata_list:
            jsondata['title'] = content.title
            jsondata['author'] = content.author
            jsondata['publish_time'] = content.publish_time
            jsondata['url'] = url
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
        activityInfo["title"] = json_data["event_name"][:60] if json_data["event_name"] is not None else None
        activityInfo["address"] = json_data["location"][:100] if json_data["location"] is not None else None
        activityInfo["startDate"] = json_data["data"] if json_data["data"] is not None else None
        activityInfo["endDate"] = json_data["data"] if json_data["data"] is not None else None
        activityInfo["startTime"] = json_data["time"] if json_data["time"] is not None else None
        activityInfo["endTime"] =  json_data["time"] if json_data["time"] is not None else None
        activityInfo["description"] = json_data["event_summary"]
        activityInfo["college"] = json_data["organizational_unit"][:40] if json_data["organizational_unit"] is not None else None
        activityInfo["accountLink"] = json_data["url"][:255] if json_data["url"] is not None else None
        activityInfo["extraInfo"] = json_data["event_time"]
        return activityInfo


if __name__ == '__main__':
    # url = 'https://mp.weixin.qq.com/template/article/1693726858/index.html'
    # url = "2333"
    # url = 'https://mp.weixin.qq.com/s/CLxcCN0FhcuswCKYR-ITpA'
    # url = 'https://mp.weixin.qq.com/s/z1i77-JDpPG3Dbvh8LLRmQ'
    # url = 'http://mp.weixin.qq.com/s?__biz=Mzg2Njc1NjM2OA==&mid=2247494924&idx=1&sn=5c4b1fcf65fab88214c5cabe64e6fbfd&chksm=ce475f73f930d665e8052799120ae478b33d802fede90016c929f89231b3abdd29fb786cad3d#rd'
    # url = 'https://mp.weixin.qq.com/s?__biz=MzI0ODcwNjkwNw==&mid=2247495765&idx=1&sn=51d1353d9d34d2c12c39c45559aca05c&chksm=e99e1261dee99b77e3433683ea5a0dc65db8feede318b3b556adcce9873a5d70edafdaa65272#rd'
    url = 'https://mp.weixin.qq.com/s?__biz=MjM5MTg0MDE4NQ==&mid=2651231260&idx=2&sn=b1e88e137d12b17bf654b9bb307d7a83&chksm=bd5d56ca8a2adfdc9f6e3fbbf7c12009a2e1700b0e99c863bea737f503bed3606955db0298cd#rd'
    url2json = URL2JSON()
    print(url2json.get_jsonlist(url,check_repeated=False))
    # strr = '{   "event_name": "2023 国际华语控烟辩论赛邀请赛半决赛",   "event_time": [     "2023-08-11 23:59"   ],   "location": null,   "organizational_unit": "北大辩协",   "event_summary": "健言青春·2023 国际华语控烟辩论赛邀请赛半决赛邀您共同参与！"   }'
    # print(json.loads(strr))

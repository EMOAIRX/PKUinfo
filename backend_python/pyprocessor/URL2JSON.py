from ContentGetter import ContentGetter
from GPTProcessor import GPTProcessor
from WebContent import WebContent
from EasyOCR import EasyOCR
import requests
import json
import mysql.connector
def check_and_add_string(connection, cursor, table_name, string_to_check):
    # 查询是否已存在该字符串
    query = "SELECT COUNT(*) FROM {} WHERE record_string = %s".format(table_name)
    cursor.execute(query, (string_to_check,))
    result = cursor.fetchone()[0]
    
    if result > 0:
        print("字符串已存在")
        return True
    else:
        # 如果不存在，则添加新字符串
        insert_query = "INSERT INTO {} (record_string) VALUES (%s)".format(table_name)
        cursor.execute(insert_query, (string_to_check,))
        connection.commit()
        print("字符串已添加")
        return False


# 这个函数改async有点难啊
def check_is_repeated(content : WebContent) -> bool:
    url = 'http://localhost:8081/api/admin/check'
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
    return False 
    # 好浪费啊，通过网络来回传递很慢的，这个最好还是在java端解决吧
    # 交互传输的代价就很大啊。。。


class URL2JSON:
    def __init__(self,ocr_reader):
        self.content_getter = ContentGetter()
        self.processor = GPTProcessor()
        self.ocr_reader = ocr_reader
        self.config = {
            'user': 'root',
            'password': 'pkuinfo',
            'host': '127.0.0.1',
            'database': 'info',
            'raise_on_warnings': True
        }
    def check_repeated(self, string_to_check): 
        try:
            connection = mysql.connector.connect(**self.config)
            cursor = connection.cursor()
            table_name = "t_records" 
            res = check_and_add_string(connection, cursor, table_name, string_to_check)
        except mysql.connector.Error as err:
            print("MySQL 错误：", err)
            res = True
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
        return res

    def get_jsonlist(self, url, check_repeated = True):
        import json
        #通过url爬取网页内容
        try:
            content = self.content_getter.get_fullcontent(url)
        except Exception as e:
            raise e
        assert isinstance(content, WebContent)
        #进行查重，重复则报错
        '''
        if check_repeated:
            if check_is_repeated(content):
                raise Exception("Repeated Content")
        '''
        if check_repeated:
            if self.check_repeated(content.title + content.author):
                print("字符串已存在")
                raise Exception("Repeated Content")
        post_time = content.publish_time
        print(post_time)

        #通过gpt将网页内容转为标准化json
        if not self.processor.first_guess(content.title, content.text):
            print("Not an Activity")
            raise Exception("Not an Activity")

        processed_text = content.title + '\n' + content.author + '\n' + content.text
        for img_link in content.img_url:
            txt_tmp = self.ocr_reader.ocr(img_link)
            processed_text += '\n' + txt_tmp 
        
        jsondata_list = None
        try:
            jsondata_list = self.processor.Text_to_JSON(processed_text)
            print("JSON_SUCCESS")
        except Exception as e:
            raise e
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
        '''
        if check_repeated:
            if check_is_repeated(content):
                raise Exception("Repeated Content")
        if check_repeated:
            url = 'http://localhost:8081/api/admin/record'
            headers = {'Content-Type': 'application/json'}
            data = {}
            data["title"] = content.title
            data["author"] = content.author
            data["publish_time"] = content.publish_time #到底是publish_time还是update_time，好像一开始改的就是错的？这个是create_time
            r = requests.post(url, json.dumps(data), headers=headers) #啊啊
            print("记录请求发送")
        '''
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
        activityInfo["startDate"] = json_data["date1"] if json_data["date1"] is not None else None
        activityInfo["endDate"] = json_data["date2"] if json_data["date2"] is not None else None
        activityInfo["startTime"] = json_data["time1"] if json_data["time1"] is not None else None
        activityInfo["endTime"] =  json_data["time2"] if json_data["time2"] is not None else None
        activityInfo["description"] = json_data["event_summary"]
        activityInfo["college"] = json_data["organizational_unit"][:40] if json_data["organizational_unit"] is not None else None
        activityInfo["link"] = json_data["url"][:255] if json_data["url"] is not None else None
        activityInfo["extraInfo"] = json_data["event_time"]
        activityInfo["tags"] = json_data["tags"] if json_data["tags"] is not None else None
        return activityInfo


if __name__ == '__main__':
    # url = 'https://mp.weixin.qq.com/template/article/1693726858/index.html'
    # url = "2333"
    # url = 'https://mp.weixin.qq.com/s/CLxcCN0FhcuswCKYR-ITpA'
    # url = 'https://mp.weixin.qq.com/s/z1i77-JDpPG3Dbvh8LLRmQ'
    # url = 'http://mp.weixin.qq.com/s?__biz=Mzg2Njc1NjM2OA==&mid=2247494924&idx=1&sn=5c4b1fcf65fab88214c5cabe64e6fbfd&chksm=ce475f73f930d665e8052799120ae478b33d802fede90016c929f89231b3abdd29fb786cad3d#rd'
    # url = 'https://mp.weixin.qq.com/s?__biz=MzI0ODcwNjkwNw==&mid=2247495765&idx=1&sn=51d1353d9d34d2c12c39c45559aca05c&chksm=e99e1261dee99b77e3433683ea5a0dc65db8feede318b3b556adcce9873a5d70edafdaa65272#rd'
    # url = 'https://mp.weixin.qq.com/s?__biz=MjM5MTg0MDE4NQ==&mid=2651231260&idx=2&sn=b1e88e137d12b17bf654b9bb307d7a83&chksm=bd5d56ca8a2adfdc9f6e3fbbf7c12009a2e1700b0e99c863bea737f503bed3606955db0298cd#rd'
    # url = 'https://mp.weixin.qq.com/s/dVwVezWK5eNTqUW_3sevng'
    # url = 'https://mp.weixin.qq.com/s/nmjXh8MM-qi76UiWujD0zw'
    value = {"event_name": "\\u4e00\\u4eba\\u4e4b\\u4e0b | \\u5317\\u5927\\u4e13\\u573a\\u5206\\u4eab\\u4f1a", "date1": "2024-03-02", "time1": "15:30:00", "date2": "2024-03-02", "time2": "17:00:00", "event_time": "2024\\u5e743\\u67082\\u65e515:30-17:00", "location": "\\u5317\\u4eac\\u5927\\u5b66\\u65b0\\u592a\\u9633\\u5b66\\u751f\\u4e2d\\u5fc3B101\\u62a5\\u544a\\u5385", "organizational_unit": "\\u5143\\u706b\\u52a8\\u6f2b\\u793e", "event_summary": "\\u3010\\u6d3b\\u52a8\\u3011\\u4e00\\u4eba\\u4e4b\\u4e0b | \\u5317\\u5927\\u4e13\\u573a\\u5206\\u4eab\\u4f1a\\u5c06\\u4e8e3\\u67082\\u65e5\\u5728\\u5317\\u4eac\\u5927\\u5b66\\u65b0\\u592a\\u9633\\u5b66\\u751f\\u4e2d\\u5fc3B101\\u62a5\\u544a\\u5385\\u4e3e\\u884c\\uff0c\\u7531\\u5143\\u706b\\u52a8\\u6f2b\\u793e\\u4e3b\\u529e\\u3002\\u6d3b\\u52a8\\u9080\\u8bf7\\u4e86\\u5c0f\\u8fde\\u6740\\u3001\\u590f\\u4faf\\u843d\\u67ab\\u3001\\u51af\\u5b9d\\u5b9d\\u7b49\\u914d\\u97f3\\u6f14\\u5458\\u3002\\u6709\\u610f\\u53c2\\u52a0\\u7684\\u670b\\u53cb\\u9700\\u5173\\u6ce8@\\u4e00\\u4eba\\u4e4b\\u4e0b\\u52a8\\u753b \\u5b98\\u65b9\\u5fae\\u535a\\uff0c\\u5e26\\u8bdd\\u9898#\\u4e00\\u4eba\\u4e4b\\u4e0b#\\u8f6c\\u53d1\\u6d3b\\u52a8\\u5fae\\u535a\\u5e76\\u8bc4\\u8bba[\\u6211\\u8981\\u62a5\\u540d]\\uff0c\\u62a5\\u540d\\u6210\\u529f\\u8005\\u5c06\\u4e8e2\\u670828\\u65e5\\u524d\\u6536\\u5230\\u5b98\\u535a\\u79c1\\u4fe1\\u901a\\u77e5\\u3002\\u6d3b\\u52a8\\u5f53\\u5929\\u9700\\u73b0\\u573a\\u5b9e\\u540d\\u5236\\u7b7e\\u5230\\u53d6\\u7968\\uff0c\\u5e76\\u643a\\u5e26\\u8eab\\u4efd\\u8bc1\\u7b49\\u6709\\u6548\\u8bc1\\u4ef6\\u3002", "tags": ["\\u6587\\u827a", "\\u62db\\u65b0", "\\u5fd7\\u613f"], "title": "\\u3010\\u6d3b\\u52a8\\u3011\\u4e00\\u4eba\\u4e4b\\u4e0b | \\u5317\\u5927\\u4e13\\u573a\\u5206\\u4eab\\u4f1a", "author": "\\u5143\\u706b\\u52a8\\u6f2b\\u793e", "publish_time": "2024-02-23 15:19", "url": "http://mp.weixin.qq.com/s?__biz=MjM5NjY2ODY0OQ==&mid=2650134362&idx=1&sn=a122c459031cb33d03c511e0266dde0f&chksm=bee4c2dc89934bca72b7eed7529b73888060560cf4f4061d04548d19da4514b5013f6ad765cf#rd "}
    url2json = URL2JSON(EasyOCR())
    print(url2json.convert_to_ActivityInfo(json.dumps(value)))
    # print(url2json.get_jsonlist(url, check_repeated = True))
    # strr = '{   "event_name": "2023 国际华语控烟辩论赛邀请赛半决赛",   "event_time": [     "2023-08-11 23:59"   ],   "location": null,   "organizational_unit": "北大辩协",   "event_summary": "健言青春·2023 国际华语控烟辩论赛邀请赛半决赛邀您共同参与！"   }'
    # print(json.loads(strr))

import os
import openai
import json
from keys import openai_APIKEY, openai_BASE

class GPTProcessor:
    def __init__(self):
        openai.api_key = openai_APIKEY
        openai.api_base = openai_BASE
        self.id = 0

    def ask_chatgpt(self, my_messages): #可以做异步，和GPT连接请求发出后，在全部完成前可以切换到其它线程
        ans = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages=my_messages,
            ).choices[0].message.content
        return ans

    def txt2json(self, text):
        result = self.ask_chatgpt(text)
        return result

    def Text_to_JSON(self, text):
        my_messages = [
            {"role": "system", "content": "Now that you are engaged in professional text processing, please let me know if the push below is a preview of an event (such as a lecture or ticket collection) (而不是活动总结或者其它内容). If so, please use JSON format to tell me the 'event_name', 'event_time', 'location', 'organizational_unit', and 'event_summary'. 时间尽可能规范到特定的时刻，如果有多个时间请一并输出，如没有则以None存在，推送发布时间为2023年，如果有多个活动，请返回list，如果没有则返回空list。Otherwise, tell me the activity category it belongs to."},
            {"role": "user", "content": text},
        ]
        infolist = self.ask_chatgpt(my_messages)
        infolist = infolist.replace('\n', ' ')
        try:
            json_list = json.loads(infolist)
        except:
            print('Error: json.loads error')
            return []
        if type(json_list) != list: 
            json_list = [json_list]
        should_exist = ['event_name', 'event_time', 'location', 'organizational_unit', 'event_summary']
        result_list = []
        for info in json_list:
            all_exist = True
            for key in should_exist:
                if key not in info:
                    print('Error: ', key, ' not exist')
                    all_exist = False
                    break
            if not all_exist:
                continue
            ask_time_message = [
                {"role": "system", "content": "请你告诉我这个活动最早的时间，请以 XXXX-XX-XX XX:XX 的格式告诉我。请注意最早的时间只会存在一个，请直接告诉我这个格式不要解释任何理由和补充，如果没有特定的时间，截止时间请告诉我为24:00，开始时间请告诉我00:00，如果未能提供请告诉我None"},
                {"role": "user", "content": str(info)},
            ]
            start_time = self.ask_chatgpt(ask_time_message)
            if len(start_time) != 16 or start_time[4] != '-' or start_time[7] != '-' or start_time[10] != ' ' or start_time[13] != ':' or not start_time[:4].isdigit() or not start_time[5:7].isdigit() or not start_time[8:10].isdigit() or not start_time[11:13].isdigit() or not start_time[14:16].isdigit():
                print('Error: start_time format error')
                continue
            json_data = {
                'event_name': info.get('event_name', None),
                'data': start_time[:10],
                'time': start_time[11:16] + ':00',
                'event_time': str(info.get('event_time', None)),
                'location': info.get('location', None),
                'organizational_unit': info.get('organizational_unit', None),
                'event_summary': info.get('event_summary', None),
            }
            result_list.append(json_data)
        return result_list

    def process_dir(self, current_dir):
        for filename in os.listdir(current_dir):
            try:
                file_path = os.path.join(current_dir, filename)
                
                if os.path.isdir(file_path):
                    self.process_dir(file_path)
                    
                elif filename.endswith('.txt'):
                    with open(file_path,encoding='utf-8') as f:
                        text = f.read()
                    json_data = self.Text_to_JSON(text)
                    
            except:
                print('Error processing file: ', filename)
                continue
        print('Done!')

if __name__ == '__main__':
    test_text = '''
 微信号 beidatuanwei 
 功能介绍 共青团北京大学委员会官方公众号

文化中国


水立方杯



嘹亮歌声传四海，文化激荡遍九州。
同心共圆中国梦，交流互鉴谱新篇。
在这个盛夏七月，2023年“文化中国·水立方杯”中文歌曲大赛（北京赛区）决赛将于7月9日晚在北京大学百周年纪念讲堂李莹厅举办。

左滑查看往届大赛活动图片



壹
大赛简介



以歌传情，以赛为媒，以侨为桥，2023年“文化中国·水立方杯”中文歌曲大赛（北京赛区）在这个夏天如约而至。自本届大赛正式启动以来，各参赛高校留学 
生热情响应、积极参与。经过选拔赛和晋级赛的激烈角逐，共有10名选手赢得了北京赛区决赛的入场券，用最美歌声彰显时代强音！

歌声连接各国青年，音乐搭建友谊桥梁。“文化中国·水立方杯”中文歌曲大赛（北京赛区）致力于展现世界青年积极、乐观、自信的精神风貌，致力于推动文 
明交流互鉴。

2023年“文化中国·水立方杯”中文歌曲大赛宣传片



贰
决赛场次信息



决赛时间：2023年7月9日（星期日）晚19:00—21:30
决赛地点：北京大学百周年纪念讲堂李莹厅

叁
领票时间及地点



领票时间：2023年7月8日（星期六）15：00（数量有限，先到先得）
领票地点：北京大学学生会办公室（新太阳学生中心北侧）

领票要求



各位同学领票时，需本人在场出示校园卡或学生证以便核验身份，每名同学限领一张门票，感谢配合。




万里山河，长风浩荡。
交流互鉴，共创未来。
让我们相聚在燕园，
唱响“再欢聚，更美好”的真诚祝愿，
7月9日晚19:00，我们不见不散！


编辑 | 宋海博
新媒体编辑 | 张祺祺
责任编辑 | 张祺祺
审核 | 连烨 芮泽华
图片来源 | “文化中国·水立方杯”公众号

微信扫一扫关注该公众号
'''
    processor = GPTProcessor()
    print ( processor.Text_to_JSON(test_text) )
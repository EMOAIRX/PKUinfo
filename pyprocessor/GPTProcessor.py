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
        import zhipuai
        zhipuai.api_key = "578b7a96a78e6cb751ee12afaa24d416.2O6f4vV4ENy74MCk"
        print({"role": "user", "content": my_messages[0]['content'] + '\n' + my_messages[1]['content']})
        response = zhipuai.model_api.sse_invoke(
            model="chatglm_pro",
            prompt=[
                {"role": "user", "content": my_messages[0]['content']},
                {"role": "assistant", "content": "好的"},
                {"role": "user", "content": my_messages[1]['content']},
            ],
            temperature=0.95,
            top_p=0.1,
            incremental=True
        )
        print(response)
        result = ''
        for event in response.events():
            if event.event == "add":
                result += event.data
        #delete ' ' from the first
        while (len(result) > 0 and result[0] == ' '):
            result = result[1:]
        print('ANS=',result)
        return result

    def txt2json(self, text):
        result = self.ask_chatgpt(text)
        return result

    def first_guess(self,title,text):
        my_messages = [
            {"role": "system", "content": "根据下面这个标题和部分文字，你觉得是否可能是某种活动 的 预告 售票 报名，请直接告诉我答案为'是'或'否'。请不要回复任何其它内容。请回复一个字，不要回复多个字。如果你觉得不确定，也请回复'是'。"},
            {"role": "user", "content": title + '\n' + text[:20]},
        ]
        ans = self.ask_chatgpt(my_messages)
        if ans == '否':
            return False
        return True


    def Text_to_JSON(self, text):
        try:
            my_messages = [
                {"role": "system", "content": "Now that you are engaged in professional text processing, please let me know if the push below is a preview of an event (such as a lecture or ticket collection) (而不是活动总结或者其它内容). If so, please use JSON format to tell me the 'event_name', 'event_time', 'location', 'organizational_unit', and 'event_summary'. 时间尽可能规范到特定的时刻，如果有多个时间请一并输出，如没有则以null存在，推送发布时间为2023年，如果有多个活动，请返回list，如果没有则返回空list。Otherwise, tell me the activity category it belongs to."},
                {"role": "user", "content": text},
            ]
            infolist = self.ask_chatgpt(my_messages)
            infolist = infolist.replace('\n', ' ') 
        except:
            my_messages = [
                {"role": "system", "content": "请获取下文（这是一篇推送的前半部分）的摘要，不要忽略所有的，时间，地点，主办方，主题，摘要，尤其是时间"},
                {"role": "user", "content": text[:1200]},
            ]
            summary = self.ask_chatgpt(my_messages)
            my_messages = [
                {"role": "system", "content": "Now that you are engaged in professional text processing, please let me know if the push below is a preview of an event (such as a lecture or ticket collection) (而不是活动总结或者其它内容). If so, please use JSON format to tell me the 'event_name', 'event_time', 'location', 'organizational_unit', and 'event_summary'. 时间尽可能规范到特定的时刻，如果有多个时间请一并输出，如没有则以null存在，推送发布时间为2023年，如果有多个活动，请只返回一个。Otherwise, tell me the activity category it belongs to."},
                {"role": "user", "content": summary + '\n' + text[:1000]},
            ]
            infolist = self.ask_chatgpt(my_messages)
            infolist = infolist.replace('\n', ' ') 

        try:
            print(infolist)
            #contrive json from string, from first '{ to the first '}' after the first '{'
            json_list = infolist[infolist.find('{'):infolist.find('}')+1]
            print(json_list)
            json_list = json.loads(json_list)
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
                {"role": "system", "content": "请你告诉我这个活动最早的时间，请以 XXXX-XX-XX XX:XX:XX 的格式告诉我。请注意最早的时间只会存在一个，请直接告诉我这个格式不要解释任何理由和补充，如果没有特定的时间，截止时间请告诉我为24:00:00，开始时间请告诉我00:00:00，如果未能提供请告诉我null"},
                {"role": "user", "content": str(info)},
            ]
            start_time = self.ask_chatgpt(ask_time_message)
            print(start_time)
            if start_time[4] != '-' or start_time[7] != '-' or start_time[10] != ' ' or start_time[13] != ':' or not start_time[:4].isdigit() or not start_time[5:7].isdigit() or not start_time[8:10].isdigit() or not start_time[11:13].isdigit() or not start_time[14:16].isdigit():
                print('Error: start_time format error')
                continue
            if len(start_time) == 16:
                start_time += ':00'
            json_data = {
                'event_name': info.get('event_name', None),
                'data': start_time[:10],
                'time': start_time[11:19],
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
'''
    processor = GPTProcessor()
    print ( processor.Text_to_JSON(test_text) )
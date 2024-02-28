import os
import openai
import json
from keys import openai_APIKEY, openai_BASE, zhipuai_APIKEY
import zhipuai
from datetime import datetime
import re
class GPTProcessor:
    def __init__(self):
        openai.api_key = openai_APIKEY
        openai.api_base = openai_BASE
        zhipuai.api_key = zhipuai_APIKEY
        self.id = 0

    def ask_chatgpt(self, my_messages): #可以做异步，和GPT连接请求发出后，在全部完成前可以切换到其它线程
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
        result = ''
        for event in response.events():
            if event.event == "add":
                result += event.data
        #delete ' ' from the first
        while (len(result) > 0 and result[0] == ' '):
            result = result[1:]
        print('ANS=',result)
        return result

    # def ask_chatgpt(self, my_messages): #可以做异步，和GPT连接请求发出后，在全部完成前可以切换到其它线程
    #     ans = openai.ChatCompletion.create(
    #             model="gpt-3.5-turbo", 
    #             messages=my_messages,
    #         ).choices[0].message.content
    #     print('ANS=',ans)
    #     return ans


    def txt2json(self, text):
        result = self.ask_chatgpt(text)
        return result

    def first_guess(self,title,text):
        my_messages = [
            {"role": "system", "content": "根据下面这个标题和部分文字，你觉得是否可能是某种活动 的 预告 售票 报名，请直接告诉我答案为'是'或'否'。请不要回复任何其它内容。请回复一个字，不要回复多个字。如果是活动的总结请返回'否'，如果你觉得不确定，也请回复'是'。请严格地以唯一的格式回复我"},
            {"role": "user", "content": title + '\n' + text[:20]},
        ]
        ans = self.ask_chatgpt(my_messages)
        if ans == '否':
            return False
        return True


    def Text_to_JSON(self, text):
        try:
            my_messages = [
                {"role": "system", "content": "Now that you are engaged in professional text processing, please let me know if the push below is a preview of an event (such as a lecture or ticket collection) （不包括活动总结). If so, please use JSON format to tell me the 'event_name', 'event_time', 'location', 'organizational_unit'. 时间尽可能规范到特定的时刻，如果有多个时间请一并输出，如没有则以null存在，推送发布时间为2023年，如果有多个活动，请返回list，如果没有则返回空list。Otherwise, tell me the activity category it belongs to. please use JSON format!去除内容中的所有引号的存在"},
                {"role": "user", "content": text + "please use JSON format!! 如果出现了内容中的引号,请不要存在,以防止json格式无法读取"},
            ]
            infolist = self.ask_chatgpt(my_messages)
            infolist = infolist.replace('\n', ' ') 
        except:
            my_messages = [
                {"role": "system", "content": "请获取下文（这是一篇推送的前半部分）的摘要，不要忽略所有的，时间，地点，主办方，主题，摘要，尤其是时间"},
                {"role": "user", "content": text[-1500:]},
            ]
            summary1 = self.ask_chatgpt(my_messages)
            my_messages = [
                {"role": "system", "content": "Now that you are engaged in professional text processing, please let me know if the push below is a preview of an event (such as a lecture or ticket collection) (不包括活动总结). If so, please use JSON format to tell me the 'event_name', 'event_time', 'location', 'organizational_unit'. 时间尽可能规范到特定的时刻，如果有多个时间请一并输出，如没有则以null存在，推送发布时间为2023年。Otherwise, tell me the activity category it belongs to."},
                {"role": "user", "content": summary + '\n' + text[:-1500]},
            ]
            infolist = self.ask_chatgpt(my_messages)
            infolist = infolist.replace('\n', ' ') 

        try:
            # print(infolist)
            #contrive json from string, from first '{ to the first '}' after the first '{'
            json_list = infolist[infolist.find('{'):infolist.find('}')+1]
            json_list = json.loads(json_list)
            my_messages = [
                {"role": "system", "content": "请获取下面活动信息的摘要，请包含主要内容但不要太长，请以描述的方式返回，请直接返回摘要，不要回答任何其它内容"},
                {"role": "user", "content": text},
            ]
            zhaiyao = self.ask_chatgpt(my_messages)
            # zhaiyao = zhaiyao.replace('\n', ' ')
            # zhaiyao = zhaiyao.replace(' ', '')
            # zhaiyao = zhaiyao[zhaiyao.find('{'):zhaiyao.find('}')+1]
            #add event_summary : zhaiyao to json_list
            json_list['event_summary'] = zhaiyao

        except Exception as e:
            print('Error: json.loads error')
            print(e)
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
                {"role": "system", "content": "提取下面的时间中最早的时刻，并严格转化为以 ????-??-?? ??:??:?? 的格式回复我。如果没有时间，请回复'没有'，以上格式代表年月日时分秒，如2023-09-11 15:00:00。严格转化格式，不要是其它的格式，必须以`-`和`:`分割，且每个部分都是数字。请一定保留 秒，即使没有显示的表现，默认以 00 填充"},
                {"role": "user", "content": str(info.get('event_time', None))},
            ]
            start_time_str = self.ask_chatgpt(ask_time_message)
            pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'
            match = re.search(pattern, start_time_str)
            if match is None:
                pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2})'
                match = re.search(pattern, start_time_str)
            try:
                extracted_datetime = match.group(1)
                start_time = str(extracted_datetime)
                if len(start_time) == 16:
                    start_time += ':00'
            except Exception as e:
                print('Error: datetime.strptime error')
                print(e)
                continue

            ask_time_message = [
                {"role": "system", "content": "提取下面的时间中最晚的时刻，并严格转化为以 ????-??-?? ??:??:?? 的格式回复我。如果没有时间，请回复'没有'，以上格式代表年月日时分秒，如2023-09-11 15:00:00。严格转化格式，不要是其它的格式，必须以`-`和`:`分割，且每个部分都是数字。请一定保留 秒，即使没有显示的表现，默认以 00 填充"},
                {"role": "user", "content": str(info.get('event_time', None))},
            ]
            end_time_str = self.ask_chatgpt(ask_time_message)
            pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'
            match = re.search(pattern, end_time_str)
            if match is None:
                pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2})'
                match = re.search(pattern, end_time_str)
            try:
                extracted_datetime = match.group(1)
                end_time = str(extracted_datetime)
                if len(end_time) == 16:
                    end_time += ':00'
            except:
                print('Error: datetime1.strptime error')
                continue
            
            json_data = {
                'event_name': info.get('event_name', None),
                'date1': start_time[:10],
                'time1': start_time[11:],
                'date2': end_time[:10],
                'time2': end_time[11:],
                'event_time': str(info.get('event_time', None)),
                'location': info.get('location', None),
                'organizational_unit': info.get('organizational_unit', None),
                'event_summary': info.get('event_summary', None),
            }
            print(json_data)
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
    你是煞笔
'''
    processor = GPTProcessor()
    print ( processor.Text_to_JSON(test_text) )
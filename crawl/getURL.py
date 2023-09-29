# -*- coding: utf-8 -*-
import requests
import time
from tokens import NOWTOKEN,headers
def page(name,fad,num=1):                             #要请求的文章页数
    url = 'https://mp.weixin.qq.com/cgi-bin/appmsg'
    title = []
    link = []
    res = []
    for i in range(num):         
        data = {
            'action': 'list_ex',
            'begin': i*5,       #页数
            'count': '5',
            'fakeid': fad,
            'type': '9',
            'query':'' ,
            'token': NOWTOKEN,
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
        }
        r = requests.get(url,headers = headers,params=data)
        print(r)
        # get json
        dic = r.json() 
        print('dic:',dic)
        try:
            for i in dic['app_msg_list']:     #遍历dic['app_msg_list']中所有内容
                res. append((i['title'],i['link']))
        except:
            print('error')
    return (name,res)

if __name__ == '__main__':

    def POSTER(link):
        import json
        headers = {'Content-Type': 'application/json'}
        url = 'http://localhost:8080/api/user/submit/link'
        data = {'link': link}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        print(r)
        print(r.text)


    while True:

        import random
        #open nameList.txt and get the name and fakeid, UTF-8
        with open('nameList.txt','r',encoding='UTF-8') as f:
            str_list = f.read()
        # print(type(total_str))
        # print(total_str)
        name_list = []
        fakeid_list = []
        lis = str_list.split('\n')
        lis = [i for i in lis if i != '']
        for i in lis:
            name,fad = i.split(' ')
            name_list.append(name)
            fakeid_list.append(fad)
        print(name_list,fakeid_list)

        for name,fad in zip(name_list,fakeid_list):
            print(name,fad)

            SLEEPTIME = random.randint(600,1000)
            print('sleep',SLEEPTIME)
            outdata = page(name,fad,1)
            #output all the urls
            for i in outdata[1]:
                print(i[0],i[1])
                link = i[1]
                try:
                    POSTER(link)
                    SLEEPTIME = random.randint(50,80)
                except:
                    print('error POST link = ',link)
                
                print('sleep',SLEEPTIME)
                time.sleep(SLEEPTIME)
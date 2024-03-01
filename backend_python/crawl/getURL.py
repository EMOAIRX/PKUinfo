# -*- coding: utf-8 -*-
import requests
import time
from tokens import NOWTOKEN,headers
def page(name,fad,num=1):                             #要请求的文章页数
    #https://mp.weixin.qq.com/cgi-bin/appmsgpublish?sub=list&search_field=null&begin=0&count=5&query=&fakeid=MzU5ODg0MTAwMw%3D%3D&type=101_1&free_publish_type=1&sub_action=list_ex&token=1551583939&lang=zh_CN&f=json&ajax=1
    url = 'https://mp.weixin.qq.com/cgi-bin/appmsgpublish?sub=list&search_field=null&begin=0&count=5&query=&fakeid='+fad+'%3D%3D&type=101_1&free_publish_type=1&sub_action=list_ex&token='+str(NOWTOKEN)+'&lang=zh_CN&f=json&ajax=1'
    title = []
    link = []
    res = []
    for i in range(num):
        r = requests.get(url,headers = headers)
        # get json
        dic = r.json() 
        import json
        try:
            A = eval(dic['publish_page'])['publish_list']
            for item in A:
                publish_info = json.loads(item['publish_info'])
                appmsg_info = publish_info['appmsgex'][0]
                T = appmsg_info['title']
                L = appmsg_info['link']
                L = L.replace('\\', '')  # Remove all backslashes from L string
                res.append((T,L))
        except Exception as e:
            print('error')
            print(e)
    print(name,res)
    return (name,res)

if __name__ == '__main__':

    def POSTER(link):
        import json
        headers = {'Content-Type': 'application/json'}
        url = 'http://localhost:9002/'
        data = {'URL': link}
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

            outdata = page(name,fad,1)
            print(outdata)
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

            SLEEPTIME = random.randint(600,1000)
            print('sleep',SLEEPTIME)
            time.sleep(SLEEPTIME)

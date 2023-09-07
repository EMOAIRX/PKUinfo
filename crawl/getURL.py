# -*- coding: utf-8 -*-
import requests
import time

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
        for i in dic['app_msg_list']:     #遍历dic['app_msg_list']中所有内容
            res. append((i['title'],i['link']))
    return (name,res)

if __name__ == '__main__':
    str = '''
北京大学智能学院 Mzk0NDE3ODg5Nw==
北大国发院 MjM5MDIwNDg0MA==
北京大学公共卫生学院生物统计系 MzU5MDg1ODYyMA==
北京大学光华管理学院 MjM5MDk3NDgwMQ==
北京大学对外汉语教育学院 MzA3ODU2MTk4NA==
北京大学物理学院人才培养 MzUxODk4MDA4NA==
北京大学教育学院 MzA4OTA5MjA4MA==
SMS_Stu_Union MzA5NDAxMDYzMQ==
北大数院人 MzU3NzA0OTA5Mg==
PKU言之有物 MzAwMDEwMzI0MQ==
北大物理人 MzA5NzUwODgxMw==
北京大学学生会 MzA3MDAxMTIxMQ==
PKU医预之家 MzAxOTAyMjk0MA==
大信科 MzA4MTAzMzQ5NA==
北京大学历史学系学生会 MzA3NDYwMzkxMg==
北大数院青年志愿者协会 MjM5MDAwNzExMA==
数院研究生会 MzAwNTA1MjA1OA==
物院学生会 MzIwNDEzMDI5OA==
北大心理人 MjM5NjQ4ODc1MA==
PKU信科职业发展中心 MzI3NTQ2MjM5NA==
光华CDC MzA4MDM0NDcwMg==
走进光华 MzkwMDIzNTgxMg==
北大史学人 MzkyODMwMzEwMw==
北京大学教育学院团研 Mzg3MzE5MzQzNA==
北大脑科学 MzAwNTEzNzcwNg==
北京大学人文社会科学研究院 MzIzNDQ0MDUwNg==
北京国际数学研究中心BICMR MzI1ODQ2MTkwOQ==
北京大学语言学实验室 Mzg3OTg2NTkxMw==
北京大学文学讲习所 Mzg3ODU1OTE2MQ==
北京大学前沿计算研究中心 MzU0MjU5NjQ3NA==
大数据分析与应用国家工程实验室 MzkyMDE5NTM0NA==
北京大学统计科学中心 Mzg3MTcyNzA1OQ==
北京大学文化产业研究院 Mzg4NTE0MDUwNg==
北大古典语文学 MzAwNzc0NzMwMw==
思想与社会 Mzg4ODEzNTExNw==
北京大学严复班 MzUyOTkwNTQwNQ==
北京大学 MzA3OTE0MjQzMw==
北大团委 MzIxNjMzMDE1NQ==
北大体育 MzA5MjI1NjIyOA==
北京大学学生发展支持 MzU5OTk0MTE3Mg==
北大新青年 MzU3ODg5ODQ3MA==
PKU体委 MzAwNDg0MDA4Mw==
北京大学教务部 MzIzNzc4ODkxOA==
北大餐饮中心官方资讯 Mzg4MTIzNzU4OQ==
燕园学子微助手 MzA3NzE0MjcyMQ==
平安燕园 MzI2OTQ2NDg5Ng==
燕园微后勤 MzUxMzEyNTczNw==
北京大学招生办 MzA4NjEzNDYxMQ==
北京大学百周年纪念讲堂 MzU2ODY1ODE1MQ==
北大就业 MzA4NjAzMTIxNw==
北大未名BBS MzA3OTMwMjc5Mg==
北大政治法律与社会项目 Mzg3NjcxNTMzNA==
Paideia_et_Cultura MzkwMzI0MjEyNw==
北京大学国发院经济双学位 MzA3MzQ5ODIyNA==
湘思PKU MzU4NjMyNzM3Nw==
北大辩协 MjM5MTg0MDE4NQ==
北大红会 MzA3NzAwNjI5NA==
爱心驿站 MzA5ODA4ODExMg==
PKU思潜十周年 Mzg4OTY4NDgxMA==
未名超算队 MzUzOTk3NzkxMg==
燕语配音社 MzAxMzMwNTAxNQ==
PKUSAA Mzg4NjExNDUzMg==
北大猫协 MjM5NDc5MzgzNg==
风雷街舞社FLCrew MzI0NjA0MTUwNA==
北大粤协 MzA5MTk4NTgxNg==
北大耕读社 MzAwNjA3NDQxMQ==
元火动漫社 MjM5NjY2ODY0OQ==
pku心协 MzA4ODg5NzU4NA==
PKU_CACA MzA3OTQwMTAwOQ==
PKU烹协 MzI4MjU0Njc1Ng==
PKU创新学社 MzA3MjMzNTQ1OQ==
北大汉推办 MzI2ODA5NTg4Nw==
北京通用人工智能研究院 Mzg2Njc1NjM2OA==
北京大学学生服务总队 MzU5NjYzNjg0Mw==
北京大学社会学系 MzU5MjczNjU0NQ==
北京大学计算机学院 MzU2MTEwNjk4Mg==
北京大学历史学系 MzI0ODE4MjM5Mw==
北京大学经济学院 MzIzMzM2NDA5Nw==
北京大学数学科学学院 MzUzMzg4MzgxMQ==
pku数学系 MzkxNTM1MjU5Mw==
P大CoE教务 MzI4OTYxMzkyOA==
北京大学中文系 MzI0ODcwNjkwNw==
北大社会学 MzkxMzMxMzQ2NQ==

'''
    import random
    name_list = []
    fakeid_list = []
    lis = str.split('\n')
    lis = [i for i in lis if i != '']
    for i in lis:
        name,fad = i.split(' ')
        name_list.append(name)
        fakeid_list.append(fad)
    print(name_list,fakeid_list)
    # lis = str . split ( '\n' )
    # lis = [i for i in lis if i != '']

    def POSTER(link):
        import json
        headers = {'Content-Type': 'application/json'}
        url = 'http://localhost:8080/api/user/submit/link'
        data = {'link': link}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        print(r)
        print(r.text)


    while True:
        for name,fad in zip(name_list,fakeid_list):
            print(name,fad)

            SLEEPTIME = random.randint(80,600)
            print('sleep',SLEEPTIME)
            outdata = page(name,fad,1)
            #output all the urls
            for i in outdata[1]:
                print(i[0],i[1])
                link = i[1]
                POSTER(link)
                SLEEPTIME = 15
                print('sleep',SLEEPTIME)
            time.sleep(SLEEPTIME)
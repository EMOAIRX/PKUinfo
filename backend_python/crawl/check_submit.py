# -*- coding: utf-8 -*-
import requests
import time
#nocheck!!!
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
        #read "check_submit.txt" and get the link for each line
        with open('check_submit.txt','r',encoding='UTF-8') as f:
            str_list = f.read()

        with open('check_submit.txt','w',encoding='UTF-8') as f:
            f.write('')
            f.flush()
        # print(type(total_str))
        # print(total_str)
        link_list = []
        lis = str_list.split('\n')
        print(lis)
        lis = [i for i in lis if i != '']
        for i in lis:
            link_list.append(i)
        print(link_list)
        #submit each link
        for link in link_list:
            print(link)
            try:
                POSTER(link)
            except:
                print('error POST link = ',link)
            time.sleep(2)
        time.sleep(10)
        #clear check_submit.txt

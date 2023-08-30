import requests
import re
from bs4 import BeautifulSoup
import os
import csv
import easyocr
import time
class ContentGetter:
    def __init__(self):
        
        self.reader = easyocr.Reader(
            ['ch_sim','en'],
            gpu = False,
            # detect_network= 'craft',
            # download_enabled= False,
            # model_storage_directory= '/mnt/d/projectB/py/add/model/'
        )
        print('OCR loaded')
        self.save_dir = self.set_directory()
        self.c = 0

    def delete_directory(self, directory):
        for root, dirs, files in os.walk(directory, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)  # 删除文件

            for dir in dirs:
                dir_path = os.path.join(root, dir)
                os.rmdir(dir_path)   # 删除子目录

        os.rmdir(directory)   # 删除目录

    def set_directory(self):
        save_dir = "./content"
        if os.path.exists(save_dir):
            self.delete_directory(save_dir)
            os.makedirs(save_dir, exist_ok=True)
            return save_dir
        else:
            os.makedirs(save_dir, exist_ok=True)
            return save_dir

    def ocr(self, img_dir) -> str:
        try:
            ocrinfo = self.reader.readtext(img_dir)
        except:
            return ''

        result = ''
        for item in ocrinfo:
            result += item[1]
        # print('result = ', result)
        return result

    def get_text(self, url):
        #获取并格式化
        r = requests.get(url)
        r.encoding = 'utf-8'
        html_doc = r.text
        
        #时间获取部分 
        date1 = re.search(r'var ct = "(\d+)"', html_doc).group(1)
        date1 = int(date1)
        timearray = time.localtime(date1)
        time1 = time.strftime("%Y-%m-%d %H:%M:%S", timearray)
        print(time1)
        result = ""
        result += time1 + '\n'
        
        #文字获取部分
        s = BeautifulSoup(html_doc,features='lxml')
        title = s.find(id = "activity-name").text
        result += title + '\n'

        doc = s.find_all("span")
        for item in doc:
            ptxt = re.sub('\s',' ',item.get_text())
            result += ptxt + '\n'
            
        doc = s.find_all("p")
        for item in doc:
            ptxt = re.sub('\s',' ',item.get_text())
            result += ptxt + '\n'
        return result

    def get_imginfo(self, url) -> str:
        #获取并格式化
        r = requests.get(url)
        r.encoding = 'utf-8'
        html_doc = r.text
        #图片获取部分
        s2 = BeautifulSoup(html_doc,"html.parser") 
        img = s2.find_all("img")
        result = ''
        for item in img:
            src=''
            try:
                src = item["src"]                   #有些存到了src,有些存到了data-src,判断一下
            except:
                try:
                    src = item["data-src"]
                except:
                    src = item["id"]

            if "https" not in src:                #把不是链接的抛掉
                continue

            if '=gif' in src:
                continue

            result += self.ocr(src)
            result += '\n'
        return result
        
    def get_fulltext(self, url):
        text = self.get_text(url)
        print(text)
        imginfo = '' #self.get_imginfo(url)
        print(text + imginfo)
        return text + imginfo

    # def main(self):
    #     with open("/mnt/d/projectB/py/add/urllist.csv", 'r' ,encoding = 'utf-8-sig') as f:    #utf-8会自动补前缀
    #         reader = csv.reader(f)
    #         for row in reader:
    #             print(str(self.c) + ':' + row[0])               #取列表第一个元素,不然不是链接形式
    #             url = row[0]
    #             text = self.get_fulltext(url)
    #             with open(os.path.join(self.save_dir, str(self.c) + '.txt'), 'w', encoding='utf-8') as f:
    #                 f.write(text)
    #             self.c += 1

if __name__ == "__main__":
    content_getter = ContentGetter()
    content_getter.get_fulltext('https://mp.weixin.qq.com/s/LUsA5qG5ysC77sugGcLjOA')

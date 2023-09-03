import requests
import re
from bs4 import BeautifulSoup
from WebContent import WebContent
import os
import csv
import easyocr
import time
class ContentGetter:
    def __init__(self):        
        # self.reader = easyocr.Reader(
        #     ['ch_sim','en'],
        #     gpu = False,
            # detect_network= 'craft',
            # download_enabled= False,
            # model_storage_directory= '/mnt/d/projectB/py/add/model/'
        # )
        # print('OCR loaded')
        pass

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

    def get_title(self, soup : BeautifulSoup) -> str:
        title = soup.find(id = "activity-name").text
        title = title.replace('\n', '').strip()
        return title
    
    def get_author(self, soup : BeautifulSoup) -> str:
        author = soup.find(id="js_name").text
        author = author.replace('\n', '').strip()
        return author

    def get_publish_time(self, html_doc : str) -> str:
        pattern = r"var createTime = '(.*?)';"
        match = re.search(pattern, html_doc)
        publish_time = ''
        if match:
            publish_time = match.group(1)
        return publish_time
    
    def get_text(self, soup : BeautifulSoup) -> str:
        doc = soup.find_all(["span", "p"])
        text = ''
        for item in doc:
            ptxt = re.sub('\s',' ',item.get_text())
            text += ptxt + '\n'
        return text

    def get_img_url(self, soup: BeautifulSoup) -> str:
        img = soup.find_all("img")
        # print(img)
        image_list = []
        for item in img:
            # print(item)
            if item.has_attr('src'):
                src = item['src']
            elif item.has_attr('data-src'):
                src = item['data-src']
            elif item.has_attr('id'):
                src = item['id']
            else:
                continue
            print(src)
            if "https" not in src: continue
            if '=gif' in src: continue
            image_list.append(src)
        return image_list



    def get_fullcontent(self, url) -> WebContent:
        result = WebContent()
        response = requests.get(url) #requests.models.Response
        response.encoding = 'utf-8' 
        html_doc = response.text #str
        soup = BeautifulSoup(html_doc,features='lxml') #bs4.BeautifulSoup
        result.title = self.get_title(soup)
        result.author = self.get_author(soup)
        result.publish_time = self.get_publish_time(html_doc)
        result.text = self.get_text(soup)
        result.link = url
        result.img_url = self.get_img_url(soup)
        return result

if __name__ == "__main__":
    content_getter = ContentGetter()
    url = 'https://mp.weixin.qq.com/s/CLxcCN0FhcuswCKYR-ITpA'
    result = content_getter.get_fullcontent(url)
    print(result)

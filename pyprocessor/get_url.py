#待修复，本地跑存在一些问题

import csv
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class URLGetter:
    def __init__(self):
        self.add: List[str] = []

    def get_url(self, name: str):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
        # 进入网页
        driver.get("https://weixin.sogou.com/")

        driver.find_element(By.ID, 'query').send_keys(name)
        driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()  # 使用CSS选择器定位元素
        try:
            driver.find_element(By.CLASS_NAME, 'swz2').click()
        except:
            print("No such element found")
            driver.quit()
            return

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@target='_blank' and contains(@uigs, 'account_article_0')]")))
        driver.find_element(By.XPATH, "//a[@target='_blank' and contains(@uigs, 'account_article_0')]")\
            .send_keys(Keys.CONTROL + Keys.RETURN)

        for window_handle in driver.window_handles:
            # 切换到窗口
            driver.switch_to.window(window_handle)
            # 获取当前窗口的URL
            url = driver.current_url
            print(url)
            if 'mp.weixin.qq' in url:
                current_url = driver.current_url
                print("当前页面的URL:", current_url)

                redirected_url = driver.execute_script("return window.location.href")

                # headers = {'User-Agent': 'Mozilla/5.0 (windows NT 10.0;WOW64) AppleWebkit/537'}
                # response = requests.get(current_url,headers=headers)
                # redirected_url = response.url
                print("重定向后的URL:", redirected_url)

                self.add.append(redirected_url)

        print('\n....done....')
        driver.quit()

    # def main(self):
    #     self.set_directory()

    #     with open(os.path.join(self.save_dir, "namelist2.csv"), 'r', encoding='utf-8') as f:
    #         reader = csv.reader(f)
    #         for row in reader:
    #             name = row[0]

    #             self.get_url(name)

    #     with open(os.path.join(self.save_dir, "urllist.csv"), 'w', newline='') as f:
    #         writer = csv.writer(f)
    #         writer.writerows([[url] for url in self.add])


if __name__ == '__main__':
    url_getter = URLGetter()
    print(url_getter.get_url('北京大学信息科学技术学院'))
    # url_getter.main()
import os
import pickle
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

brower = webdriver.Chrome()
wait = WebDriverWait(brower, 10)

def getTaobaoCookies():
    # get login taobao cookies
    url = "https://www.taobao.com/"
    brower.get("https://login.taobao.com/member/login.jhtml")
    while True:
        print("Please login in taobao.com!")
        time.sleep(3)
        # if login in successfully, url  jump to www.taobao.com
        while brower.current_url ==  url:
            tbCookies  = brower.get_cookies()
            brower.quit()
            cookies = {}
            for item in tbCookies:
                cookies[item['name']] = item['value']
            outputPath = open('taobaoCookies.pickle','wb')
            pickle.dump(cookies,outputPath)
            outputPath.close()
            return cookies

a=getTaobaoCookies()
print(a)

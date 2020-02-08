import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

wd = webdriver.Chrome()
wait = WebDriverWait(wd,10)

a=os.getcwd()
def get_JD_cookies():
    url =r'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F'
    correct_url='https://www.jd.com/'
    wd.get(url)
    while True:
        print("Please login in jd.com")
        print(wd.current_url)
        print(correct_url)
        time.sleep(10)
        while wd.current_url == correct_url:
            jd_cookies = wd.get_cookies()
            wd.quit()
            cookies={}
            for item in jd_cookies:
                cookies[item['name']]=item['value']
            out_put_path = open('jd_cookies.pickle','wb')
            pickle.dump(cookies,out_put_path)
            out_put_path.close()
            return cookies

a=get_JD_cookies()
print(a)

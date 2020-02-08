import pickle
import os
import time
from selenium import webdriver

cookies_name='jd_cookies.pickle'

def get_cookies(cookies_name):
    if os.path.exists(cookies_name):
        f=open(cookies_name,'rb')
        jd_cookies=pickle.load(f)
    else:
        print('no cookies there')
    return jd_cookies

jd_cookies=get_cookies(cookies_name)

wd=webdriver.Chrome()
wd.get('https://www.jd.com/')
for cookie in jd_cookies:
    wd.add_cookie({
        'domain':'.jd.com',
        'name':cookie,
        'value':jd_cookies[cookie],
        'path':'/',
        'expires':None
    })
wd.get('https://www.jd.com')

time.sleep(3)

wd.quit()

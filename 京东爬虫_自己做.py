from selenium import webdriver
import os
import time
import cv2

url='https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F'
wd = webdriver.Chrome()
wd.get(url)
time.sleep(3)
login_url=r'//*[@class="login-tab login-tab-r"]'        #这个是京东用密码登陆的那个按钮的特征
elenemt=wd.find_element_by_xpath(login_url)
elenemt.click()


time.sleep(3)

wd.quit()

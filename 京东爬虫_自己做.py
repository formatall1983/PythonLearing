#coding=utf-8
from selenium import webdriver
import os
import time
import cv2
import requests
import base64

path=r'D:\OneDrive\工作\Github\PythonLearing'
os.chdir(path)
print(path)
url='https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F'
login_name='13761360968'
login_password='qqqqqwwwww'
login_name_box_xpath=r"//*[@id='loginname']"      #用于查找京东登录名输入框的Xpath写法
login_pw_box_xpath=r"//*[@id='nloginpwd']"
login_button_xpath=r'//*[@id="loginsubmit"]'
wd = webdriver.Chrome()


wd.get(url)
time.sleep(3)
login_url=r'//*[@class="login-tab login-tab-r"]'        #这个是京东用密码登陆的那个按钮的特征
elenemt=wd.find_element_by_xpath(login_url)
elenemt.click()
login_name_box=wd.find_element_by_xpath(login_name_box_xpath)
login_name_box.send_keys(login_name)
login_password_box=wd.find_element_by_xpath(login_pw_box_xpath)
login_password_box.send_keys(login_password)
login_button=wd.find_element_by_xpath(login_button_xpath)
login_button.click()




def move_pic():
    big_pic_xpath=r'//*[@class="JDJRV-bigimg"]/img'
    small_pic_xpath=r'//*[@class="JDJRV-smallimg"]/img'
    big_pic_src=wd.find_element_by_xpath(big_pic_xpath).get_attribute('src')
    small_pic_src=wd.find_element_by_xpath(small_pic_xpath).get_attribute('src')
    big_pic_name='big_pic.png'
    small_pic_name='small_pic.png'
    big_pic=big_pic_src[22:]
    small_pic=small_pic_src[22:]
    img=base64.urlsafe_b64decode(big_pic + '='*(4-len(big_pic)%4))
    f=open(big_pic_name,'wb')
    f.write(img)
    f.close
    
    img=base64.urlsafe_b64decode(small_pic + '='*(4-len(small_pic)%4))
    f=open(small_pic_name,'wb')
    f.write(img)
    f.close


move_pic()


time.sleep(3)

wd.quit()

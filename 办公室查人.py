#couding=utf-8
from selenium import webdriver      #引入webdriver
import time
from selenium.webdriver.chrome.options import Options       #无头模式必须,为无头模式指定参数
chrome_options=Options()        #无头模式必须, 为无头模式指定参数
chrome_options.add_argument('--headless')       #固定写法,无头模式必须那么写
chrome_options.add_argument('--disable-gpu')        #固定写法,无头模式必须那么写
path=r'cchromedriver.exe'       #本行作为示例,如果weidriver不再默认位置, 可以指定,指定方式为:  wd=webdriver(path)

ad='http://192.168.1.1/oraybox/login.html'       #本行为要爬取的网址
def check(address):     #该函数为爬取的函数
    wd=webdriver.Chrome(chrome_options=chrome_options)      #创建浏览器对象,这里的参数为设置无头浏览的参数,默认可以指定浏览器驱动地址,例如:wd=webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
    wd.get(address)
    wd.implicitly_wait(10)      #每0.5秒系统会自动检测需要的元素有没有加载到, 如果没有加载到, 则等待0.5秒再试, 一直持续10秒
    element=wd.find_element_by_id('password')       #用css的方法找到密码输入框
    element.send_keys('cd1983111\n')        #输入密码以后点击
    element=wd.find_element_by_xpath('//*[@id="manage-list"]/li[4]/a')      #点击'本地设备',这个xpath的查找内容, 是直接用chrome的copy-xPath的方法得到的
    element.click()
    #element=wd.find_element_by_xpath('//*[@id="devices-list"]/tr[1]/td[1]/span/../..')
    elements=wd.find_elements_by_xpath('//*[@id="devices-list"]/tr/td[1]/a')       #等待本地设备加载出来,然后内容给到elements,因为每个内容有2个td标签, 所以只要获取第一个就可以了
    result=[]
    for element in elements:        #循环输出本地设备
        #print(element.get_attribute('outerHTML'))       #本行做示例,打印得到的所有html代买
        #print(element.text)        #打印文本内容
        #print(element.get_attribute('data-alias'))      #本行做实例, 打印得到的内容中的特定属性内容
        result.append(element.text)
    wd.quit()
    return result

a=check(ad)
print(a)

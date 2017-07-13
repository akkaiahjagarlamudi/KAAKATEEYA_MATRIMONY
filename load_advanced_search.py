from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4


count =0
i=0
path1 = r'C:\Python27\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(path1)
browser.get('http://kaakateeya.com/dashboard/C')
time.sleep(3)
browser.find_element_by_link_text("Member Login").click();
username = browser.find_element_by_id("txtUserName")
password = browser.find_element_by_id("txtPassword")

username.send_keys("akkaiah.j@gmail.com")
password.send_keys("einstein1")
browser.find_element_by_id("btnUserLogin").click();
time.sleep(10)
browser.find_element_by_xpath('//*[@id="ulastro"]/li[13]/div[2]/input').click()
time.sleep(10)

browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[1]/div[1]/ul/li/a[4]').click()
time.sleep(5)
browser.find_element_by_link_text("Search").click();
time.sleep(3)
browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/md-content/md-tabs/md-tabs-wrapper/md-tabs-canvas/md-pagination-wrapper/md-tab-item[2]/span').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="tab-content-3"]/div/div/form/div/div[2]/div[2]/div/div[2]/div/button').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="tab-content-3"]/div/div/form/div/div[2]/div[2]/div/div[2]/div/ul/li[26]/a/label').click()
time.sleep(20)
while(count!=430):
    try:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        browser.find_element_by_xpath('//*[@id="Div1"]/div/partner-data/div[3]/div['+ str(10+i*8)+']/div[1]/a/span').click()
        #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #browser.find_element_by_xpath('//*[@id="PartnerProfilles"]/div['+str(10+i*9)+']/div[1]/a/span').click()
    except Exception, err:
        i=i-1
        print Exception, err
        time.sleep(3)
    #browser.find_element_by_css_selector('#PartnerProfilles > div.row.col-lg-10 > div:nth-child(1) > a > span').click()
    #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    i=i+1
    count = count+1
#browser.find_element_by_link_text("India, USA").click();
#browser.find_element_by_xpath('//*[@id="advancedcountryliving"]/div/button/span').click()
#time.sleep(3)
#time.sleep(3)
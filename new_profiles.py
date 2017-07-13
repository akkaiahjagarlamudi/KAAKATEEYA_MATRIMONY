from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4



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
time.sleep(3)
browser.find_element_by_xpath('//*[@id="ulastro"]/li[13]/div[2]/input').click()
time.sleep(5)
i=0
count = 0

while(count!=430):
    try:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        browser.find_element_by_xpath('//*[@id="Div1"]/div/partner-data/div[3]/div['+ str(11+i*9)+']/div[1]/a/span').click()
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

elem3 = browser.page_source
#print elem3.text

f = open("D:\kaaka\search_new\NewProfiles.txt","w+")
# + creates a file if its not there
f1 = open("D:\kaaka\search_new\Profiles.txt","ab+")
str = f1.read()
f1.seek(0,2)

soup = bs4.BeautifulSoup(elem3,'html.parser')
for a in soup.findAll('p',{"class" : "label_check pull-left clearfix"}):
        #print a.text
        if a.text.strip() not in str:
            f.write(a.text.strip()+'\n')
            f1.write(a.text.strip()+'\r\n' )
            #or print a.string


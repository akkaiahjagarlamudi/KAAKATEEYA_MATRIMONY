from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import bs4



f = open("D:\kaaka\search_new\NewProfiles.txt","w+")
# + creates a file if its not there
f1 = open("D:\kaaka\search_new\Profiles.txt","ab+")
str = f1.read()
f2 = open("D:\kaaka\search_new\Kaakateeya Marriages.html","ab+")
elem3 = f2.read()
f1.seek(0,2)

soup = bs4.BeautifulSoup(elem3,'html.parser')
for a in soup.findAll('p',{"class" : "label_check pull-left clearfix"}):
        #print a.text
        if a.text.strip() not in str:
            f.write(a.text.strip()+'\n')
            f1.write(a.text.strip()+'\r\n' )
            #or print a.string


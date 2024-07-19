from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
driver = webdriver.Chrome()
url = 'http://127.0.0.1/static/emp.html'
driver.get(url)
sleep(1)
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
table=soup.find('table')

trs=table.find_all('tr')
for idx,tr in enumerate(trs):
    if idx ==0:
        continue
    tds=tr.find_all('td')
    myname =tds[1].text
    addr = tds[3].text
    print("{}\t{}".format(myname,addr))



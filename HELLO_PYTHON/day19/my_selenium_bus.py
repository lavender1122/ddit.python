from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import enum
driver = webdriver.Chrome()
url = 'https://traffic.daejeon.go.kr/bus/busInfo'
driver.post(url)
sleep(1)
html=driver.page_source
# print(html)

soup =BeautifulSoup(html,'lxml')
# table=soup.select_one("table")
# # print(table)
# trs=table.select('tr')
# for idx,tr in enumerate(trs):
#     if idx ==0:
#         continue
#     tds=tr.find_all('td')
#     myname =tds[1].text
#     addr = tds[3].text
#     print("{}\t{}".format(myname,addr))




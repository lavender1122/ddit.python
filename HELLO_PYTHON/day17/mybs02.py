import requests                  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup    # HTML을 파싱하는 모듈
from psutil._common import addr
 
# 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
res  = requests.get('http://127.0.0.1:88')
html = res.text
# print(html)
soup = BeautifulSoup(res.text, 'html.parser')

trs=soup.find_all('tr')
# print(trs)

for idx,tr in enumerate(trs):
    if idx ==0:
        continue
    tds=tr.find_all('td')
    myname =tds[1].text
    addr = tds[3].text
    print("{}\t{}".format(myname,addr))

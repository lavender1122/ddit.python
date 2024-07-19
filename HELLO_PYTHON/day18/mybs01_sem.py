import requests                  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup    # HTML을 파싱하는 모듈
import datetime
from day18.daostock import DaoStock

ds=DaoStock()
 
ymd=datetime.datetime.today().strftime('%Y%m%d_%H%M')

print(ymd) 
 
res = requests.get('https://stock.mk.co.kr/domestic/all_stocks')

soup = BeautifulSoup(res.text, 'html.parser')

# print(res.text)
print("------------------------------------------------------")

divs = soup.find_all("div", class_="st_name")

for idx,div in enumerate(divs):
    s_name = div.text.strip()
    s_code=div.find("a")['href'].split("/")[3]
    price=div.parent.find_all("div")[1].text.strip().replace(",","")
    cnt = ds.insert(s_code, s_name, price, ymd)
    print(idx,s_name,s_code,price,ymd,cnt)

#strip() : 왼쪽 오른쪽 공백제거


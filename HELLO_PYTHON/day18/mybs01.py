import requests                  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup    # HTML을 파싱하는 모듈
from datetime import datetime
from day18.daostock import DaoStock
 
# 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
res = requests.get('https://stock.mk.co.kr/domestic/all_stocks')
html = res.text
soup = BeautifulSoup(html, 'html.parser')

# ul 태그 중에 class가 sty1인 요소를 선택
ul = soup.select_one('ul.sty1')

# ul에서 모든 종목의 이름과 가격을 가져와서 출력
names = ul.select('div.st_name')   # 종목명을 담은 div 태그들 선택
prices = ul.select('div.st_price')  # 가격을 담은 div 태그들 선택
# print(type(prices.text.replace(',',''))) //str
# print(type(int(prices.text.replace(',','')))) //int

now = datetime.now()
# print("문자열 변환 : ",ymd)

de = DaoStock()
# de.insert(1, 1, 1, 1) 테스트 완료

for idx, (name, price) in enumerate(zip(names, prices)):
    s_code='kr'+str(idx)
    s_name = name.text.strip()   # 종목명 텍스트 가져오기 (앞뒤 공백 제거)
    s_price = price.text.replace(',','').strip()  # 가격 텍스트 가져오기 (앞뒤 공백 제거)
    # s_price = price.text.replace(',','')  # 가격 텍스트 가져오기 (앞뒤 공백 제거)
    ymd=now.strftime('%Y%m%d_%H%M')
    de.insert(s_code, s_name, s_price, ymd)
    print("{}\t{}\t{}\t{}".format(s_code, s_name, s_price,ymd))

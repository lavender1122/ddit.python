import requests                  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup    # HTML을 파싱하는 모듈
 
# 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
res  = requests.get('http://127.0.0.1:88')
html = res.text
# print(html)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.find('table').find('tr'))
print(soup.find_all('table')[0].find_all('tr')[0])

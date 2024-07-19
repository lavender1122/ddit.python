import requests                  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup    # HTML을 파싱하는 모듈
 
# 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
res  = requests.get('http://localhost/static/emp.html')
html = res.text
print(html)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.find('table').find('tr'))

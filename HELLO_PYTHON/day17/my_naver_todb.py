# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
import requests                  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup    # HTML을 파싱하는 모듈
from day17.daoemp import DaoBlog
import json
from day17.my_naver_json import my_json
client_id = "iCbb4ifEIF_R7lWqJrUJ"
client_secret = "lynGe1kqtz"
encText = urllib.parse.quote("오류동맛집")
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # JSON 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
response_body = response.read()
html = response_body.decode('utf-8')
soup= BeautifulSoup(html,"xml")
items = soup.find_all('item')
de = DaoBlog()
oj=json.loads(my_json)
items = oj['items']

for idx,item in  enumerate(items):
    title = item["title"]
    link = item["link"]
    description = item["description"]
    bloggername = item["bloggername"]
    bloggerlink = item["bloggerlink"]
    postdate = item["postdate"]
    cnt = de.insert(title, link, description, bloggername, bloggerlink, postdate)
    print("{}\t{}\t{}".format(idx, title, bloggername))   
    print("추가 성공!",cnt)

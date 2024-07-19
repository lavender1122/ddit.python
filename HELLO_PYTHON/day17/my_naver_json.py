# 네이버 검색 API 예제 - 블로그 검색
import json
import os
import sys
import urllib.request
import requests                  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup    # HTML을 파싱하는 모듈
client_id = "iCbb4ifEIF_R7lWqJrUJ"
client_secret = "lynGe1kqtz"
encText = urllib.parse.quote("오류동맛집")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
response_body = response.read()
my_json = response_body.decode('utf-8')

oj=json.loads(my_json)
items = oj['items']

for idx,item in  enumerate(items):
    title = item["title"]
    bloggername = item["bloggername"]
    print("{}\t{}\t{}".format(idx, title, bloggername))    
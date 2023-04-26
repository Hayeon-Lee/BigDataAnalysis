#과제 1: 블로그 검색, "빅데이터" 정확도 순, 1~110번 제목 출력
import os
import sys
import datetime
import time
import json
import urllib.request

clientid = ""
key=""

LEC = True

def getRequestUrl(url):
    req=urllib.request.Request(url)
    req.add_header("X-Naver-Client-id", clientid)
    req.add_header("X-Naver-Client-Secret", key)

    try: 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
        
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getNaverSearch(svc, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    svc = "/%s.json" % svc
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)

    url = base + svc + parameters
    responseDecode = getRequestUrl(url)

    if responseDecode == None:
        return None
    else:
        return json.loads(responseDecode)
    
def getPostData(resultJ, resultL):
    for item in resultJ['items']:
        resultL.append(item['title'])
    print(len(resultL))

def main():
    svc = 'blog'   # 크롤링 할 대상  : news, blog, encyc, shop
    srcText = input('검색어를 입력하세요: ')
    resultL=[]
    start=1
     
    jsonResponse = getNaverSearch(svc, srcText, start, 100)
    if jsonResponse != None:
        getPostData(jsonResponse, resultL)
    
    jsonResponse = getNaverSearch(svc, srcText, 101, 10)
    if jsonResponse != None:
        getPostData(jsonResponse, resultL)

    print("가져온 데이터 : %d 건" %len( resultL))

    for title in resultL:
        title = title.replace('<b>', '')
        title = title.replace('</b>','')
        print(title)

    
if __name__ == '__main__':
    main()
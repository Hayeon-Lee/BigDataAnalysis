#과제2: api코드로 자신의 이름, email 출력하기
import urllib3
import facebook
import requests

token = ''
graph = facebook.GraphAPI(access_token = token)
profile = graph.request('me?fields=id,name,birthday, age_range, email')

print(profile['name'])
print(profile['email'])
import urllib
import json
import re

#getGeoCode_2 (지번주소용)
def getGeoCode_2( addr) :
    q= urllib.parse.quote(addr)
    data = urllib.request.urlopen("") #key
    result = json.loads(data.read())
    if (result['response']['status'] =='OK') :
        x=float(result['response']['result']['point']['x'])
        y=float(result['response']['result']['point']['y'])
    else :
        x,y=0,0
    return x, y

#after_trimming은 과제2번에서 했습니다.
#지번 주소로 trimming 한 데이터 처리
for index, row in after_trimming.iterrows():
    if after_trimming.loc[index,'x']==0:
        cx, cy = getGeoCode_2(after_trimming.loc[index, 'address2'])
        after_trimming.loc[index, 'x'] = cx
        after_trimming.loc[index, 'y'] = cy

#이후에 남은 도로명 주소로 trimming 한 데이터 처리
for index, row in after_trimming.iterrows():
    if after_trimming.loc[index, 'x']==0:
        cx, cy = getGeoCode(after_trimming.loc[index, 'address2'])
        after_trimming.loc[index, 'x'] = cx
        after_trimming.loc[index, 'y'] = cy

not_trimming=0
for index, row in after_trimming.iterrows():
    if after_trimming.loc[index, 'x']==0:
        not_trimming+=1
print("x좌표가 0으로 된 데이터 갯수: ", not_trimming)

#교수님께서 12개까지 줄여보라 하셨고 실행결과 5개까지 줄여보았습니다.
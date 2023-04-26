#학교 공식 홈페이지에서 7개의 학과 이름 print 하기
from bs4 import BeautifulSoup
import urllib.request

def ssuMajor(result):
    ssuUrl='https://ssu.ac.kr/%ea%b5%90%ec%9c%a1-%c2%b7-%ec%97%b0%ea%b5%ac/%eb%8c%80%ed%95%99%ec%86%8c%ea%b0%9c/it%eb%8c%80%ed%95%99/'
    html=urllib.request.urlopen(ssuUrl)
    soupSSU = BeautifulSoup(html, 'html.parser')
    tag_div = soupSSU.find_all('div', 'vc_row wpb_row vc_row-fluid vc_custom_1559024152576') #학과 정보가 있는 div
    tag_a1 = tag_div[0].find_all('a') #그 안의 a태그 분류
    tag_a2 = tag_div[1].find_all('a') #그 안의 a태그 분류

    for content in tag_a1: #첫번째 a 묶음 
        name = content.text.strip()
        name = name.replace('\n', '')
        result.append(name)
    
    for content in tag_a2: #두번째 a 묶음
        name = content.text.strip()
        name = name.replace('\n', '')
        result.append(name)
        
    return result

def main():
    result = []
    result = ssuMajor(result)
    
    for name in result:
        print(name)
       
if __name__ == '__main__':
     main()
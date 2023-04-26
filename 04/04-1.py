###과제1 : 의미상 nominal 인 column 만 count 하기

#내 코드

for c in titanic.columns : 
    if len(titanic[c].value_counts())<=3:
        print(titanic[c].value_counts())
        
#위에 나와있는 데이터 중 컬럼 수가 지나치게 많은 컬럼은 의미가 없다고 판단하였습니다.
#굵직한 데이터(alive, who, class, sex, survived 등의 데이터)들을 살펴보니 길이가 3 이하인 것을 알게되었고, len이 3보다 작거나 같을 경우 출력하였습니다.
## *과제 1 : 성별, 혈액형 별 몸무게의 평균
#성별과 혈액형 별 몸무게의 평균

s_table = {} #{성별: {혈액형 : [몸무게, 명수], 혈액형 : [몸무게, 명수]}...}
for rec in Table:
    sexType = rec[1] #성별
    bloodType = rec[5] #혈액형
    weight = rec[7] #몸무게
    if sexType in s_table:#이 성별을 체크한 적이 있는 경우
        if bloodType in s_table[sexType]: #이 성별 중에서 이 혈액형을 체크했다면
            s_table[sexType][bloodType] = [s_table[sexType][bloodType][0]+weight, s_table[sexType][bloodType][1]+1]
        else: #이 성별 중에서 이 혈액형을 체크하지 않았다면
            s_table[sexType][bloodType] =  [weight, 1]
    else: #이 성별을 체크한 적이 없는 경우
        s_table[sexType] = {bloodType:[weight,1]}

#출력하기
for s_key, s_value in s_table.items():
    for b_key, b_value in s_value.items():
        print(s_key, end=", ")
        print(b_key, end=", ")
        print(b_value[0]/b_value[1])
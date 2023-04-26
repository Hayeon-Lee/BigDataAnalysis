## 과제 4 : 각 사람의 BMI ( 몸무게 kg /  (키 m ^2) )를 구하여 column을 추가하시오
w=df["weight"]
h=((df["height"] * 0.01) ** 2)
bmi = w/h
df["BMI"] = bmi
print(df)

'''
#다른 학우 풀이
df["BMI"] = df["weight"]/(df["height"]*0.01)**2
print(df)
'''
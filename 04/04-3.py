### 과제 3 : fare 의 통계적 outlier를 구하여 filtering ( outlier인 값만 출력) 하시오 

so = titanic['fare'].quantile(0.25)
eo = titanic['fare'].quantile(0.75)

IQR = eo - so #75에서 25를 빼면 50이 나온다 == IQR
outlier = IQR * 1.5 #outlier는 IQR 에 1.5배를 한 것이다

print(titanic[(titanic['fare']<so-outlier)]['fare'])
print(titanic[(titanic['fare']>eo+outlier)]['fare'])
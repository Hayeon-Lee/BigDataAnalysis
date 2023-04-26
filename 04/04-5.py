import seaborn as sns
import pandas as pd

titanic= sns.load_dataset("titanic")
val = titanic['fare'].quantile(0.99)
titanic_copy = titanic

#titanic에서 fare 값이 val 보다 큰 부분의 인덱스 추출
location = titanic_copy.loc[titanic_copy['fare']>val]['fare']
indexes = location.index

#indexes 배열에 있는 인덱스의 fare 값은 val보다 크므로 val로 교체
for i in indexes:
    titanic_copy.loc[i, 'fare'] = val
plt.boxplot(titanic_copy['fare'])

#결과 plot 보시면 최댓값이 250으로 나와있는 것을 확인하실 수 있습니다.
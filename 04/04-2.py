### 과제 2 : class와 embarked 필드를 이용해 0.5 비율을 층화추출하시오 

import seaborn as sns
import pandas as pd

titanic= sns.load_dataset("titanic")

titanic=titanic.dropna(subset=['pclass'])
titanic=titanic.dropna(subset=['embarked'])
titanic['CE'] = titanic['pclass'].astype('str')+titanic['embarked']

from sklearn.model_selection import train_test_split
train_data, test_data = train_test_split(titanic, test_size=0.5, random_state=2, stratify=titanic['CE'])

print("전체 결과값")
print(test_data)
print ("결과값:\n", test_data.CE.value_counts(normalize=True))
## 과제1 : class별 생존자수를 비교하고 (시각화포함), 통계적으로 유의한 차이인지 분석하시오
import seaborn as sns
import pandas as pd
from scipy import stats
titanic= sns.load_dataset("titanic")

ct = pd.crosstab(titanic["class"], titanic["survived"], normalize = True)
ct.plot.bar(stacked=True)

print(stats.chi2_contingency(ct))
#p-value 가 0.05보다 크기 때문에 유의미한 차이가 있지 않다.
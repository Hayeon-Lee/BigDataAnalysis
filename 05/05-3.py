# red wine 읽어오기
red_df= pd.read_csv("winequality-red.csv", sep=";")

#가장 상관관계가 높은 변수 찾기
q_corr = red_df.corr()['quality'] #series 데이터
tmp_q_corr = q_corr #컬럼과 값 추가를 위해 따로 저장해둠
q_corr.drop('quality', axis=0, inplace=True) #자기 자신과의 상관관계 제거
q_corr_sort = q_corr.sort_values(ascending=False)
print("가장 상관관계가 높은 변수는:", q_corr_sort.index[0])

#headmap으로 표현
sns.heatmap(red_df.corr())

# 해석: 가장 상관관계가 높은 변수는 alcohol이다.
# heatmap으로 표현하였을 때, quality에서 alcohol이 가장 밝은 색으로 표현되었다.
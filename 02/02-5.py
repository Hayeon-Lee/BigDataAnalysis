## 과제 5 : studentlist의 혈액형 별 도수를 bar 차트로 그리시오

new_df = df.groupby(["bloodtype"]).size()
index = new_df.index
plt.bar(index, new_df[index])

'''
#다른 학우 풀이
pd.DataFrame(df.groupby('bloodtype').size()).rename(columns = {0:"count"}).plot(kind="bar")
#dataframe으로 바로 표를 만들 수 있는데 count와 index 매칭이 한개밖에 안되므로, 이걸 plot호출하면 바로 그래프 그리기 가능 
'''
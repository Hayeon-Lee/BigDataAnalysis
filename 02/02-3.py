## 과제 3 : 혈액형이 B형인 사람의 키의 평균을 구하시오

df.loc[df["bloodtype"]=="B", ["height"]]["height"].mean()
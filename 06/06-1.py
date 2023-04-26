## 과제1 : 전체 변수로 부터  MedIncome을 예측하는 모델을 만들고, 예측 결과의 상관계수를 계산하시오 
boston= load_boston()
boston_df = pd.DataFrame(boston.data, columns = boston.feature_names)
boston_df['PRICE'] = boston.target
y = boston_df['MedInc']
x = boston_df['PRICE']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
lr = LinearRegression()
lr.fit(x_train.values.reshape(-1,1),y_train)
y_predict = lr.predict(x_test.values.reshape(-1,1))
print(lr.intercept_)
np.round(lr.coef_,1)
mse = mean_squared_error(y_test,y_predict)
mse
rsme = np.sqrt(mse)
rsme
plt.scatter(y_test,y_predict)
stats.pearsonr(y_test,y_predict) #상관계수 0.38
boston_df[['PRICE','MedInc']].corr()
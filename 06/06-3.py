housing = fetch_california_housing()
Y = housing.target
X = housing.data

m = LinearRegression()
kfold=KFold(n_splits=5, shuffle=True, random_state=1) # shuffle = False 면 고정 추출
scores= cross_val_score(m, X, Y, cv=kfold, scoring=make_scorer(mean_squared_error))
print (scores)
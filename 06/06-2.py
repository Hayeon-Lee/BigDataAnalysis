data_df["h10"]= data_df["horsepower"]
X = data_df.drop(['horsepower'], axis=1, inplace=False)

data_df = pd.read_csv("auto-mpg.csv",header=0,engine='python')
print(data_df.shape)

data_df.info()

data_df = data_df.drop(['car_name','origin'],axis = 1,inplace = False)
data_df.info()
# horsepower 1/10 으로 줄인다.
#data_df.horsepower = data_df.horsepower.astype('int')
data_df[data_df.horsepower == '?'] # horse ? 값찾기
data_df.horsepower = data_df.horsepower.replace('?',np.NAN)
data_df = data_df.dropna()
data_df.horsepower = data_df.horsepower.astype('int')
data_df.horsepower = data_df.horsepower * 0.1
data_df.head()
y = data_df['mpg']
x = data_df.drop(['mpg'],axis=1,inplace = False)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=0)
lr = LinearRegression()
lr.fit(x_train,y_train)
y_predict = lr.predict(x_test)
print(np.round(lr.intercept_,2))
print(lr.coef_)
mse = mean_squared_error(y_test,y_predict)
print(mse)
rsme = np.sqrt(mse)
print(rsme)
coef = pd.Series(data=lr.coef_,index = x.columns)
coef
import matplotlib.pyplot as plt
import seaborn as sns
fig, axs = plt.subplots(figsize=(16, 16), ncols=3, nrows=2)

x_features = ['model_year', 'acceleration', 'displacement', 'horsepower','weight', 'cylinders']
plot_color = ['r', 'b', 'y', 'b','g', 'r']
print(data_df.head())
for i, feature in enumerate(x_features):
      row = int(i/3)
      col = i%3
      sns.regplot(x=feature, y='mpg', data=data_df, ax=axs[row][col], color=plot_color[i])
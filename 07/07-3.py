#중요 feature 10개 사용 성능
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

#X, Y 정의
Y=b_cancer.target
Xraw=b_cancer.data

#top 10개 feature 구하기
X_train = pd.read_csv('UCI_HAR_Dataset/train/X_train.txt', sep='\s+',header=None,  engine='python')
feature_importance_values = dt_HAR.feature_importances_
feature_importance_values_s = pd.Series(feature_importance_values, index=X_train.columns)
feature_top10 = feature_importance_values_s.sort_values(ascending=False)[:10]
X_trainraw = X_train.iloc[:,feature_top10.index]

#모델 생성
X_trainraw, X_testraw, Y_train, Y_test=train_test_split(Xraw, Y, test_size=0.3)
model_logist = LogisticRegression(max_iter=5000)
model_logist.fit(X_trainraw, Y_train)
Y_predictraw=model_logist.predict(X_testraw)

accuracy_raw=accuracy_score(Y_test, Y_predictraw)
precision_raw=precision_score(Y_test, Y_predictraw)
recall_raw=recall_score(Y_test, Y_predictraw)
f1_raw=f1_score(Y_test, Y_predictraw)

print('정확도: {0:.3f}, 정밀도: {1:.3f}, 재현율: {2:.3f},  F1: {3:.3f}'.format(acccuracy,precision_raw,recall_raw,f1_raw))

#기존 성능 (과제 1번 위에 있는 코드의 실행결과(성능)와 동일함 )
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

scaler = StandardScaler()
b_cancer_scaled = scaler.fit_transform(b_cancer.data) #차원 조절, data에 맞춰서
Y = b_cancer_df['diagnosis']
X = b_cancer_scaled 

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
lr_b_cancer = LogisticRegression()
lr_b_cancer.fit(X_train, Y_train)
Y_predict = lr_b_cancer.predict(X_test)

acccuracy = accuracy_score(Y_test, Y_predict)
precision = precision_score(Y_test, Y_predict)
recall = recall_score(Y_test, Y_predict)
f1 = f1_score(Y_test, Y_predict)

print('정확도: {0:.3f}, 정밀도: {1:.3f}, 재현율:{2:.3f},  F1: {3:.3f}'.format(acccuracy,precision,recall,f1))
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

b_cancer = load_breast_cancer()
scaler=StandardScaler()
b_cancer_scaled = scaler.fit_transform(b_cancer.data)

Y=b_cancer.target
X=b_cancer_scaled

pca = decomposition.PCA(n_components=3)
pca.fit(X)
X=pca.transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3, random_state=0)

model=svm.SVC()
model.fit(X_train, Y_train)

accuracy=accuracy_score(Y_test, Y_predict)
precision=precision_score(Y_test, Y_predict)
recall=recall_score(Y_test, Y_predict)
f1=f1_score(Y_test, Y_predict)
roc_auc=roc_auc_score(Y_test, Y_predict)

print('정확도: {0:.3f}, 정밀도: {1:.3f}, 재현율: {2:.3f},  F1: {3:.3f}'.format(acccuracy,precision,recall,f1))
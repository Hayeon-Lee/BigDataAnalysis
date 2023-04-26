Y=b_cancer_df['diagnosis']
X_raw=b_cancer.data
model_logist = LogisticRegression(max_iter=5000) #리밋 없으면 한계가 나온다는 워닝 나옴! 그래서 미리 준 것
X_trainraw, X_testraw, Y_train, Y_test = train_test_split(X_raw, Y, test_size=0.3, random_state=0)
model_logist.fit(X_trainraw, Y_train)
Y_predictraw=model_logist.predict(X_testraw)
print (confusion_matrix(Y_test, Y_predictraw))
print (confusion_matrix(Y_test, Y_predict))

acccuracy_raw = accuracy_score(Y_test, Y_predictraw)
precision_raw = precision_score(Y_test, Y_predictraw)
recall_raw = recall_score(Y_test, Y_predictraw)
f1_raw = f1_score(Y_test, Y_predictraw)

print('정확도: {0:.3f}, 정밀도: {1:.3f}, 재현율: {2:.3f},  F1: {3:.3f}'.format(acccuracy,precision_raw,recall_raw,f1_raw))
print('정확도: {0:.3f}, 정밀도: {1:.3f}, 재현율: {2:.3f},  F1: {3:.3f}'.format(acccuracy,precision,recall,f1))

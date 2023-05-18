nsmc_train_df #훈련용


nsmc_test_df #평가용

#TF-IDF 기반 피처 벡터 생성
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(tokenizer = okt_tokenizer, ngram_range=(1,1), min_df=3, max_df=0.9) # 3개 미만 문서에 나오는 단어 제거, 90%이상 문서에 나오는 단어제거
tfidf.fit(nsmc_train_df['document'])
nsmc_train_tfidf = tfidf.transform(nsmc_train_df['document'])

#로지스틱 회귀 기반 분석모델 생성
from sklearn.linear_model import LogisticRegression
SA_lr = LogisticRegression(random_state = 0)

SA_lr.fit(nsmc_train_tfidf, nsmc_train_df['label']) # X, y

#로지스틱 회귀의 best 하이퍼 파라미터 찾기
params = {'C': [1, 3, 3.5, 4, 4.5, 5]}
SA_lr_grid_cv = GridSearchCV(SA_lr, param_grid=params, cv=3, scoring='accuracy', verbose=1)


#최적 분석 모델 훈련
SA_lr_grid_cv.fit(nsmc_train_tfidf, nsmc_train_df['label'])

print(SA_lr_grid_cv.best_params_, round(SA_lr_grid_cv.best_score_, 4))

# 최적 파라미터의 best 모델 저장
SA_lr_best = SA_lr_grid_cv.best_estimator_


#평가용 데이터를 이용하여 감성 분석 모델 정확도
# 평가용 데이터의 피처 벡터화 
nsmc_test_tfidf = tfidf.transform(nsmc_test_df['document'])
test_predict = SA_lr_best.predict(nsmc_test_tfidf)
from sklearn.metrics import accuracy_score

print('감성 분석 정확도 : ', round(accuracy_score(nsmc_test_df['label'], test_predict), 3))
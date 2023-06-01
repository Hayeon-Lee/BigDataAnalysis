# BigDataAnalysis

## 🚩 레포지토리 설명

숭실대학교에서 최대선 교수님의 빅데이터분석 수업을 공부한 내용입니다.

**모든 jupyter notebook 내부 내용 중 과제를 제외한 내용의 저작권은 최대선 교수님입니다.**

## 📝 목차

1.  파이썬 리뷰

    - 정렬(sorted)
    - 기술 통계: 평균 구하기
    - 기술 통계: 도수 구하기
    - join: 타 파일에 있는 내용과 합쳐 분석하기
    - group by: 유형별로 묶어 분석하기

<br/>

2.  Numpy와 Pandas 활용

    - numpy로 만든 자료 기본 정보 출력하기
    - numpy 기본 연산
    - indexing, slicing
    - Pandas Dataframe 활용
    - 데이터프레임에서 iloc[], loc[], 값에 의한 참조 등 조건에 맞게 라벨링하기
    - 데이터프레임에서 column 연산하기
    - matplotlib 활용하기

<br/>

3.  크롤링과 웹페이지 스크레이핑

    - 네이버 API 활용하여 크롤링하기
    - 페이스북 API 활용하여 크롤링하기
    - beautifulsoup으로 정적 웹페이지 파싱하기

<br/>

4.  기술 통계

    - 변수의 종류와 titanic column 짝짓기
    - undersampling vs oversampling
    - 표본 추출(단순, 층화, oversampling)
    - numeric data 처리하기
      - 기술통계, 평균과 중간값
      - Quantile, IQR
      - boxplot
      - outlier
      - 시각화: boxplot, countplot, histplot
    - 결측치, 오류 데이터 처리, 카테고리 세팅
    - 통계적 추정
      - 신뢰구간 정하기: st.t.interval(), st.norm.interval()
      - 평균비교: st.ttest_1samp()
      - 도수비교: chisquare

    <br/>

5.  변수 간 분석

    - 2가지 변수 간 관계 분석
      - 교차 분석(nominal-nominal): crosstab, chi2_contingency
      - 평균 비교(nominal-numeric)
        - df.groupby(독립변수).종속변수.mean()
        - 통계적 유의성(독립적, paired, 3가지 이상의 종류인 독립변수)
      - 상관 분석(numeric-numeric)
        - titanic.corr()
        - sns.pairplot(), sns.heatmap()
        - 스피어만 상관계수
      - 회귀 분석(numeric-numeric)
        - 단순 선형회귀(m=ols('~'))
        - 중선형 회귀(m=ols('~'))
      - 모델과 예측

<br/>

6.  머신러닝

    - 집값 예측하기: 상관분석
    - 자동차연비예측: 회귀분석
    - 결과 개선
      - 다른 regression model(linear, ridge)
      - parameter tuning
      - feature selection
    - validation, test
    - cross validation: kfold

<br/>

7.  머신러닝 - 분류

    - 로지스틱 회귀
    - 전처리: Scaling, PCA
    - 결정트리
    - 분류 성능 지표
    - encoding

<br/>

9.  clustering

    - clustering 개념
    - k-means clustering
    - 최적의 k값 찾기
    - iris 데이터로 실습하기

<br/>

10. 주소를 이용한 빅데이터 분석

    - 주소를 지도에 출력하기 (geoCoding)
      - 정규식 이용하여 주소를 trimming 하기
      - 지도 시각화하기
    - 블록맵 만들기
      - 인구대비별 병상수 계산하여 블록맵 만들기

<br/>

12. 텍스트 프로세싱
    - 영어 텍스트 분석: 워드 클라우드 만들기
      - stopword와 lemmatize를 제외한 결과와 비교해보기
    - 한글 텍스트 분석: 형태소 분석
      - Okt()를 이용하여 한글 텍스트 분석하기
      - 동사와 명사 분류하기
      - 워드 클라우드 만들기
    - 특징 벡터화 (BOW)
      - monogram, bigram 각각의 성능 비교하기
      - 감성 분석하기


<br/>

13. NLP
    - 딥러닝
        - Iris 분류하기
        - hidden layer 를 추가하여 성능 비교하기
    - RNN 언어 모델
        - 네이버 영화평 분석하기
        - 분석한 내용을 토대로 특정 단어 다음에 올 단어 추정하기


<br/>

14. 가명처리
    - 범주화
    - 라운딩
    - 수치형 데이터 통계 및 시각화
    - 상하단 코딩

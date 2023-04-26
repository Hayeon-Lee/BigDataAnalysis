## 과제 1 : 1부터 30까지 숫자로 (5,3,2) 3차원을 만든 뒤, 각 숫자에 0과1 사이의 random noise  을 곱한 결과를 출력하시오
#- np.random.rand() : 0~1 사이 숫자 생성

arr = np.arange(1,31,1).reshape(5,3,2)
rn = np.random.rand(30).reshape(5,3,2)

arr = arr * rn
print(arr)
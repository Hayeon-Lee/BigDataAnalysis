## 과제 2 : np.arange(30).reshape((5,6)) 에서 0,2,4.. column (axis=1) 만 뽑아서 새로운 array를 만드시오
arr2 = np.arange(30).reshape((5,6))
new_arr2 = arr2[:, 0:5:2]
print(new_arr2)
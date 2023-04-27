#품종은 label encoding 해주고, 클러스터 라벨과 값을 비교하면 됨, 클러스터 n을 3으로 놓고 하자
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score

#clusterLabel이 기존 라벨
#best_ClusterLabel이 best label

#라벨 인코딩
le = LabelEncoder()
result = le.fit_transform(iris['species'])
iris['encoding_species'] = result

#best cluster 설정 후 새로운 칼럼 추가
display(iris)
iris_best_cluster=3
iris_best_kmeans = KMeans(n_clusters=iris_best_cluster, random_state=0)
iris_best_Y_labels = kmeans.fit_predict(iris_features)
iris['best_ClusterLabel'] = iris_best_Y_labels

#라벨 값 바꾸기
iris['best_ClusterLabel'] = iris['best_ClusterLabel'].replace(0,3)
iris['best_ClusterLabel'] = iris['best_ClusterLabel'].replace(1,0)
iris['best_ClusterLabel'] = iris['best_ClusterLabel'].replace(3,1)

print(confusion_matrix(iris['ClusterLabel'], iris['best_ClusterLabel']))
#원래 iris
#iris_Y_labels

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples
from sklearn.preprocessing import StandardScaler
import seaborn as sns 

iris = sns.load_dataset('iris')
iris_features = iris[['sepal_length', 'sepal_width','petal_length','petal_width']].values

iris_features_scaled = StandardScaler().fit_transform(iris_features)

iris_kmeans = KMeans(n_clusters=3, random_state=0)
iris_Y_labels = kmeans.fit_predict(iris_features_scaled)

iris['ClusterLabel'] = iris_Y_labels
iris.head()
print(iris['ClusterLabel'].unique())
'''
CLUSTER ANALYSIS
How do we implement a k-means clustering algorithm?

scikit-learn KMeans documentation for reference:
http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
'''

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import numpy as np

# Import iris data
iris = datasets.load_iris()
d = iris.data

# Run KMeans
est = KMeans(n_clusters=3, init='random')
est.fit(d)
y_kmeans = est.predict(d)

colors = np.array(['#FF0054','#FBD039','#23C2BC'])
plt.scatter(d[:, 2], d[:, 0], c=colors[y_kmeans], s=50)
plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[0])

# EXERCISE: Find the centers and plot them on the same graph.


'''
VISUALIZING THE CLUSTERS
What are some different options to visualize 
multi-dimensional data? Let's look at three ways you can do this.
- Scatter Plot Grid
- 3D Plot
- Parallel Coordinates
'''

#================================
# Option #1: Scatter Plot Grid
plt.figure(figsize=(8, 8))

# Upper Left
plt.subplot(221)
plt.scatter(d[:,2], d[:,0], c = colors[y_kmeans])
plt.ylabel(iris.feature_names[0])

# Upper Right
plt.subplot(222)
plt.scatter(d[:,3], d[:,0], c = colors[y_kmeans])

# Lower Left
plt.subplot(223)
plt.scatter(d[:,2], d[:,1], c = colors[y_kmeans])
plt.ylabel(iris.feature_names[1])
plt.xlabel(iris.feature_names[2])

# Lower Right
plt.subplot(224)
plt.scatter(d[:,3], d[:,1], c = colors[y_kmeans])
plt.xlabel(iris.feature_names[3])

#================================
# Option #2: 3d plot
from mpl_toolkits.mplot3d import Axes3D
ax = Axes3D(plt.figure(figsize=(10, 9)), rect=[.01, 0, 0.95, 1], elev=30, azim=134)
ax.scatter(d[:,0], d[:,1], d[:,2], c = colors[y_kmeans], s=120)
ax.set_xlabel('Sepal Width')
ax.set_ylabel('Sepal Width')
ax.set_zlabel('Petal Length')
# Modified from the example here: 
# http://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_iris.html

# EXERCISE: Create a Parallel Coordinates visualization

#================================
# Option 3: Parallel Coordinates

                     
'''
DETERMINING THE NUMBER OF CLUSTERS
How do you choose k? There isn't a bright line, but we can evaluate 
performance metrics such as the silhouette coefficient and within sum of 
squared errors across values of k.

scikit-learn Clustering metrics documentation:
http://scikit-learn.org/stable/modules/classes.html#clustering-metrics
'''

# Create a bunch of different models
k_rng = range(1,15)
est = [KMeans(n_clusters = k).fit(d) for k in k_rng]

#================================
# Option 1: Silhouette Coefficient
# Generally want SC to be closer to 1, while also minimizing k

from sklearn import metrics
silhouette_score = [metrics.silhouette_score(d, e.labels_, metric='euclidean') for e in est[1:]]

# Plot the results
plt.figure(figsize=(7, 8))
plt.subplot(211)
plt.title('Using the elbow method to inform k choice')
plt.plot(k_rng[1:], silhouette_score, 'b*-')
plt.xlim([1,20])
plt.grid(True)
plt.ylabel('Silhouette Coefficient')
plt.plot(3,silhouette_score[1], 'o', markersize=12, markeredgewidth=1.5,
         markerfacecolor='None', markeredgecolor='r')

# EXERCISE: Calculate the sum of squared errors and plot over a range of k

#================================
# Option 2: Within Sum of Squares (a.k.a., inertia)
# Generally want to minimize WSS, while also minimizing k
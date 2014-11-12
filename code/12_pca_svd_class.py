
import numpy as np
import matplotlib.pyplot as plt


# 1) Set up some data and look at it a little

x1 = np.random.normal(loc=40, scale=8, size=100)
x2 = x1 -10 + np.random.normal(scale=3, size=100)
plt.scatter(x1, x2)

X = np.column_stack((x1, x2))
X.shape

X.mean(axis=0)
X_centered = X - X.mean(axis=0)

np.cov(X, rowvar=0)
np.cov(X_centered, rowvar=0)
# same covariance matrix!


# 2) Do some PCA

eig_vals, Q = np.linalg.eig(np.cov(X_centered, rowvar=0)*99)
#get eigen values and eigen vectors

ordered = sorted(zip(eig_vals, Q.T), reverse=True) 
#order eigen values
eig_vals = np.array([_[0] for _ in ordered])
Q = np.column_stack((_[1] for _ in ordered))
#these lines of code re-order eig_vals and Q, nothing more

X_transformedPCA = np.dot(Q[:, 0].reshape(2, 1).T, X_centered.T).reshape(100, 1)
# eigen vector associated with largest eigen value times X

X_reconstituted = np.dot(X_transformedPCA, Q[:, 0].reshape(1, 2))

plt.scatter(X_centered[:, 0], X_centered[:, 1])
plt.scatter(X_reconstituted[:, 0], X_reconstituted[:, 1], c='r')


# 3) Do some SVD

U, singular_vals, V_T = np.linalg.svd(X_centered)
Sigma = np.zeros((100, 2))
Sigma[:2, :2] = np.diag(singular_vals)
np.dot(U, np.dot(Sigma, V_T))[:5, :]
X_centered[:5, :]

print singular_vals**2
print eig_vals

X_transformedSing = np.dot(U[:,0].reshape(100, 1), Sigma[0, 0])
X_reconstituted = np.dot(X_transformedSing, V_T[0, :].reshape(1, 2))

plt.scatter(X_centered[:, 0], X_centered[:, 1])
plt.scatter(X_reconstituted[:, 0], X_reconstituted[:, 1], c='r')


# sklearn

from sklearn.decomposition import PCA
pca = PCA(n_components=1)
pca.fit(X)
X_transformedSK = pca.transform(X)
print(pca.explained_variance_ratio_) 
X_reconstituted = pca.inverse_transform(X_transformedSK)

plt.scatter(X[:, 0], X[:, 1])
plt.scatter(X_reconstituted[:, 0], X_reconstituted[:, 1], c='r')

X_transformedPCA[:5:]
X_transformedSing[:5:]
X_transformedSK[:5:]

import sys
from csvreader import CsvReader
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

class KmeansClustering:
	def __init__(self, max_iter=20, ncentroid=5):
		self.ncentroid: int = ncentroid # number of centroids
		self.max_iter: int = max_iter # number of max iterations to update the centroids
		self.centroids = [] # values of the centroids

	def fit(self, X: np.ndarray):
		"""
		Run the K-means clustering algorithm.
		For the location of the initial centroids, random pick ncentroids from the dataset.
		Args:
		-----
			X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Return:
		-------
			None.
		Raises:
		-------
			This function should not raise any Exception.
		"""

		# Choose centroids
		self.centroids = X[np.random.choice(X.shape[0], self.ncentroid, replace=False), :]
		
		# Add column to X (will be used for distances)
		# D = np.zeros(X.shape[0])
		X = np.c_[np.zeros(X.shape[0]), X]

		# Kmean iteration
		for iter in range(self.max_iter):

			# Assign each point to its nearest centroid
			for p in X:
				p:np.ndarray
				for centroid in self.centroids:
					# L1 distance
					centroid[0] = abs(p[2] - centroid[1]) + abs(p[3] - centroid[2]) + abs(p[4] - centroid[3])
					# L2 distance
					# centroid[0] = np.sqrt((p[2] - centroid[1]) ** 2 + (p[3] - centroid[2]) ** 2 + (p[4] - centroid[3]) ** 2)
				mini = (0, self.centroids[0, 0])
				for i, v in enumerate(self.centroids[1:, 0]):
					if mini[1] > v:
						mini = (i + 1, v)
				p[0], p[1] = mini

			# print(X)
			# print(self.centroids)

			centroid_moved = False
			for i, c in enumerate(self.centroids):
				# print(X[(X[:, 0, None] == i).any(axis=1)])
				# Takes each element where index 0 equal i (all points from this cluster)
				# print(X[(X[:, 0, None] == i).any(axis=1)], '\n', c)
				print(c)
				points = X[(X[:, 0, None] == i).any(axis=1)]
				for j in range(3):
					new_value = points[:, j + 2].mean()
					if c[j + 1] != new_value:
						centroid_moved = True 
					c[j + 1] = new_value
				print(c)
			

			
			if not centroid_moved:
				print(f'Finished! Centroids moved {iter} times')
				break
		fig: Figure = plt.figure()
		ax: plt.Axes = fig.add_subplot(projection='3d')

		ax.scatter(*X[:, 2:].swapaxes(0, 1), c=X[:, 0])
		ax.scatter(*self.centroids[:, 1:].swapaxes(0, 1), s=100, c='r')
		plt.show()
		return self.centroids


	def predict(self, X):
		"""
		Predict from wich cluster each datapoint belongs to.
		Args:
		-----
			X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Return:
		-------
			the prediction has a numpy.ndarray, a vector of dimension m * 1.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		pass


def main(**kwargs):
	print(kwargs)
	if not kwargs.get('filepath'):
		print('Error: Missing filepath', file=sys.stderr)
		return 1
	
	with CsvReader(kwargs.get('filepath'), header=True) as file:
		datas: np.ndarray = np.array(file.getdata(), dtype=np.float64)
		# print(datas)
		km = KmeansClustering(int(kwargs.get('max_iter')), int(kwargs.get('ncentroid')))
		centroids = km.fit(datas)

if __name__ == "__main__":
	main(**dict(arg.split('=') for arg in sys.argv[1:]))

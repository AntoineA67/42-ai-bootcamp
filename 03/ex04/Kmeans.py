import sys
from csvreader import CsvReader
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

class KmeansClustering:

	# Dataset OFFSET if some columns should not be used
	OFFSET = 1

	def __init__(self, max_iter=20, ncentroid=5):
		self.ncentroid: int = ncentroid # number of centroids
		self.max_iter: int = max_iter # number of max iterations to update the centroids
		self.centroids: np.ndarray = np.zeros(1) # values of the centroids
		self.D: np.ndarray = np.zeros(1)
		self.is_standard = False

	def fit(self, X: np.ndarray, standardize=False):
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

		# Randomly choose centroids among points
		self.D = X.copy()
		if standardize:
			for i in range(self.D.shape[1] - KmeansClustering.OFFSET):
				self.D[:, i + KmeansClustering.OFFSET] = (self.D[:, i + KmeansClustering.OFFSET] - np.mean(self.D[:, i + KmeansClustering.OFFSET])) / np.std(self.D[:, i + KmeansClustering.OFFSET])
		self.centroids = self.D[np.random.choice(self.D.shape[0], self.ncentroid, replace=False), :]
		self.centroids = np.c_[np.zeros(self.centroids.shape[0]), self.centroids]
		
		# Add two columns to X (will be used for distances and clustering)
		self.D = np.c_[np.zeros(X.shape[0]), np.zeros(X.shape[0]), self.D]



		# K-means iterations
		for iter in range(self.max_iter):

			# Assign each point to its nearest centroid
			for p in self.D:
				p:np.ndarray
				for centroid in self.centroids:
					# L1 distance
					centroid[0] = sum([abs(p[i + KmeansClustering.OFFSET + 2] - centroid[i + 1 + KmeansClustering.OFFSET]) for i in range(self.D.shape[1] - KmeansClustering.OFFSET - 2)])
					# L2 distance
					# centroid[0] = np.sqrt(sum([(p[i + 2 + KmeansClustering.OFFSET] - centroid[i + 1 + KmeansClustering.OFFSET]) ** 2 for i in range(self.D.shape[1] - KmeansClustering.OFFSET - 2)]))
				mini = (0, self.centroids[0, 0])
				for i, v in enumerate(self.centroids[1:, 0]):
					if mini[1] > v:
						mini = (i + 1, v)
				p[0], p[1] = mini

			# Move centroids to average points positions
			centroid_moved = False
			for i, c in enumerate(self.centroids):
				# Takes each element where index 0 equal i (all points from this cluster)
				points = self.D[(self.D[:, 0, None] == i).any(axis=1)]
				for j in range(self.D.shape[1] - 2 - KmeansClustering.OFFSET):
					new_value = points[:, j + 2 + KmeansClustering.OFFSET].mean()
					if c[j + 1 + KmeansClustering.OFFSET] != new_value:
						centroid_moved = True 
					c[j + 1 + KmeansClustering.OFFSET] = new_value

			# Stop before iteration limit reached if no more iterations needed
			if not centroid_moved or iter == self.max_iter - 1:
				print(f'Finished! Centroids moved {iter + 1} times')
				break

		# Add number of data corresponding to each centroid
		data = np.c_[self.centroids[:, 2:], np.zeros(self.centroids.shape[0])]
		for i in range(data.shape[0]):
			data[i, -1] = self.D[(self.D[:, 0, None] == i).any(axis=1)].shape[0]

		print(f'Centroids (last field is the number of data corresponding to the centroid):\n{data}\n')
		return self.centroids

	def predict(self, X, standardize=False):
		"""
		Predict from wich cluster each datapoint belongs to.
		Args:
		-----
			X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Return:
		-------
			the prediction as a numpy.ndarray, a vector of dimension m * 1.
		Raises:
		-------
			This function should not raise any Exception.
		"""
		if len(self.D) == 1 or (not self.is_standard and standardize):
			self.fit(X, standardize=standardize)
		print(f'Predictions:\n{self.D[:, 0]}\n')
		return self.D[:, 0]

	def plot(self, X, standardize=False):
		if len(self.D) == 1 or (not self.is_standard and standardize):
			self.fit(X, standardize=standardize)

		fig: Figure = plt.figure()
		ax: plt.Axes = fig.add_subplot(projection='3d')

		# Plot in 3d the 3 firsts dimensions from clustered dataset
		ax.scatter(*self.D[:, 2 + KmeansClustering.OFFSET:5 + KmeansClustering.OFFSET].swapaxes(0, 1), c=self.D[:, 0])

		# Plot centroids in red and bigger size
		ax.scatter(*self.centroids[:, 1 + KmeansClustering.OFFSET: 4 + KmeansClustering.OFFSET].swapaxes(0, 1), s=100, c='r')
		plt.show()

	def getdata(self):
		return self.D


def main(**kwargs):
	if not kwargs.get('filepath'):
		print('Error: Missing filepath', file=sys.stderr)
		return 1
	
	with CsvReader(kwargs.get('filepath'), header=True) as file:
		if file is None:
			print(f'Error while opening the file "{kwargs.get("filepath")}"', file=sys.stderr)
			return 1
		standardize = False
		datas: np.ndarray = np.array(file.getdata(), dtype=np.float64)
		km = KmeansClustering(int(kwargs.get('max_iter')), int(kwargs.get('ncentroid')))
		centroids = km.fit(datas, standardize)
		km.predict(datas, standardize)

		if int(kwargs.get('ncentroid')) == 4 and kwargs.get('filepath') and kwargs.get('filepath').split('/')[-1] == 'solar_system_census.csv':
			centroids[:, 0] = np.arange(centroids.shape[0])
			predictions = [list(p) for p in centroids]

			# Sort predictions: Belt in first (highest height and lowest bone density) then venusians (lowest weight),
			# then martians(taller than on earth) and terrians (last data)
			predictions.sort(key=lambda x: x[2] -x[4] * 10, reverse=True)
			belt = predictions[0][1]
			predictions.sort(key=lambda x: (x[1] == belt, -x[3]), reverse=True)
			venus = predictions[1][1]
			predictions.sort(key=lambda x: (x[1] == belt, x[1] == venus, x[2]), reverse=True)
			for i, p in enumerate(predictions):
				p[1] = i
			
			print(f"""\t\t\tHeight\tWeight\tBone Density
Citizen of the Belt:\t{predictions[0][2]:6.2f}\t{predictions[0][3]:6.2f}\t{predictions[0][4]:6.2f}\t(highest height and lowest bone density)
Venusians:\t\t{predictions[1][2]:6.2f}\t{predictions[1][3]:6.2f}\t{predictions[1][4]:6.2f}\t(lowest weight)
Martians:\t\t{predictions[2][2]:6.2f}\t{predictions[2][3]:6.2f}\t{predictions[2][4]:6.2f}\t(taller than on earth)
Terrians:\t\t{predictions[3][2]:6.2f}\t{predictions[3][3]:6.2f}\t{predictions[3][4]:6.2f}\t""")

			# For colors a bit of extra calculation has to be done to match between datapoint, centroid index and the desired color
			colors = ['gray', 'orange', 'red', 'blue']
			d = km.getdata()
			c = [0] * len(predictions)
			for p in predictions:
				c[int(p[0])] = p[1]
			cc = []
			for p in d:
				cc.append(colors[c[int(p[0])]])

			b = mpatches.Patch(color=colors[int(predictions[0][1])], label='The Belt')
			v = mpatches.Patch(color=colors[int(predictions[1][1])], label='Venus')
			m = mpatches.Patch(color=colors[int(predictions[2][1])], label='Mars')
			e = mpatches.Patch(color=colors[int(predictions[3][1])], label='The Earth')
			fig, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3)
			fig.legend(handles=[b, v, m, e])
			ax0.scatter(d[:, 3], d[:, 4], c=cc)
			ax1.scatter(d[:, 3], d[:, 5], c=cc)
			ax2.scatter(d[:, 4], d[:, 5], c=cc)
			ax0.scatter(centroids[:, 2], centroids[:, 3], c='r', s=100)
			ax1.scatter(centroids[:, 2], centroids[:, 4], c='r', s=100)
			ax2.scatter(centroids[:, 3], centroids[:, 4], c='r', s=100)
			plt.show()
	
		km.plot(datas, standardize)

if __name__ == "__main__":
	main(**dict(arg.split('=') for arg in sys.argv[1:]))

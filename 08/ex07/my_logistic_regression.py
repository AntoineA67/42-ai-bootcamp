import numpy as np
from time import time

class MyLogisticRegression:
	"""
	Description:
	My personnal logistic regression to classify things.
	"""
	EPS = 1e-15

	def __init__(self, theta, alpha=0.001, max_iter=20000):
		self.alpha = alpha
		self.max_iter = max_iter
		self.theta = np.array(theta)
		if len(self.theta.shape) == 1:
			self.theta = self.theta[:, np.newaxis]

	def predict_(self, x: np.ndarray):
		"""Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
		Args:
			x: has to be an numpy.ndarray, a vector of dimension m * n.
			self.theta: has to be an numpy.ndarray, a vector of dimension (n + 1) * 1.
		Returns:
			y_hat as a numpy.ndarray, a vector of dimension m * 1.
			None if x or theta are empty numpy.ndarray.
			None if x or theta dimensions are not appropriate.
		Raises:
			This function should not raise any Exception.
		"""
		if type(x) != np.ndarray: return None

		X: np.ndarray = np.c_[np.ones(len(x)), x]

		return 1 / (1 + np.exp(-X.dot(self.theta)))

	def loss_elem(self, y: np.ndarray, y_hat: np.ndarray):
		if type(y) != type(y_hat) != np.ndarray or y.size == 0 or y_hat.size == 0: return None

		return y * np.log(y_hat + self.EPS) + (1 - y) * np.log(1 - y_hat + self.EPS)

	def _gradient(self, x: np.ndarray, y: np.ndarray):
		"""Computes a gradient vector from three non-empty numpy.ndarray, with a for-loop. The three arrays must have compatibl
		Args:
			x: has to be an numpy.ndarray, a matrix of shape m * n.
			y: has to be an numpy.ndarray, a vector of shape m * 1.
			self.theta: has to be an numpy.ndarray, a vector of shape (n + 1) * 1.
		Returns:
			The gradient as a numpy.ndarray, a vector of shape n * 1, containing the result of the formula for all j.
			None if x, y, or theta are empty numpy.ndarray.
			None if x, y and theta do not have compatible dimensions.
		Raises:
			This function should not raise any Exception.
		"""
		if type(y) != type(x) != np.ndarray or x.size == 0 or y.size == 0: return None

		X = np.c_[np.ones(len(x)), x]

		return (X.T.dot(self.predict_(x) - y)) / len(X)

	def loss_(self, y: np.ndarray, y_hat: np.ndarray):
		"""
		Computes the logistic loss value.
		Args:
			y: has to be an numpy.ndarray, a vector of shape m * 1.
			y_hat: has to be an numpy.ndarray, a vector of shape m * 1.
			eps: epsilon (default=1e-15)
		Returns:
			The logistic loss value as a float.
			None on any error.
		Raises:
			This function should not raise any Exception.
		"""
		elem: np.ndarray = self.loss_elem(y, y_hat)
		if elem is None: return None

		return -elem.mean()

	def fit_(self, x: np.ndarray, y: np.ndarray):
		"""
		Trains theta on x and y
		Args:
			x: has to be an numpy.ndarray, a vector of shape m * n.
			y: has to be an numpy.ndarray, a vector of shape m * 1.
		Returns:
			self.theta
		Raises:
			This function should not raise any Exception.
		"""
		for i in self._ft_progress(range(self.max_iter)):
			self.theta = self.theta - self.alpha * self._gradient(x, y)
		
		return self.theta
	
	@staticmethod
	def _ft_progress(lst):
		"""
		Displays a progress bar and yield each element from lst
		"""
		start = time()
		for i in lst:
			m, s, ms = int((time() - start) / 60), int(time() - start) % 60, int((time() - start) * 10)  % 10
			eta = (time() - start) * len(lst) / (i + 1) - (time() - start)
			print(f"\rFitting data: {(str(m) + 'm ' if m > 0 else '') + str(s).zfill(2) + ('.' + str(ms) if not m else '') + 's':^9} \
	{str(i + 1) + '/' + str(len(lst)):^10} \
	{'{'}{'=' + '=' * int(20 * (i + 1) / len(lst)) + ('>' if int(20 * (i + 1) / len(lst)) < 20 else ''):21}{'}'} \
	{'ETA: ' + (str(int(eta / 60)).zfill(2) + 'm' if int(eta / 60) > 0 else '') + str(int(eta % 60)).zfill(2) + 's' if i != len(lst) - 1 else 'Finished':^10} \
	{str(int(i / len(lst) * 100)) + '%' if i < len(lst) - 1 else '':^5}", end='\n' if i == len(lst) - 1 else '')
			yield i

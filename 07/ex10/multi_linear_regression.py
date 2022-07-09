import numpy as np
import matplotlib.pyplot as plt
from time import sleep, time

class MyLinearRegression:
	"""
		Description:
			My personnal linear regression class to fit like a boss.
	"""
	def __init__(self, theta, alpha=0.0001, max_iter=10000):
		self.alpha = alpha
		self.max_iter = max_iter
		self.theta = np.array(theta, dtype=np.float64)
		if self.theta.shape == (2, ):
			self.theta = self.theta.astype(dtype=np.float64)[:, np.newaxis]

	@staticmethod
	def _ft_progress(lst):
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

	@staticmethod
	def mse_elem_(y: np.ndarray, y_hat: np.ndarray):
		if type(y) != np.ndarray or type(y_hat) != np.ndarray or y.size == 0 or y_hat.size == 0: return None

		return np.power(y_hat - y, 2)

	@staticmethod
	def mse_(y: np.ndarray, y_hat: np.ndarray):
		"""
		Description:
			Calculate the MSE between the predicted output and the real output.
		Args:
			y: has to be a numpy.array, a vector of dimension m * 1.
			y_hat: has to be a numpy.array, a vector of dimension m * 1.
		Returns:
			mse: has to be a float.
			None if there is a matching dimension problem.
		Raises:
			This function should not raise any Exceptions.
		"""
		elem = MyLinearRegression.mse_elem_(y, y_hat)
		if elem is None:
			return None

		return elem.mean()

	@staticmethod
	def gradient_(x: np.ndarray, y: np.ndarray, theta: np.ndarray):
		"""Computes a gradient vector from three non-empty numpy.array, without any for-loop.
			The three arrays must have the compatible dimensions.
		Args:
			x: has to be an numpy.array, a matrix of dimension m * n.
			y: has to be an numpy.array, a vector of dimension m * 1.
			theta: has to be an numpy.array, a vector (n +1) * 1.
		Return:
			The gradient as a numpy.array, a vector of dimensions n * 1,
			containg the result of the formula for all j.
			None if x, y, or theta are empty numpy.array.
			None if x, y and theta do not have compatible dimensions.
			None if x, y or theta is not of expected type.
		Raises:
			This function should not raise any Exception.
		"""
		if type(x) != np.ndarray or type(theta) != np.ndarray or x.size == 0 or theta.size == 0 or x.shape[1] != theta.shape[0] - 1 or x.shape[0] != y.shape[0]:
			return None

		X: np.ndarray = np.c_[np.ones(x.shape[0]), x]

		# print(X, theta)

		return np.matmul(X.T / x.size, np.matmul(X, theta) - y)


	def fit_(self, x: np.ndarray, y: np.ndarray):
		"""
		Description:
			Fits the model to the training dataset contained in x and y.
		Args:
			x: has to be a numpy.array, a matrix of dimension m * n:
			(number of training examples, number of features).
			y: has to be a numpy.array, a vector of dimension m * 1:
			(number of training examples, 1).
			theta: has to be a numpy.array, a vector of dimension (n + 1) * 1:
			(number of features + 1, 1).
			alpha: has to be a float, the learning rate
			max_iter: has to be an int, the number of iterations done during the gradient descent
		Return:
			new_theta: numpy.array, a vector of dimension (number of features + 1, 1).
			None if there is a matching dimension problem.
			None if x, y, theta, alpha or max_iter is not of expected type.
		Raises:
			This function should not raise any Exception.
		"""
		if type(x) != np.ndarray or type(self.theta) != np.ndarray or x.size == 0 or self.theta.size == 0 or x.shape[1] != self.theta.shape[0] - 1 or x.shape[0] != y.shape[0]:
			return None

		new_theta = self.theta.copy()

		for _ in self._ft_progress(range(self.max_iter)):
			new_theta = new_theta - self.alpha * self.gradient_(x, y, new_theta)
		
		self.theta = new_theta
		return self
		# return new_theta

	def predict_(self, x: np.ndarray):
		"""Computes the prediction vector y_hat from two non-empty numpy.array.
		Args:
			x: has to be an numpy.array, a vector of dimensions m * n.
			theta: has to be an numpy.array, a vector of dimensions (n + 1) * 1.
		Return:
			y_hat as a numpy.array, a vector of dimensions m * 1.
			None if x or theta are empty numpy.array.
			None if x or theta dimensions are not appropriate.
			None if x or theta is not of expected type.
		Raises:
			This function should not raise any Exception.
		"""
		if type(x) != np.ndarray or type(self.theta) != np.ndarray or x.size == 0 or self.theta.size == 0 or x.shape[1] != self.theta.shape[0] - 1:
			return None

		return np.matmul(np.c_[np.ones(x.shape[0]), x], self.theta)

	@staticmethod
	def loss_elem_(y: np.ndarray, y_hat: np.ndarray) -> np.ndarray:
		"""
		Description:
			Calculates all the elements (y_pred - y)^2 of the loss function.
		Args:
			y: has to be an numpy.array, a vector.
			y_hat: has to be an numpy.array, a vector.
		Returns:
			J_elem: numpy.array, a vector of dimension (number of the training examples,1).
			None if there is a dimension matching problem between X, Y or theta.
			None if any argument is not of the expected type.
		Raises:
			This function should not raise any Exception.
		"""
		if type(y) != np.ndarray or type(y_hat) != np.ndarray or y.size == 0 or y_hat.size == 0: return None

		# if y.shape != y_hat.shape:
		# 	if len(y.shape) == 2:
		# 		return np.power(y_hat - y.swapaxes(0, 1), 2)
		# 	return np.power(y_hat.swapaxes(0, 1) - y, 2)
		return np.power(y_hat - y, 2)

	@staticmethod
	def loss_(y: np.ndarray, y_hat: np.ndarray):
		"""
		Description:
			Calculates the value of loss function.
		Args:
			y: has to be an numpy.array, a vector.
			y_hat: has to be an numpy.array, a vector.
		Returns:
			J_value : has to be a float.
			None if there is a dimension matching problem between X, Y or theta.
			None if any argument is not of the expected type.
		Raises:
			This function should not raise any Exception.
		"""
		elem = MyLinearRegression.loss_elem_(y, y_hat)
		if elem is None:
			return None

		return elem.mean() / 2

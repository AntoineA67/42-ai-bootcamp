import numpy as np
import matplotlib.pyplot as plt
from time import time

class MyLinearRegression:
	"""
		Description:
			My personnal linear regression class to fit like a boss.
	"""
	def __init__(self, thetas, alpha=0.001, max_iter=1000):
		self.alpha = alpha
		self.max_iter = max_iter
		self.thetas = np.array(thetas)
		if self.thetas.shape == (2, ):
			self.thetas = self.thetas.astype(dtype=np.float64)[:, np.newaxis]

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
		if type(y) != np.ndarray or type(y_hat) != np.ndarray: return None

		if y.shape != y_hat.shape:
			return np.power(y_hat - y.swapaxes(0, 1), 2)
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
		if type(y) != np.ndarray or type(y_hat) != np.ndarray: return None

		return MyLinearRegression.mse_elem_(y, y_hat).mean()

	def fit_(self, x: np.ndarray, y: np.ndarray):
		"""
		Description:
			Fits the model to the training dataset contained in x and y.
		Args:
			x: has to be a numpy.ndarray, a vector of dimension m * 1: (number of training examples, 1).
			y: has to be a numpy.ndarray, a vector of dimension m * 1: (number of training examples, 1).
			theta: has to be a numpy.ndarray, a vector of dimension 2 * 1.
			alpha: has to be a float, the learning rate
			max_iter: has to be an int, the number of iterations done during the gradient descent
		Returns:
			new_theta: numpy.ndarray, a vector of dimension 2 * 1.
			None if there is a matching dimension problem.
		Raises:
			This function should not raise any Exception.
		"""
		if type(x) != np.ndarray or type(y) != np.ndarray or type(self.thetas) != np.ndarray or type(self.alpha) != float or type(self.max_iter) != int or self.max_iter <= 0\
			or x.size == 0 or y.size == 0 or self.thetas.size != 2: return None

		X = np.c_[np.ones(len(x)), x]

		for _ in self._ft_progress(range(self.max_iter)):
			change = np.matmul(X.T / x.size, np.matmul(X, self.thetas) - y)
			self.thetas = self.thetas - (self.alpha * change)
		
		return self.thetas

	def predict_(self, x: np.ndarray):
		"""Computes the vector of prediction y_hat from two non-empty numpy.array.
		Args:
			x: has to be an numpy.array, a vector of dimension m * 1.
			theta: has to be an numpy.array, a vector of dimension 2 * 1.
		Returns:
			y_hat as a numpy.array, a vector of dimension m * 1.
			None if x and/or theta are not numpy.array.
			None if x or theta are empty numpy.array.
			None if x or theta dimensions are not appropriate.
		Raises:
			This function should not raise any Exceptions.
		"""
		if type(x) != np.ndarray or type(self.thetas) != np.ndarray: return None

		return np.matmul(np.c_[np.ones(x.shape[0]), x], self.thetas)

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
		if type(y) != np.ndarray or type(y_hat) != np.ndarray: return None

		if y.shape != y_hat.shape:
			if len(y.shape) == 2:
				return np.power(y_hat - y.swapaxes(0, 1), 2)
			return np.power(y_hat.swapaxes(0, 1) - y, 2)
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

	def plot_with_loss_(self, x: np.ndarray, y: np.ndarray, ax: plt.Axes = None):
		"""Plot the data and prediction line from three non-empty numpy.ndarray.
		Args:
			x: has to be an numpy.ndarray, a vector of dimension m * 1.
			y: has to be an numpy.ndarray, a vector of dimension m * 1.
			theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
		Returns:
			Nothing.
		Raises:
			This function should not raise any Exception.
		"""
		if type(x) != np.ndarray or type(y) != np.ndarray or type(self.thetas) != np.ndarray: return None

		if ax is None:
			_, ax1 = plt.subplots()
		else:
			ax1 = ax

		y_hat = self.predict_(x)
		if y_hat is None: return None

		ax1.scatter(x, y)
		ax1.plot(x, y_hat, c='orange')
		ax1.vlines(x, y, y_hat, linestyles='dashed')
		ax1.set_title(f'Cost: {self.loss_(y, y_hat)}')

		if not ax:
			plt.show()

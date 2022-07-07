import numpy as np

class MyLinearRegression():
	"""
		Description:
		My personnal linear regression class to fit like a boss.
	"""
	def __init__(self, thetas, alpha=0.001, max_iter=1000):
		self.alpha = alpha
		self.max_iter = max_iter
		self.thetas = np.array(thetas)[:, np.newaxis]
		
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
			or x.size == 0 or y.size == 0 or self.thetas.size == 0: return None

		self.thetas = self.thetas.astype(dtype=np.float64, copy=True).reshape((2, ))
		for _ in range(self.max_iter):
			self.thetas -= self.alpha * self.gradient(x, y, self.thetas)
		
		return self.thetas

	def gradient(self, x: np.ndarray, y: np.ndarray, theta: np.ndarray):
		"""Computes a gradient vector from three non-empty numpy.array, without any for loop.
			The three arrays must have compatible shapes.
		Args:
			x: has to be a numpy.array, a matrix of shape m * 1.
			y: has to be a numpy.array, a vector of shape m * 1.
			theta: has to be a numpy.array, a 2 * 1 vector.
		Return:
			The gradient as a numpy.ndarray, a vector of dimension 2 * 1.
			None if x, y, or theta is an empty numpy.ndarray.
			None if x, y and theta do not have compatible dimensions.
		Raises:
			This function should not raise any Exception.
		"""
		if type(x) != np.ndarray or type(y) != np.ndarray or type(theta) != np.ndarray\
			or x.size == 0 or y.size == 0 or theta.size == 0: return None
	
		X: np.ndarray = np.c_[np.ones(x.size), x]

		print(theta)
		theta = theta[:, np.newaxis]
		print(np.matmul(X.T / x.size, np.matmul(X, theta) - y))

		return np.matmul(X.T / x.size, np.matmul(X, theta) - y)

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
		if elem is None: return None
		return MyLinearRegression.loss_elem_(y, y_hat).mean() / 2
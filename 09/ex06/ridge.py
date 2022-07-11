import numpy as np
from multi_linear_regression import MyLinearRegression as MyLR

class MyRidge(MyLR):
	"""
	Description:
		My personnal ridge regression class to fit like a boss.
	"""
	def __init__(self, theta, alpha=0.001, max_iter=1000, lambda_=0.5):
		super().__init__(theta, alpha, max_iter)
		self.lambda_ = lambda_

	def loss_elem_(self, y: np.ndarray, y_hat: np.ndarray) -> np.ndarray:
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

		Y = y_hat - y
		theta2 = np.append([0], self.theta.flat[1:])

		return ((Y * Y).sum() + (self.lambda_ * theta2 * theta2).sum()) / y.size / 2

	def loss_(self, y: np.ndarray, y_hat: np.ndarray):
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
		Y = y_hat - y
		theta2 = np.append([0], self.theta.flat[1:])

		return ((Y * Y).sum() + (self.lambda_ * theta2 * theta2).sum()) / y.size / 2
		# elem = MyRidge.loss_elem_(y, y_hat)
		# if elem is None:
		# 	return None

		# return elem.mean() / 2

	def gradient_(self, x: np.ndarray, y: np.ndarray, theta: np.ndarray):
		"""Computes the regularized linear gradient of three non-empty numpy.ndarray,
			without any for-loop. The three arrays must have compatible shapes.
		Args:
			y: has to be a numpy.ndarray, a vector of shape m * 1.
			x: has to be a numpy.ndarray, a matrix of dimesion m * n.
			theta: has to be a numpy.ndarray, a vector of shape (n + 1) * 1.
			lambda_: has to be a float.
		Return:
			A numpy.ndarray, a vector of shape (n + 1) * 1, containing the results of the formula for all j.
			None if y, x, or theta are empty numpy.ndarray.
			None if y, x or theta does not share compatibles shapes.
			None if y, x or theta or lambda_ is not of the expected type.
		Raises:
			This function should not raise any Exception.
		"""
		if type(y) == type(x) != np.ndarray or not isinstance(self.lambda_, (int, float)) or y.size == 0 or x.size == 0:
			return None
		
		X: np.ndarray = np.c_[np.ones(len(x)), x]
		theta2: np.ndarray = np.append(0, theta[1:])

		# print(X)
		# print(y)
		# print(theta)

		return (X.T.dot((X.dot(theta) - y)) + (self.lambda_ * theta2)[:, np.newaxis]) / len(x)
	
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
		
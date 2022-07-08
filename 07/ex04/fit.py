import numpy as np
from gradient import gradient

def fit_(x: np.ndarray, y: np.ndarray, theta: np.ndarray, alpha: float = .0001, max_iter: int = 100000):
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
	if type(x) != np.ndarray or type(theta) != np.ndarray or x.size == 0 or theta.size == 0 or x.shape[1] != theta.shape[0] - 1 or x.shape[0] != y.shape[0]:
		return None

	new_theta = theta.astype(dtype=np.float64, copy=True)

	for _ in range(max_iter):
		new_theta = new_theta - alpha * gradient(x, y, new_theta)
	
	return new_theta

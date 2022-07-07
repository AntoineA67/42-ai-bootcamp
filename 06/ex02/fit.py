import numpy as np
from vec_gradient import gradient

def fit_(x: np.ndarray, y: np.ndarray, theta: np.ndarray, alpha: float, max_iter: int):
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
	if type(x) != np.ndarray or type(y) != np.ndarray or type(theta) != np.ndarray or type(alpha) != float or type(max_iter) != int or max_iter <= 0\
		or x.size == 0 or y.size == 0 or theta.size == 0: return None

	new_theta = theta.astype(dtype=np.float64, copy=True)
	for _ in range(max_iter):
		new_theta -= alpha * gradient(x, y, new_theta)
	
	return new_theta

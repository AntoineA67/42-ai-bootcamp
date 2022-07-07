import numpy as np

def simple_gradient(x: np.ndarray, y: np.ndarray, theta: np.ndarray):
	"""Computes a gradient vector from three non-empty numpy.array, without any for-loop.
		The three arrays must have compatible shapes.
	Args:
		x: has to be an numpy.array, a vector of shape m * 1.
		y: has to be an numpy.array, a vector of shape m * 1.
		theta: has to be an numpy.array, a 2 * 1 vector.
	Return:
		The gradient as a numpy.array, a vector of shape 2 * 1.
		None if x, y, or theta are empty numpy.array.
		None if x, y and theta do not have compatible shapes.
		None if x, y or theta is not of the expected type.
	Raises:
		This function should not raise any Exception.
	"""
	if type(x) != np.ndarray or type(y) != np.ndarray or type(theta) != np.ndarray\
		or x.size == 0 or y.size == 0 or theta.size == 0: return None

	y_hat = np.matmul(np.c_[np.ones(x.size), x], theta)

	return np.array([(y_hat - y).mean(), ((y_hat - y) * x).mean()])

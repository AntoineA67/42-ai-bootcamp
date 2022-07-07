import numpy as np

def gradient(x: np.ndarray, y: np.ndarray, theta: np.ndarray):
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

	return np.matmul(X.T / x.size, np.matmul(X, theta) - y)

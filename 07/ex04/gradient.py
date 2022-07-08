import numpy as np

def gradient(x: np.ndarray, y: np.ndarray, theta: np.ndarray):
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

	return (np.matmul(X.T / x.size, np.matmul(X, theta) - y))

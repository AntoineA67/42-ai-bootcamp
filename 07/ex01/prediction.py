import numpy as np

def predict_(x: np.ndarray, theta: np.ndarray):
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
	if type(x) != np.ndarray or type(theta) != np.ndarray or x.size == 0 or theta.size == 0 or x.shape[1] != theta.shape[0] - 1:
		return None

	return np.matmul(np.c_[np.ones(x.shape[0]), x], theta)

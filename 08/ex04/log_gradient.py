import numpy as np

def log_gradient(x: np.ndarray, y: np.ndarray, theta: np.ndarray):
	"""Computes a gradient vector from three non-empty numpy.ndarray, with a for-loop. The three arrays must have compatibl
	Args:
		x: has to be an numpy.ndarray, a matrix of shape m * n.
		y: has to be an numpy.ndarray, a vector of shape m * 1.
		theta: has to be an numpy.ndarray, a vector of shape (n + 1) * 1.
	Returns:
		The gradient as a numpy.ndarray, a vector of shape n * 1, containing the result of the formula for all j.
		None if x, y, or theta are empty numpy.ndarray.
		None if x, y and theta do not have compatible dimensions.
	Raises:
		This function should not raise any Exception.
	"""
	if type(x) != np.ndarray or type(y) != np.ndarray or type(theta) != np.ndarray\
		or x.size == 0 or y.size == 0 or theta.size == 0 or theta.size != x.shape[1] + 1: return None

	X: np.ndarray = np.c_[np.ones(len(x)), x]
	# corresponds to log_pred(x, theta)
	h_theta_X = 1 / (1 + np.exp(-X.dot(theta)))

	return (X.T.dot(h_theta_X - y)) / len(x)

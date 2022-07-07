import numpy as np

def simple_predict(x: np.ndarray, theta: np.ndarray):
	"""Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
	Args:
		x: has to be an numpy.ndarray, a vector of dimension m * 1.
		theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
	Returns:
		y_hat as a numpy.ndarray, a vector of dimension m * 1.
		None if x or theta are empty numpy.ndarray.
		None if x or theta dimensions are not appropriate.
	Raises:
		This function should not raise any Exception.
	"""
	if type(x) != np.ndarray or type(theta) != np.ndarray\
		or x.size == 0 or theta.size == 0 or (len(x.shape) != 1 and x.shape[1] != 1) or theta.size != 2: return None

	return np.array(theta[0] + theta[1] * x, dtype=np.float64)

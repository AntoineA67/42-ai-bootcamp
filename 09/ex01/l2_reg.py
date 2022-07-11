import numpy as np

def iterative_l2(theta: np.ndarray):
	"""Computes the L2 regularization of a non-empty numpy.ndarray, with a for-loop.
	Args:
		theta: has to be a numpy.ndarray, a vector of shape n * 1.
	Returns:
		The L2 regularization as a float.
		None if theta in an empty numpy.ndarray.
	Raises:
		This function should not raise any Exception.
	"""
	if type(theta) != np.ndarray or theta.size == 0: return None

	reg = 0

	for x in theta[1:].flat:
		reg += x * x

	return reg


def l2(theta: np.ndarray):
	"""Computes the L2 regularization of a non-empty numpy.ndarray, without any for-loop.
	Args:
		theta: has to be a numpy.ndarray, a vector of shape n * 1.
	Returns:
		The L2 regularization as a float.
		None if theta in an empty numpy.ndarray.
	Raises:
		This function should not raise any Exception.
	"""
	if type(theta) != np.ndarray or theta.size == 0: return None

	return np.power(theta.flat[1:], 2).sum()

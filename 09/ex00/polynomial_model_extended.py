import numpy as np

def add_polynomial_features(x: np.ndarray, power: int):
	"""Add polynomial features to matrix x by raising its columns to every power in the range of 1 up to the power give
	Args:
		x: has to be an numpy.ndarray, a matrix of shape m * n.
		power: has to be an int, the power up to which the columns of matrix x are going to be raised.
	Returns:
		The matrix of polynomial features as a numpy.ndarray, of shape m * (np), containg the polynomial feature va
		None if x is an empty numpy.ndarray.
	Raises:
		This function should not raise any Exception.
	"""
	if type(x) != np.ndarray or type(power) != int or x.size == 0 or power < 1: return None

	X = x.copy()
	for i in range(2, power + 1):
		X = np.c_[X, np.power(x, i)]

	return X

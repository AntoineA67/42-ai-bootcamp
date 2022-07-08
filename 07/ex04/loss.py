import numpy as np

def loss_(y: np.ndarray, y_hat: np.ndarray):
	"""Computes the mean squared error of two non-empty numpy.array, without any for loop.
		The two arrays must have the same dimensions.
	Args:
		y: has to be an numpy.array, a vector.
		y_hat: has to be an numpy.array, a vector.
	Return:
		The mean squared error of the two vectors as a float.
		None if y or y_hat are empty numpy.array.
		None if y and y_hat does not share the same dimensions.
		None if y or y_hat is not of expected type.
	Raises:
		This function should not raise any Exception.
	"""
	if type(y) != np.ndarray or type(y_hat) != np.ndarray or y.size == 0 or y_hat.size == 0 or y.shape != y_hat.shape:
		return None

	return ((y_hat - y) * (y_hat - y)).sum() / y.shape[0] / 2

import numpy as np

def add_polynomial_features(x: np.ndarray, power: int):
	"""Add polynomial features to vector x by raising its values up to the power given in argument.
	Args:
		x: has to be an numpy.array, a vector of dimension m * 1.
		power: has to be an int, the power up to which the components of vector x are going to be raised.
	Return:
		The matrix of polynomial features as a numpy.array, of dimension m * n,
		containing the polynomial feature values for all training examples.
		None if x is an empty numpy.array.
		None if x or power is not of expected type.
	Raises:
		This function should not raise any Exception.
	"""
	if type(x) != np.ndarray or type(power) != int: return None

	X = x.copy()
	for i in range(1, power):
		X = np.c_[X, np.power(x, i + 1)]
	
	return X

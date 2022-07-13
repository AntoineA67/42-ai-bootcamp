import numpy as np

def zscore(x: np.ndarray):
	"""Computes the normalized version of a non-empty numpy.ndarray using the z-score standardization.
	Args:
		x: has to be an numpy.ndarray, a vector.
	Returns:
		x’ as a numpy.ndarray.
		None if x is a non-empty numpy.ndarray or not a numpy.ndarray.
	Raises:
		This function shouldn’t raise any Exception.
	"""
	if type(x) != np.ndarray or x.size == 0: return None

	m = (x.sum() / x.size)
	std = np.sqrt((np.power(x - m, 2).sum()) / x.size)

	return (x - m) / std

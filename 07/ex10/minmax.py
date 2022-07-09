import numpy as np

def minmax(x: np.ndarray):
	"""Computes the normalized version of a non-empty numpy.ndarray using the min-max standardization.
	Args:
		x: has to be an numpy.ndarray, a vector.
	Returns:
		x’ as a numpy.ndarray.
		None if x is a non-empty numpy.ndarray or not a numpy.ndarray.
	Raises:
		This function shouldn’t raise any Exception.
	"""
	if type(x) != np.ndarray or x.size == 0: return None

	min, max = x.min(), x.max()
	max_minus_min = max - min
	return (x - min) / max_minus_min

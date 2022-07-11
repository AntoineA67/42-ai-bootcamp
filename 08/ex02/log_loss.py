import numpy as np

def log_loss_(y: np.ndarray, y_hat: np.ndarray, eps: float=1e-15):
	"""
	Computes the logistic loss value.
	Args:
		y: has to be an numpy.ndarray, a vector of shape m * 1.
		y_hat: has to be an numpy.ndarray, a vector of shape m * 1.
		eps: has to be a float, epsilon (default=1e-15)
	Returns:
		The logistic loss value as a float.
		None on any error.
	Raises:
		This function should not raise any Exception.
	"""
	if type(y) != np.ndarray or type(y_hat) != np.ndarray or eps == 0.0 or y.size == 0 or y_hat.size == 0: return None

	return -(y * np.log(y_hat + eps) + (1 - y) * np.log(1 - y_hat + eps)).mean()

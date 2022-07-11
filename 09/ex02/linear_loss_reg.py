import numpy as np

def reg_loss_(y: np.ndarray, y_hat: np.ndarray, theta: np.ndarray, lambda_: float):
	"""Computes the regularized loss of a linear regression model from two non-empty numpy.array, without any for loop.
	Args:
		y: has to be an numpy.ndarray, a vector of shape m * 1.
		y_hat: has to be an numpy.ndarray, a vector of shape m * 1.
		theta: has to be a numpy.ndarray, a vector of shape n * 1.
		lambda_: has to be a float.
	Returns:
		The regularized loss as a float.
		None if y, y_hat, or theta are empty numpy.ndarray.
		None if y and y_hat do not share the same shapes.
	Raises:
		This function should not raise any Exception.
	"""
	if type(y) == type(y_hat) == type(theta) != np.ndarray or type(lambda_) != float or y.size != y_hat.size or y.size == 0 or theta.size == 0:
		return None
	
	Y = y_hat - y
	theta2 = np.append([0], theta.flat[1:])

	return ((Y * Y).sum() + (lambda_ * theta2 * theta2).sum()) / y.size / 2

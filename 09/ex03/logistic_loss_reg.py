import numpy as np

def reg_log_loss_(y: np.ndarray, y_hat: np.ndarray, theta: np.ndarray, lambda_: float):
	"""Computes the regularized loss of a logistic regression model from two non-empty numpy.ndarray, without any for l
	Args:
		y: has to be an numpy.ndarray, a vector of shape m * 1.
		y_hat: has to be an numpy.ndarray, a vector of shape m * 1.
		theta: has to be a numpy.ndarray, a vector of shape n * 1.
		lambda_: has to be a float.
	Returns:
		The regularized loss as a float.
		None if y, y_hat, or theta is empty numpy.ndarray.
		None if y and y_hat do not share the same shapes.
	Raises:
		This function should not raise any Exception.
	"""
	if type(y) == type(y_hat) == type(theta) != np.ndarray or type(lambda_) != float or y.size != y_hat.size or y.size == theta.size == 0:
		return None

	theta2 = np.append([0], theta[1:])
	
	return -(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat)).sum() / y.size + lambda_ / (y.size * 2) * (theta2 * theta2).sum()

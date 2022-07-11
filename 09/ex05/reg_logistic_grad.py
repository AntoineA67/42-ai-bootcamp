import numpy as np

def reg_logistic_grad(y: np.ndarray, x: np.ndarray, theta: np.ndarray, lambda_: float):
	"""Computes the regularized logistic gradient of three non-empty numpy.ndarray, with two for-loops. The three array
	Args:
		y: has to be a numpy.ndarray, a vector of shape m * 1.
		x: has to be a numpy.ndarray, a matrix of dimesion m * n.
		theta: has to be a numpy.ndarray, a vector of shape n * 1.
		lambda_: has to be a float.
	Returns:
		A numpy.ndarray, a vector of shape n * 1, containing the results of the formula for all j.
		None if y, x, or theta are empty numpy.ndarray.
		None if y, x or theta does not share compatibles shapes.
	Raises:
		This function should not raise any Exception.
	"""
	if type(y) == type(x) == type(theta) != np.ndarray or not isinstance(lambda_, (int, float)) or y.size == 0 or x.size == 0:
		return None
	
	X: np.ndarray = np.c_[np.ones(len(x)), x]
	theta2: np.ndarray = np.append(0, theta[1:])

	return (X.T.dot((1 / (1 + np.exp(-X.dot(theta))) - y)) + (lambda_ * theta2)[:, np.newaxis]) / len(x)


def vec_reg_logistic_grad(y: np.ndarray, x: np.ndarray, theta: np.ndarray, lambda_: float):
	"""Computes the regularized logistic gradient of three non-empty numpy.ndarray, without any for-loop. The three arr
	Args:
	y: has to be a numpy.ndarray, a vector of shape m * 1.
	x: has to be a numpy.ndarray, a matrix of shape m * n.
	theta: has to be a numpy.ndarray, a vector of shape n * 1.
	lambda_: has to be a float.
	Returns:
	A numpy.ndarray, a vector of shape n * 1, containing the results of the formula for all j.
	None if y, x, or theta are empty numpy.ndarray.
	None if y, x or theta does not share compatibles shapes.
	Raises:
	This function should not raise any Exception.
	"""
	if type(y) == type(x) == type(theta) != np.ndarray or not isinstance(lambda_, (int, float)) or y.size == 0 or x.size == 0:
		return None
	
	X: np.ndarray = np.c_[np.ones(len(x)), x]
	theta2: np.ndarray = np.append(0, theta[1:])

	return (X.T.dot((1 / (1 + np.exp(-X.dot(theta))) - y)) + (lambda_ * theta2)[:, np.newaxis]) / len(x)
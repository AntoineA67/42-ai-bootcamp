import numpy as np

def reg_linear_grad(y: np.ndarray, x: np.ndarray, theta: np.ndarray, lambda_: float):
	"""Computes the regularized linear gradient of three non-empty numpy.ndarray,
		with two for-loop. The three arrays must have compatible shapes.
	Args:
		y: has to be a numpy.ndarray, a vector of shape m * 1.
		x: has to be a numpy.ndarray, a matrix of dimesion m * n.
		theta: has to be a numpy.ndarray, a vector of shape (n + 1) * 1.
		lambda_: has to be a float.
	Return:
		A numpy.ndarray, a vector of shape (n + 1) * 1, containing the results of the formula for all j.
		None if y, x, or theta are empty numpy.ndarray.
		None if y, x or theta does not share compatibles shapes.
		None if y, x or theta or lambda_ is not of the expected type.
	Raises:
		This function should not raise any Exception.
	"""
	if type(y) == type(x) == type(theta) != np.ndarray or not isinstance(lambda_, (int, float)) or y.size == 0 or x.size == 0:
		return None
	
	X: np.ndarray = np.c_[np.ones(len(x)), x]
	theta2: np.ndarray = np.append(0, theta[1:])

	return (X.T.dot((X.dot(theta) - y)) + (lambda_ * theta2)[:, np.newaxis]) / len(x)


def vec_reg_linear_grad(y: np.ndarray, x: np.ndarray, theta: np.ndarray, lambda_: float):
	"""Computes the regularized linear gradient of three non-empty numpy.ndarray,
		without any for-loop. The three arrays must have compatible shapes.
	Args:
		y: has to be a numpy.ndarray, a vector of shape m * 1.
		x: has to be a numpy.ndarray, a matrix of dimesion m * n.
		theta: has to be a numpy.ndarray, a vector of shape (n + 1) * 1.
		lambda_: has to be a float.
	Return:
		A numpy.ndarray, a vector of shape (n + 1) * 1, containing the results of the formula for all j.
		None if y, x, or theta are empty numpy.ndarray.
		None if y, x or theta does not share compatibles shapes.
		None if y, x or theta or lambda_ is not of the expected type.
	Raises:
		This function should not raise any Exception.
	"""
	if type(y) == type(x) == type(theta) != np.ndarray or not isinstance(lambda_, (int, float)) or y.size == 0 or x.size == 0:
		return None
	
	X: np.ndarray = np.c_[np.ones(len(x)), x]
	theta2: np.ndarray = np.append(0, theta[1:])

	return (X.T.dot((X.dot(theta) - y)) + (lambda_ * theta2)[:, np.newaxis]) / len(x)
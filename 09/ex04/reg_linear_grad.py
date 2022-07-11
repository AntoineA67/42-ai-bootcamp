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
	
	X = np.c_[np.ones(len(x)), x]
	J = np.array([(X.dot(theta) - y).mean()])

	for j in range(x.shape[1]):
		s = 0
		for i in range(len(x)):
			s += (theta[0] + (theta[1:] * x[i]).sum() - y[i]) * x[i][j] + float(lambda_ * theta[j])
		print(s)
		J = np.append(J, s / len(x))
	
	return J


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
	if type(y) == type(x) == type(theta) != np.ndarray or type(lambda_) != float or y.size != 0 or x.size != 0:
		return None
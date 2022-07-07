import numpy as np

def mse_elem_(y: np.ndarray, y_hat: np.ndarray):
	if type(y) != np.ndarray or type(y_hat) != np.ndarray: return None

	if y.shape != y_hat.shape:
		return np.power(y_hat - y.swapaxes(0, 1), 2)
	return np.power(y_hat - y, 2)

def mse_(y: np.ndarray, y_hat: np.ndarray):
	"""
	Description:
		Calculate the MSE between the predicted output and the real output.
	Args:
		y: has to be a numpy.array, a vector of dimension m * 1.
		y_hat: has to be a numpy.array, a vector of dimension m * 1.
	Returns:
		mse: has to be a float.
		None if there is a matching dimension problem.
	Raises:
		This function should not raise any Exceptions.
	"""
	if type(y) != np.ndarray or type(y_hat) != np.ndarray: return None

	return mse_elem_(y, y_hat).mean()

def rmse_elem_(y: np.ndarray, y_hat: np.ndarray):
	if type(y) != np.ndarray or type(y_hat) != np.ndarray: return None

	if y.shape != y_hat.shape:
		return y_hat - y.swapaxes(0, 1)
	return y_hat - y


def rmse_(y: np.ndarray, y_hat: np.ndarray):
	"""
	Description:
		Calculate the RMSE between the predicted output and the real output.
	Args:
		y: has to be a numpy.array, a vector of dimension m * 1.
		y_hat: has to be a numpy.array, a vector of dimension m * 1.
	Returns:
		rmse: has to be a float.
		None if there is a matching dimension problem.
	Raises:
		This function should not raise any Exceptions.
	"""
	if type(y) != np.ndarray or type(y_hat) != np.ndarray: return None

	return np.sqrt(mse_(y, y_hat))

def mae_elem_(y: np.ndarray, y_hat: np.ndarray):
	if type(y) != np.ndarray or type(y_hat) != np.ndarray: return None

	if y.shape != y_hat.shape:
		return np.abs(y_hat - y.swapaxes(0, 1))
	return np.abs(y_hat - y)

def mae_(y: np.ndarray, y_hat: np.ndarray):
	"""
	Description:
		Calculate the MAE between the predicted output and the real output.
	Args:
		y: has to be a numpy.array, a vector of dimension m * 1.
		y_hat: has to be a numpy.array, a vector of dimension m * 1.
	Returns:
		mae: has to be a float.
		None if there is a matching dimension problem.
	Raises:
		This function should not raise any Exceptions.
	"""
	if type(y) != np.ndarray or type(y_hat) != np.ndarray: return None

	return mae_elem_(y, y_hat).mean()

def r2score_elem(y: np.ndarray, y_hat: np.ndarray):
	if type(y) != np.ndarray or type(y_hat) != np.ndarray: return None

	m = y.mean()
	if y.shape != y_hat.shape:
		return np.true_divide(np.power(y_hat.swapaxes(0, 1) - y, 2), np.power(y - m, 2))
	return np.true_divide(np.power(y_hat - y, 2), np.power(y - m, 2))

def r2score_(y: np.ndarray, y_hat: np.ndarray):
	"""
	Description:
		Calculate the R2score between the predicted output and the output.
	Args:
		y: has to be a numpy.array, a vector of dimension m * 1.
		y_hat: has to be a numpy.array, a vector of dimension m * 1.
	Returns:
		r2score: has to be a float.
		None if there is a matching dimension problem.
	Raises:
		This function should not raise any Exceptions.
	"""
	if type(y) != np.ndarray or type(y_hat) != np.ndarray: return None

	if y.shape != y_hat.shape:
		return 1 - np.power(y_hat.swapaxes(0, 1) - y, 2).sum() / np.power(y - y.mean(), 2).sum()
	return 1 - np.power(y_hat - y, 2).sum() / np.power(y - y.mean(), 2).sum()

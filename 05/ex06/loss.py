import numpy as np

def loss_elem_(y: np.ndarray, y_hat: np.ndarray) -> np.ndarray:
	"""
	Description:
		Calculates all the elements (y_pred - y)^2 of the loss function.
	Args:
		y: has to be an numpy.array, a vector.
		y_hat: has to be an numpy.array, a vector.
	Returns:
		J_elem: numpy.array, a vector of dimension (number of the training examples,1).
		None if there is a dimension matching problem between X, Y or theta.
		None if any argument is not of the expected type.
	Raises:
		This function should not raise any Exception.
	"""
	if type(y) != np.ndarray or type(y_hat) != np.ndarray: return None

	if y.shape != y_hat.shape:
		return np.power(y_hat.swapaxes(0, 1) - y, 2)
	return np.power(y_hat - y, 2)

def loss_(y: np.ndarray, y_hat: np.ndarray):
	"""
	Description:
		Calculates the value of loss function.
	Args:
		y: has to be an numpy.array, a vector.
		y_hat: has to be an numpy.array, a vector.
	Returns:
		J_value : has to be a float.
		None if there is a dimension matching problem between X, Y or theta.
		None if any argument is not of the expected type.
	Raises:
		This function should not raise any Exception.
	"""
	elem = loss_elem_(y, y_hat)
	if elem is None: return None
	return loss_elem_(y, y_hat).mean() / 2

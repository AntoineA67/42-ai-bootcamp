import numpy as np

def accuracy_score_(y: np.ndarray, y_hat: np.ndarray):
	"""
	Compute the accuracy score.
	Args:
		y:a numpy.ndarray for the correct labels
		y_hat:a numpy.ndarray for the predicted labels
	Returns:
		The accuracy score as a float.
		None on any error.
	Raises:
		This function should not raise any Exception.
	"""
	if type(y) == type(y_hat) != np.ndarray or y.size == y_hat.size == 0: return None

	return np.array([1 if y[i] == y_hat[i] else 0 for i in range(y.size)]).sum() / y.size


def precision_score_(y: np.ndarray, y_hat: np.ndarray, pos_label=1):
	"""
	Compute the precision score.
	Args:
		y:a numpy.ndarray for the correct labels
		y_hat:a numpy.ndarray for the predicted labels
		pos_label: str or int, the class on which to report the precision_score (default=1)
	Returns:
		The precision score as a float.
		None on any error.
	Raises:
		This function should not raise any Exception.
	"""
	if type(y) == type(y_hat) != np.ndarray or y.size == y_hat.size == 0 or not isinstance(pos_label, (int, str)): return None

	tp = np.array([1 if (y_hat[i] == pos_label and y_hat[i] == y[i]) else 0 for i in range(y.size)]).sum()
	fp = np.array([1 if (y_hat[i] == pos_label and y_hat[i] != y[i]) else 0 for i in range(y.size)]).sum()

	return  tp / (tp + fp)


def recall_score_(y: np.ndarray, y_hat: np.ndarray, pos_label=1):
	"""
	Compute the recall score.
	Args:
		y:a numpy.ndarray for the correct labels
		y_hat:a numpy.ndarray for the predicted labels
		pos_label: str or int, the class on which to report the precision_score (default=1)
	Returns:
		The recall score as a float.
		None on any error.
	Raises:
		This function should not raise any Exception.
	"""
	if type(y) == type(y_hat) != np.ndarray or y.size == y_hat.size == 0 or not isinstance(pos_label, (int, str)): return None

	tp = np.array([1 if (y_hat[i] == pos_label and y_hat[i] == y[i]) else 0 for i in range(y.size)]).sum()
	fn = np.array([1 if (y_hat[i] != pos_label and y_hat[i] != y[i]) else 0 for i in range(y.size)]).sum()

	return  tp / (tp + fn)


def f1_score_(y: np.ndarray, y_hat: np.ndarray, pos_label=1):
	"""
	Compute the f1 score.
	Args:
		y:a numpy.ndarray for the correct labels
		y_hat:a numpy.ndarray for the predicted labels
		pos_label: str or int, the class on which to report the precision_score (default=1)
	Returns:
		The f1 score as a float.
		None on any error.
	Raises:
		This function should not raise any Exception.
	"""
	if type(y) == type(y_hat) != np.ndarray or y.size == y_hat.size == 0 or not isinstance(pos_label, (int, str)): return None

	p, r = precision_score_(y, y_hat, pos_label), recall_score_(y, y_hat, pos_label)

	return 2 * p * r / (p + r)

import numpy as np
import pandas as pd

def confusion_matrix_(y_true: np.ndarray, y_hat: np.ndarray, labels: list=None, df_option: bool=False):
	"""
	Compute confusion matrix to evaluate the accuracy of a classification.
	Args:
		y_true: a numpy.ndarray for the correct labels
		y_hat: a numpy.ndarray for the predicted labels
		labels: optional, a list of labels to index the matrix. This may be used to reorder or select a subset of labels. (
		df_option: optional, if set to True the function will return a pandas DataFrame instead of a numpy array. (default=
	Returns:
		Confusion matrix as a numpy ndarray or a pandas DataFrame according to df_option value.
		None on any error.
	Raises:
		This function should not raise any Exception.
	"""
	if type(y_hat) != np.ndarray or type(y_true) != np.ndarray or y_hat.size != y_true.size or y_true.size == 0: return None

	if labels:
		dct = {v: i for i, v in enumerate(labels)}
	else:
		uniques = np.unique(np.append(y_hat, y_true))
		dct = {v: i for i, v in enumerate(uniques)}

	matrix = np.zeros((len(dct), len(dct)), dtype=int)
	y_hat_flat = y_hat.flatten()
	y_true_flat = y_true.flatten()

	for i in range(y_hat_flat.size):
		if dct.get(y_true_flat[i]) is not None and dct.get(y_hat_flat[i]) is not None:
			matrix[dct[y_true_flat[i]]][dct[y_hat_flat[i]]] += 1
	
	if df_option:
		return pd.DataFrame(matrix, dct.keys(), dct.keys())

	return matrix

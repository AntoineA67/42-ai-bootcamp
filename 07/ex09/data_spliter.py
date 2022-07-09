import numpy as np

def data_spliter(x: np.ndarray, y: np.ndarray, proportion: float):
	"""Shuffles and splits the dataset (given by x and y) into a training and a test set,
		while respecting the given proportion of examples to be kept in the training set.
	Args:
		x: has to be an numpy.array, a matrix of dimension m * n.
		y: has to be an numpy.array, a vector of dimension m * 1.
		proportion: has to be a float, the proportion of the dataset that will be assigned to the
		training set.
	Return:
		(x_train, x_test, y_train, y_test) as a tuple of numpy.array
		None if x or y is an empty numpy.array.
		None if x and y do not share compatible dimensions.
		None if x, y or proportion is not of expected type.
	Raises:
		This function should not raise any Exception.
	"""
	if type(x) != np.ndarray or type(y) != np.ndarray or type(proportion) != float or x.size == 0 or y.size == 0 or x.shape[0] != y.shape[0] or proportion > 1. or proportion < 0. : return None

	concat = np.c_[x, y]
	np.random.shuffle(concat)
	p = int(proportion * len(x))

	return (concat[:p, :-1], concat[p:, :-1], concat[:p, -1][:, np.newaxis], concat[p:, -1][:, np.newaxis])


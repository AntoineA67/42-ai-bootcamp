import matplotlib.pyplot as plt
import numpy as np
from prediction import predict_

def plot(x: np.ndarray, y: np.ndarray, theta: np.ndarray):
	"""Plot the data and prediction line from three non-empty numpy.array.
	Args:
		x: has to be an numpy.array, a vector of dimension m * 1.
		y: has to be an numpy.array, a vector of dimension m * 1.
		theta: has to be an numpy.array, a vector of dimension 2 * 1.
	Returns:
		Nothing.
	Raises:
		This function should not raise any Exceptions.
	"""
	if type(x) != np.ndarray or type(theta) != np.ndarray or type(y) != np.ndarray\
		or x.size == 0 or theta.size == 0 or y.size == 0\
		or (len(x.shape) != 1 and x.shape[1] != 1) or (len(y.shape) != 1 and y.shape[1] != 1)\
		or theta.size != 2: return None

	plt.scatter(x, y)
	plt.plot(x, predict_(x, theta=theta), c='orange')
	plt.show()

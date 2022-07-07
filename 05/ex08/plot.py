import numpy as np
import matplotlib.pyplot as plt
from vec_loss import loss_
from prediction import predict_

def plot_with_loss(x: np.ndarray, y: np.ndarray, theta: np.ndarray):
	"""Plot the data and prediction line from three non-empty numpy.ndarray.
	Args:
	x: has to be an numpy.ndarray, a vector of dimension m * 1.
	y: has to be an numpy.ndarray, a vector of dimension m * 1.
	theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
	Returns:
	Nothing.
	Raises:
	This function should not raise any Exception.
	"""
	if type(x) != np.ndarray or type(y) != np.ndarray or type(theta) != np.ndarray: return None

	y_hat = predict_(x, theta)
	if y_hat is None: return None

	_, ax = plt.subplots()
	ax.scatter(x, y)
	ax.plot(x, y_hat, c='orange')
	ax.vlines(x, y, y_hat, linestyles='dashed')
	ax.set_title(f'Cost: {loss_(y, y_hat) * 2}')

	plt.show()

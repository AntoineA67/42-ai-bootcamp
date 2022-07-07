import numpy as np
import matplotlib.pyplot as plt
from prediction import predict_
from other_losses import mse_

def plot_with_loss(x: np.ndarray, y: np.ndarray, theta: np.ndarray, ax: plt.Axes = None):
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

	if ax is None:
		_, ax1 = plt.subplots()
	else:
		ax1 = ax

	y_hat = predict_(x, theta)
	if y_hat is None: return None

	ax1.scatter(x, y)
	ax1.plot(x, y_hat, c='orange')
	ax1.vlines(x, y, y_hat, linestyles='dashed')
	loss = mse_(y, y_hat)
	ax1.set_title(f'Cost: {loss * 2}')

	if not ax:
		plt.show()

import numpy as np
from fit import fit_
from prediction import predict_
from plot import plot_with_loss
import matplotlib.pyplot as plt
from other_losses import mse_

def main():
	x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
	y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
	theta= np.array([1, 1]).reshape((-1, 1))

	y_hat = predict_(x, theta)
	print(f'Theta\n{theta}\n\nPrediction:\n{y_hat}\n\nCost: {mse_(y, y_hat)}\n\n\n')

	theta1 = fit_(x, y, theta, alpha=5e-4, max_iter=100000)

	y_hat1 = predict_(x, theta1)
	print(f'Theta1\n{theta1}\n\nPrediction1:\n{y_hat1}\n\nCost: {mse_(y, y_hat1)}')

	_, ax = plt.subplots(ncols=2)
	plot_with_loss(x, y, theta1, ax[1])
	plot_with_loss(x, y, theta, ax[0])

	plt.show()

if __name__ == '__main__':
	main()

import numpy as np
from multi_linear_regression import MyLinearRegression as MultiLinearRegression
import pandas as pd
import matplotlib.pyplot as plt

def model(data: pd.DataFrame):

	np.set_printoptions(precision=2, threshold=np.inf, linewidth=np.inf)

	# Extracted data
	X1 = np.array(data['Age'])[:, np.newaxis]
	X2 = np.array(data['Thrust_power'])[:, np.newaxis]
	X3 = np.array(data['Terameters'])[:, np.newaxis]

	# Full data for multivariate fitting
	X = np.array(data)[:, :3]

	Y = np.array(data['Sell_price'])[:, np.newaxis]

	theta = np.arange(2)[:, np.newaxis]
	ln1, ln2, ln3, ln4 = MultiLinearRegression(theta, 5e-4, 50000), MultiLinearRegression(theta, 5e-5, 50000), MultiLinearRegression(theta, 5e-5, 50000), MultiLinearRegression(np.arange(4)[:, np.newaxis], 5e-5, 50000)
	print(f'Losses before fitting:\t{ln1.loss_(Y, ln1.predict_(X1)):.3f}\t{ln2.loss_(Y, ln2.predict_(X2)):.3f}\t{ln3.loss_(Y, ln3.predict_(X3)):.3f}\t{ln4.loss_(Y, ln4.predict_(X)):.3f}')
	theta1, theta2, theta3, theta4 = ln1.fit_(X1, Y).reshape(2), ln2.fit_(X2, Y).reshape(2), ln3.fit_(X3, Y).reshape(2), ln4.fit_(X, Y).reshape(4)

	losses = [ln1.loss_(Y, ln1.predict_(X1)), ln2.loss_(Y, ln2.predict_(X2)), ln3.loss_(Y, ln3.predict_(X3)), ln4.loss_(Y, ln4.predict_(X))]
	ln5 = MultiLinearRegression([theta1[0], theta1[1], theta2[1], theta3[1]], 5e-4, 50000)
	print(f"""Thetas after fitting:{theta1}\t{theta2}\t{theta3}\t{theta4}
MSE after fitting:\t{ln1.mse_(Y, ln1.predict_(X1)):.3f}\t{ln1.mse_(Y, ln2.predict_(X2)):.3f}\t{ln1.mse_(Y, ln3.predict_(X3)):.3f}\t{ln1.mse_(Y, ln4.predict_(X)):.3f}
Losses after fitting:\t{losses[0]:.3f}\t{losses[1]:.3f}\t{losses[2]:.3f}\t{losses[3]:.3f}
Combined univariate losses:\t{ln5.loss_(Y, ln5.predict_(X)):.3f}
Multivariate loss:\t\t{losses[3]:.3f}""")

	# Prediction data

	#	fit one by one
	Y1, Y2, Y3 = ln1.predict_(X1), ln2.predict_(X2), ln3.predict_(X3)

	#	fit all three features at the same time
	Y4 = ln4.predict_(X)
	
	_, ax = plt.subplots(ncols=3, nrows=2)

	ax[0][0].scatter(X1, Y, label='Sell price', c='midnightblue')
	ax[0][0].scatter(X1, Y1, label='Predicted sell price', c='cornflowerblue')

	ax[0][1].scatter(X2, Y, label='Sell price', c='darkgreen')
	ax[0][1].scatter(X2, Y2, label='Predicted sell price', c='mediumseagreen')

	ax[0][2].scatter(X3, Y, label='Sell price', c='darkmagenta')
	ax[0][2].scatter(X3, Y3, label='Predicted sell price', c='violet')

	ax[1][0].scatter(X1, Y, label='Sell price', c='midnightblue')
	ax[1][0].scatter(X1, Y4, label='Predicted sell price', c='cornflowerblue')

	ax[1][1].scatter(X2, Y, label='Sell price', c='darkgreen')
	ax[1][1].scatter(X2, Y4, label='Predicted sell price', c='mediumseagreen')

	ax[1][2].scatter(X3, Y, label='Sell price', c='darkmagenta')
	ax[1][2].scatter(X3, Y4, label='Predicted sell price', c='violet')

	for j in range(2):
		for i in range(3):
			ax[j][i].set_xlabel(f"x{i}: {['Age (in years)', 'Thrust power (in 10Km/s)', 'Terameters (in terameters)'][i]}")
			ax[j][i].set_ylabel(f"y: sell price (in keuros)")
			ax[j][i].grid()
			ax[j][i].legend()


	plt.show()
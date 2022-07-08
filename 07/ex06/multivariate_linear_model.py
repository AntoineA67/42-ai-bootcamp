import numpy as np
from multi_linear_regression import MyLinearRegression as MultiLinearRegression
from uni_linear_regression import MyLinearRegression as UniLinearRegression
import pandas as pd
import matplotlib.pyplot as plt

def model(data: pd.DataFrame):
	# Extracted data
	X1 = np.array(data['Age'])[:, np.newaxis]
	X2 = np.array(data['Thrust_power'])[:, np.newaxis]
	X3 = np.array(data['Terameters'])[:, np.newaxis]

	Y = np.array(data['Sell_price'])[:, np.newaxis]

	theta = np.arange(2)[:, np.newaxis]
	print(X1, Y, theta)
	ln = MultiLinearRegression(theta, 5e-4, 200000)

	print(ln.theta)
	theta1 = ln.fit_(X1, Y)

	# Prediction data
	Y1 = ln.predict_(X1)
	print(theta1)
	
	_, ax = plt.subplots(ncols=3)

	for i in range(len(ax)):
		ax[i].grid()

	ax[0].plot(X1, Y1)
	ax[0].scatter(X1, Y)
	# ax[0].scatter(Y1, Y)
	plt.show()
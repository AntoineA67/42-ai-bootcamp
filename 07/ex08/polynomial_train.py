import pandas as pd
import numpy as np
from polynomial_model import add_polynomial_features
from multi_linear_regression import MyLinearRegression as MyLR
import matplotlib.pyplot as plt

def polynomial_train():
	data = pd.read_csv('../resources/are_blue_pills_magics.csv')

	theta1, theta2, theta3 = np.array(np.ones(2)).reshape(-1,1), np.array(np.ones(3)).reshape(-1,1), np.array(np.ones(4)).reshape(-1,1)
	theta2 = np.array([[17],[22],[ -3]]).reshape(-1,1)
	theta3 = np.array([[1],[4],[5], [0]]).reshape(-1,1)
	theta4 = np.array([[6],[ 7],[ -1],[ 1],[ -1]]).reshape(-1,1)
	theta5 = np.array([[1140],[ -1850],[ 1110],[ -305],[ 40],[ -2]]).reshape(-1,1)
	theta6 = np.array([[9110],[ -18015],[ 13400],[ -4935],[ 966],[ -96.4],[ 3.86]]).reshape(-1,1)

	thetas = [theta1, theta2, theta3, theta4, theta5, theta6]
	x, X, y = np.array(data['Micrograms'])[:, np.newaxis], add_polynomial_features(np.array(data['Micrograms'])[:, np.newaxis], 6), np.array(data['Score'])[:, np.newaxis]

	_, ax = plt.subplots(ncols=2)

	continuous_x = np.arange(1,7.01, 0.01).reshape(-1,1)
	x_ = add_polynomial_features(continuous_x, 6)

	mses = []

	for i in range(6):
		lr = MyLR(thetas[i], np.power(10., (-i - 4.)), np.power(10, 5))
		lr.fit_(X[:, :i + 1], y)
		predict = lr.predict_(x_[:, :i + 1])
		# print(predict)
		print(f'MSE degree {i + 1}: {lr.mse_(y, lr.predict_(X[:, :i + 1]))}\n\n')
		mses.append((i, lr.mse_(y, lr.predict_(X[:, :i + 1]))))
		ax[1].bar(i, lr.mse_(y, lr.predict_(X[:, :i + 1])), label=f'Degree {i + 1}')
		ax[0].plot(continuous_x, predict, label=f'Degree {i + 1}')
	
	plt.legend()

	mses = np.array(mses)

	# ax[1].bar(mses[:, 0], mses[:, 1])
	ax[0].scatter(x, y)

	plt.show()


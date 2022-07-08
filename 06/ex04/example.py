from my_linear_regression import MyLinearRegression as MyLR
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error

def main():
	data = pd.read_csv("../resources/are_blue_pills_magics.csv")
	Xpill = np.array(data['Micrograms']).reshape(-1,1)
	Yscore = np.array(data['Score']).reshape(-1,1)
	linear_model1 = MyLR(np.array([[89.0], [-8]]), 5e-5, 50000)
	linear_model2 = MyLR(np.array([[89.0], [-6]]))
	Y_model1 = linear_model1.predict_(Xpill)
	Y_model2 = linear_model2.predict_(Xpill)
	print(MyLR.mse_(Yscore, Y_model1))
	# 57.60304285714282
	print(mean_squared_error(Yscore, Y_model1))
	# 57.603042857142825
	print(MyLR.mse_(Yscore, Y_model2))
	# 232.16344285714285
	print(mean_squared_error(Yscore, Y_model2))
	# 232.16344285714285

	# Perform linear regression
	linear_model1.fit_(Xpill, Yscore)
	fitted_prediction = linear_model1.predict_(Xpill)
	print(f'Found new thetas!:\n{linear_model1.thetas}\nnew cost: {linear_model1.loss_(Yscore, fitted_prediction)}')

	_, ax = plt.subplots(ncols=2)
	linear_model1.plot_with_loss_(Xpill, Yscore, ax[0])

	# First subplot
	ax[0].set_ylabel('Space driving score')
	ax[0].set_xlabel('Quantity of blue pill (in micrograms)')
	ax[0].scatter(Xpill, fitted_prediction)
	ax[0].grid()
	ax[0].legend(['Strue(pills)', 'Prediction line', 'Loss', 'Spredict(pills)'])

	# Second subplot
	ax[1].set_ylabel('cost function J(θ0, θ1)')
	ax[1].set_xlabel('θ1')
	ax[1].grid()
	t = np.arange(linear_model1.thetas[1] - 2, linear_model1.thetas[1] + 2, 0.1)
	thetas0 = np.arange(linear_model1.thetas[0] - 3, linear_model1.thetas[0] + 3, 1)
	t_loss = np.array([[MyLR.loss_(Yscore, MyLR([i, x]).predict_(Xpill)) for x in t] for i in thetas0])

	# print(t_loss)
	for i, theta0 in enumerate(t_loss):
		ax[1].plot(t, theta0, label=f'J(θ0={thetas0[i]:.2f}, θ1)')
	ax[1].legend()


	plt.show()

if __name__ == '__main__':
	main()

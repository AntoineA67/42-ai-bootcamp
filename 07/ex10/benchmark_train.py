import numpy as np
import pandas as pd
from multi_linear_regression import MyLinearRegression as MyLR
from z_score import zscore
from minmax import minmax
from data_spliter import data_spliter
import matplotlib.pyplot as plt

def main():
	# Load data
	data = pd.read_csv('../resources/space_avocado.csv')
	# Choose normalization function
	std_f = zscore

	# Define X, Y and normalize them
	X, Y = np.array(data)[:, 1:4], np.array(data['target']).reshape(-1, 1)
	X = np.c_[std_f(X[:, 0]), std_f(X[:, 1]), std_f(X[:, 2])]
	Y = std_f(Y)

	# Split data in train set and test set
	X_train, X_test, Y_train, Y_test = data_spliter(X, Y, .2)

	# Generate random thetas and initialize linear regression class
	lr = MyLR(np.random.rand(4, 1), 0.01, 20000)

	# Train model on train set and set prediction data on train set and on test set
	lr.fit_(X_train, Y_train)
	Y_hat_train, Y_hat_test = lr.predict_(X_train), lr.predict_(X_test)

	# Init plot figure and axes
	fig, ax = plt.subplots(ncols=3, nrows=2)
	labels = ['Weight', 'Prod distance', 'Time delivery']

	# Plot data
	for i in range(3):
		# Scatter true values in blue
		ax[0][i].scatter(X_test[:, i], Y_test, c='blue', alpha=.5, label='True values')
		ax[1][i].scatter(X_train[:, i], Y_train, c='blue', alpha=.5, label='True values values')

		# Scatter prediction values
		ax[0][i].scatter(X_test[:, i], Y_hat_test, c='violet', alpha=.5, label='Prediction values')
		ax[1][i].scatter(X_train[:, i], Y_hat_train, c='violet', alpha=.5, label='Prediction values')

		# Add labels
		ax[0][i].set_xlabel(labels[i])
		ax[1][i].set_xlabel(labels[i])
		ax[0][i].set_ylabel('Target(price)')
		ax[1][i].set_ylabel('Target(price)')
		ax[0][i].legend()
		ax[1][i].legend()

	# Add titles
	fig.suptitle('Train set')
	fig.supxlabel('Test set')

	# Print score over train set and test set
	print(f'Degree 1:\nMSE train: {lr.mse_(Y_train, Y_hat_train)}\nMSE test: {lr.mse_(Y_test, Y_hat_test)}\n\n')

	plt.show()


if __name__ == '__main__':
	main()

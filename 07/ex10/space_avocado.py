import numpy as np
import pandas as pd
from multi_linear_regression import MyLinearRegression as MyLR
from z_score import zscore
from minmax import minmax
from polynomial_model import add_polynomial_features
from data_spliter import data_spliter
import matplotlib.pyplot as plt

def main():
	# Load data
	data = pd.read_csv('../resources/space_avocado.csv')

	# Choose normalization function
	NORM_F = zscore

	# Define X, Y and normalize them
	X, Y = np.array(data)[:, 1:4], np.array(data['target']).reshape(-1, 1)
	X = np.c_[NORM_F(X[:, 0]), NORM_F(X[:, 1]), NORM_F(X[:, 2])]
	Y = NORM_F(Y)

	# Split data in train set and test set
	X_train, X_test, Y_train, Y_test = data_spliter(X, Y, .2)

	fig2 = plt.figure()
	ax2 = fig2.subplots(ncols=2)

	# Metrics to log
	metrics = pd.DataFrame()

	# Will train for degree 1 to 4 included
	for degree in range(1, 5):

		# Generate random thetas and initialize linear regression class
		lr = MyLR(np.random.rand(3 * degree + 1, 1), 0.01, 20000)

		# Add polynomial degree
		X_train_d:np.ndarray = np.c_[add_polynomial_features(X_train[:, 0], degree), add_polynomial_features(X_train[:, 1], degree), add_polynomial_features(X_train[:, 2], degree)]
		X_test_d:np.ndarray = np.c_[add_polynomial_features(X_test[:, 0], degree), add_polynomial_features(X_test[:, 1], degree), add_polynomial_features(X_test[:, 2], degree)]

		# Train model on train set and set prediction data on train set and on test set
		lr.fit_(X_train_d, Y_train)
		Y_hat_train, Y_hat_test = lr.predict_(X_train_d), lr.predict_(X_test_d)

		# Init plot figure and axes
		fig = plt.figure()
		ax = fig.subplots(ncols=3, nrows=2)
		labels = ['Weight', 'Prod distance', 'Time delivery']

		# Plot data
		for i in range(3):
			# Scatter true values in blue
			ax[0][i].scatter(X_train_d[:, i * degree], Y_train, c='blue', alpha=.5, label='True values')
			ax[1][i].scatter(X_test_d[:, i * degree], Y_test, c='blue', alpha=.5, label='True values')

			# Scatter prediction values
			ax[0][i].scatter(X_train_d[:, i * degree], Y_hat_train, c='violet', alpha=.5, label='Prediction values')
			ax[1][i].scatter(X_test_d[:, i * degree], Y_hat_test, c='violet', alpha=.5, label='Prediction values')

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
		fig.text(x=0., y=.98, s=f'Degree: {degree}')

		mse_train = lr.mse_(Y_train, Y_hat_train)
		mse_test = lr.mse_(Y_test, Y_hat_test)

		# Print score over train set and test set
		print(f'Degree {degree}:\nMSE train: {mse_train}\nMSE test: {mse_test}\n\n')

		# Plot MSE for this degree
		bar_train = ax2[0].bar(degree, mse_train, label=f'Degree {degree}')
		bar_test = ax2[1].bar(degree, mse_test, label=f'Degree {degree}')
		ax2[0].bar_label(bar_train)
		ax2[1].bar_label(bar_test)

		# Add metrics for this degree
		new_metric = pd.DataFrame({'degree': [degree], 'theta': [' '.join(str(x).strip('[]') for x in lr.theta)],'mse_train': [mse_train], 'mse_test': [mse_test]})
		metrics = pd.concat([metrics, new_metric], ignore_index=True, axis=0)

		# Plot 3d representation for best model:
		if degree == 3:
			# Create subplots
			fig3d = plt.figure()
			ax3d1 = fig3d.add_subplot(231, projection='3d')
			ax3d2 = fig3d.add_subplot(232, projection='3d')
			ax3d3 = fig3d.add_subplot(233, projection='3d')
			ax3d4 = fig3d.add_subplot(234, projection='3d')
			ax3d5 = fig3d.add_subplot(235, projection='3d')
			ax3d6 = fig3d.add_subplot(236, projection='3d')

			# Scatter true values, predicted values and error in 4d
			img1 = ax3d4.scatter(X_test_d[:, 0 * degree], X_test_d[:, 1 * degree], X_test_d[:, 2 * degree], c=Y_test, cmap=plt.hot())
			img2 = ax3d5.scatter(X_test_d[:, 0 * degree], X_test_d[:, 1 * degree], X_test_d[:, 2 * degree], c=Y_hat_test, cmap=plt.hot())
			img3 = ax3d6.scatter(X_test_d[:, 0 * degree], X_test_d[:, 1 * degree], X_test_d[:, 2 * degree], c=np.abs(Y_test - Y_hat_test), cmap=plt.plasma())
		
			# Add colorbars that represent the 4th dimension, price
			fig3d.colorbar(img1, ax=ax3d4, label='True price values')
			fig3d.colorbar(img2, ax=ax3d5, label='Predicted price values')
			fig3d.colorbar(img3, ax=ax3d6, label='Error map on price values')

			# Scatter price in z and 2 of the 3 parameters in x and y
			ax3d1.scatter(X_test_d[:, 0 * degree], X_test_d[:, 1 * degree], Y_test, c='blue', alpha=.5)
			ax3d1.scatter(X_test_d[:, 0 * degree], X_test_d[:, 1 * degree], Y_hat_test, c='violet', alpha=.5)
			ax3d1.set_xlabel('Weight')
			ax3d1.set_ylabel('Prod distance')
			ax3d1.set_zlabel('Price')
			ax3d2.scatter(X_test_d[:, 0 * degree], X_test_d[:, 2 * degree], Y_test, c='blue', alpha=.5)
			ax3d2.scatter(X_test_d[:, 0 * degree], X_test_d[:, 2 * degree], Y_hat_test, c='violet', alpha=.5)
			ax3d2.set_xlabel('Weight')
			ax3d2.set_ylabel('Time delivery')
			ax3d2.set_zlabel('Price')
			ax3d3.scatter(X_test_d[:, 1 * degree], X_test_d[:, 2 * degree], Y_test, c='blue', alpha=.5)
			ax3d3.scatter(X_test_d[:, 1 * degree], X_test_d[:, 2 * degree], Y_hat_test, c='violet', alpha=.5)
			ax3d3.set_xlabel('Prod distance')
			ax3d3.set_ylabel('Time delivery')
			ax3d3.set_zlabel('Price')


	# Set titles and labels for MSE metrics
	ax2[0].set_xlabel('Degree')
	ax2[1].set_xlabel('Degree')
	ax2[0].set_ylabel('MSE')
	ax2[1].set_ylabel('MSE')
	ax2[0].set_title('Train set')
	ax2[1].set_title('Test set')

	# Write metrics to csv
	metrics.to_csv('./models.csv')

	plt.show()


if __name__ == '__main__':
	main()

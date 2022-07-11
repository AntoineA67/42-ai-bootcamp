import enum
import numpy as np
import sys
from data_spliter import data_spliter
import pandas as pd
from my_logistic_regression import MyLogisticRegression as MyLR
import matplotlib.pyplot as plt
from z_score import zscore

def main():

	# Read data
	data = pd.read_csv('../resources/solar_system_census.csv')
	data_labels = pd.read_csv('../resources/solar_system_census_planets.csv')

	# Init X
	X: np.ndarray = np.array(data.values[:, 1:])
	# Normalize data
	X: np.ndarray = np.array([zscore(X[:, i]) for i in range(X.shape[1])]).swapaxes(0, 1)

	# Init Y
	Y: np.ndarray = np.array(data_labels['Origin'])[:, np.newaxis]
	# Y: np.ndarray = zscore(Y)

	# Split dataset
	X_train, X_test, Y_train, Y_test = data_spliter(X, Y, .35)

	Y_hat_test_multi = np.array(0)

	for zcode in range(4):

		Y_train_loc = np.array([1 if x == zcode else 0 for x in Y_train])[:, np.newaxis]
		Y_test_loc = np.array([1 if x == zcode else 0 for x in Y_test])[:, np.newaxis]

		lr = MyLR(np.random.rand(4), .001, 50000)

		print(f'Zcode: {zcode}')
		print(f'Loss before training on train set (random theta): {lr.loss_(Y_train_loc, lr.predict_(X_train)):.3f}')
		print(f'Loss before training on test set (random theta): {lr.loss_(Y_test_loc, lr.predict_(X_test)):.3f}')
		Y_hat_test = lr.predict_(X_test)
		Y_hat_norm = np.array([1.0 if x > .5 else 0.0 for x in Y_hat_test])[:, np.newaxis]
		correct = np.sum([Y_test_loc[i][0] == Y_hat_norm[i][0] for i in range(len(X_test))])

		print(f'Fraction of correct prediction on test set before training (should be around 25%): {correct} / {len(X_test)} ({correct / len(X_test) * 100:.3f}%)')

		# Train model
		lr.fit_(X_train, Y_train_loc)
		Y_hat_test = lr.predict_(X_test)

		print(f'Loss after training on train set: {lr.loss_(Y_train_loc, lr.predict_(X_train)):.3f}')
		print(f'Loss after training on test set: {lr.loss_(Y_test_loc, Y_hat_test):.3f}')

		# Normalize data, if output > .5 consider 1 else consider 0
		Y_hat_norm = np.array([1.0 if x > .5 else 0.0 for x in Y_hat_test])[:, np.newaxis]
		correct = np.sum([Y_test_loc[i][0] == Y_hat_norm[i][0] for i in range(len(X_test))])

		print(f'Fraction of correct prediction on test set: {correct} / {len(X_test)} ({correct / len(X_test) * 100:.3f}%)\n\n')

		if zcode == 0:
			Y_hat_test_multi = Y_hat_test
		else:
			Y_hat_test_multi = np.c_[Y_hat_test_multi, Y_hat_test]

	# Compute multi log regression
	Y_flat = Y_test.reshape(1, -1).astype(int)[0]
	Y_hat_index = np.argmax(Y_hat_test_multi, axis=1)
	prediction = np.array([1 if Y_hat_index[i] == Y_flat[i] else 0 for i in range(len(Y_flat))])


	print('Multi log regression:')
	print(f'Fraction of correct prediction on test set: {prediction.sum()} / {prediction.size} ({prediction.sum() / prediction.size * 100:.3f}%)\n')

	# Scatter data
	_, ax = plt.subplots(ncols=4)

	labels = ['Weight', 'Height', 'Bone Density']

	for i in range(3):
		ax[i].scatter(X_test[:, i], Y_test, alpha=.5, label='True values', c=prediction)
		ax[i].set_xlabel(labels[i])
		ax[i].set_ylabel('Location')

	ax[3].scatter(np.arange(Y_flat.size, dtype=int), Y_flat, alpha=.5, label='True values', c=prediction)
	ax[3].set_xlabel('Index')
	ax[3].set_ylabel('Location')

	plt.show()


if __name__ == '__main__':
	main()

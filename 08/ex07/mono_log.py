import numpy as np
import sys
from data_spliter import data_spliter
import pandas as pd
from my_logistic_regression import MyLogisticRegression as MyLR
import matplotlib.pyplot as plt
from z_score import zscore

def main(args):
	# Check zcode
	zcode = args[1].split('=')
	if len(args) != 2 or '-zipcode' not in zcode or len(zcode) != 2 or not zcode[1].isdigit() or int(zcode[1]) not in np.arange(4):
		print('Usage: `python mono_log.py -zipcode=x` with x being 0, 1, 2 or 3')
		return
	zcode = float(zcode[1])
	
	# Read data
	data = pd.read_csv('../resources/solar_system_census.csv')
	data_labels = pd.read_csv('../resources/solar_system_census_planets.csv')

	# Init X and Y
	X: np.ndarray = np.array(data.values[:, 1:])
	# Normalize data
	X: np.ndarray = np.array([zscore(X[:, i]) for i in range(X.shape[1])]).swapaxes(0, 1)
	Y: np.ndarray = np.array([1 if x == zcode else 0 for x in data_labels['Origin']])[:, np.newaxis]
	
	# Split dataset
	X_train, X_test, Y_train, Y_test = data_spliter(X, Y, .35)

	lr = MyLR(np.random.rand(4), .001, 150000)

	print(f'Loss before training on train set (random theta): {lr.loss_(Y_train, lr.predict_(X_train)):.3f}')
	print(f'Loss before training on test set (random theta): {lr.loss_(Y_test, lr.predict_(X_test)):.3f}')
	Y_hat_test = lr.predict_(X_test)
	Y_hat_norm = np.array([1.0 if x > .5 else 0.0 for x in Y_hat_test])[:, np.newaxis]
	correct = np.sum([Y_test[i][0] == Y_hat_norm[i][0] for i in range(len(X_test))])

	print(f'Fraction of correct prediction on test set before training (should be around 25%): {correct} / {len(X_test)} ({correct / len(X_test) * 100:.3f}%)')

	# Train model
	lr.fit_(X_train, Y_train)
	Y_hat_test = lr.predict_(X_test)

	print(f'Loss after training on train set: {lr.loss_(Y_train, lr.predict_(X_train)):.3f}')
	print(f'Loss after training on test set: {lr.loss_(Y_test, Y_hat_test):.3f}')

	# Normalize data, if output > .5 consider 1 else consider 0
	Y_hat_norm = np.array([1.0 if x > .5 else 0.0 for x in Y_hat_test])[:, np.newaxis]
	correct = np.sum([Y_test[i][0] == Y_hat_norm[i][0] for i in range(len(X_test))])

	print(f'Fraction of correct prediction on test set: {correct} / {len(X_test)} ({correct / len(X_test) * 100:.3f}%)')

	_, ax = plt.subplots(ncols=3)

	labels = ['Weight', 'Height', 'Bone Density']

	for i in range(3):
		ax[i].scatter(X_test[:, i], Y_test, alpha=.5, label='True values')
		ax[i].scatter(X_test[:, i], Y_hat_norm, alpha=.5, c='violet', label='Prediction values')
		ax[i].set_xlabel(labels[i])
		ax[i].set_ylabel('Location')

	plt.show()


if __name__ == '__main__':
	main(sys.argv)

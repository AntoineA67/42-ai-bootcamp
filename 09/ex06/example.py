import numpy as np
from ridge import MyRidge
from multi_linear_regression import MyLinearRegression as MyLR
import matplotlib.pyplot as plt

def main():
	X = np.random.rand(3, 4)
	Y = np.array([[23.], [48.], [218.]])
	mylr = MyRidge([[42.], [1.], [1.], [1.], [1]], lambda_=.5)

	# Example 0:
	y_hat = mylr.predict_(X)
	print(f'y_hat:\n{y_hat}\n\n')

	# Example 1:
	print(f'mylr.loss_elem_(Y, y_hat):\n{mylr.loss_elem_(Y, y_hat)}\n\n')

	# Example 2:
	print(f'mylr.loss_(Y, y_hat):\n{mylr.loss_(Y, y_hat)}\n\n')

	# Example 3:
	mylr.alpha = 1.6e-4
	mylr.max_iter = 20000
	mylr.fit_(X, Y)
	print(f'mylr.theta:\n{mylr.theta}\n\n')

	# Example 4:
	y_hat = mylr.predict_(X)
	print(f'y_hat:\n{y_hat}\n\n')

	# Example 5:
	print(f'mylr.loss_elem_(Y, y_hat):\n{mylr.loss_elem_(Y, y_hat)}\n\n')

	# Example 6:
	print(f'mylr.loss_(Y, y_hat):\n{mylr.loss_(Y, y_hat)}\n\n')


	X = np.random.rand(20)[:, np.newaxis]
	Y = np.random.rand(20)[:, np.newaxis]

	_, ax = plt.subplots()

	for i in range(5):
		mylr = MyRidge([[1.], [1.]], lambda_=i, alpha=.001, max_iter=10000)
		mylr.fit_(X, Y)
		Y_hat = mylr.predict_(X)
		ax.scatter(X, Y_hat)
		ax.plot(X, Y_hat, label=f'Lambda {i}')

	ax.scatter(X, Y)
	ax.legend()
	plt.show()

if __name__ == '__main__':
	main()

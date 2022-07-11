import numpy as np
from ridge import MyRidge
import matplotlib.pyplot as plt

def main():
	X = np.random.rand(3, 4)
	Y = np.array([[23.], [48.], [218.]])
	# Y = np.random.rand(3)[:, np.newaxis]
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
	print(X, Y)
	mylr.fit_(X, Y)
	print(f'mylr.theta:\n{mylr.theta}\n\n')

	# Example 4:
	y_hat = mylr.predict_(X)
	print(f'y_hat:\n{y_hat}\n\n')

	# Example 5:
	print(f'mylr.loss_elem_(Y, y_hat):\n{mylr.loss_elem_(Y, y_hat)}\n\n')

	# Example 6:
	print(f'mylr.loss_(Y, y_hat):\n{mylr.loss_(Y, y_hat)}\n\n')

	X = np.array([[1.], [2.], [3.]])
	Y = np.random.rand(3)[:, np.newaxis]
	mylr = MyRidge([[1.], [1.]], lambda_=0)

	mylr.fit_(X, Y)
	Y_hat = mylr.predict_(X)
	_, ax = plt.subplots()

	ax.scatter(X, Y)
	ax.scatter(X, Y_hat, c='violet')
	ax.plot(X, Y_hat)

	plt.show()

if __name__ == '__main__':
	main()

import numpy as np
from my_linear_regression import MyLinearRegression as MyLR

def main():
	
	X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [34., 55., 89., 144.]])
	X = np.random.rand(3, 4)
	Y = np.array([[23.], [48.], [218.]])
	Y = np.random.rand(3)[:, np.newaxis]
	mylr = MyLR([[42.], [1.], [1.], [1.], [1]])

	# Example 0:
	y_hat = mylr.predict_(X)
	print(f'y_hat:\n{y_hat}\n\n')
		# Output:
		# array([[8.], [48.], [323.]])

	# Example 1:
	print(f'mylr.loss_elem_(Y, y_hat):\n{mylr.loss_elem_(Y, y_hat)}\n\n')
		# Output:
		# array([[225.], [0.], [11025.]])

	# Example 2:
	print(f'mylr.loss_(Y, y_hat):\n{mylr.loss_(Y, y_hat)}\n\n')
		# Output:
		# 1875.0

	# Example 3:
	mylr.alpha = 1.6e-4
	mylr.max_iter = 200000
	mylr.fit_(X, Y)
	print(f'mylr.theta:\n{mylr.theta}\n\n')
		# Output:
		# array([[18.188..], [2.767..], [-0.374..], [1.392..], [0.017..]])

	# Example 4:
	y_hat = mylr.predict_(X)
	print(f'y_hat:\n{y_hat}\n\n')
		# Output:
		# array([[23.417..], [47.489..], [218.065...]])

	# Example 5:
	print(f'mylr.loss_elem_(Y, y_hat):\n{mylr.loss_elem_(Y, y_hat)}\n\n')
		# Output:
		# array([[0.174..], [0.260..], [0.004..]])

	# Example 6:
	print(f'mylr.loss_(Y, y_hat):\n{mylr.loss_(Y, y_hat)}\n\n')
		# Output:
		# 0.0732..

if __name__ == '__main__':
	main()

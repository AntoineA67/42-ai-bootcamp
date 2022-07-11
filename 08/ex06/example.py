import numpy as np
from my_logistic_regression import MyLogisticRegression as MyLR

def main():
	X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [3., 5., 9., 14.]])
	Y = np.array([[1], [0], [1]])
	# Randomized thetas
	mylr = MyLR(np.random.rand(5), 0.001, 100000)

	# Example 0:
	Y_hat = mylr.predict_(X)
	print(Y_hat, '\n')
		# Output:
		# array([[0.99930437],
		# [1. ],
		# [1. ]])

	# Example 1:
	# Erreur example
	print('Loss before training', mylr.loss_(Y,Y_hat), '\n')
		# Output:
		# 11.513157421577004

	# Example 2:
	mylr.fit_(X, Y)
	print(mylr.theta, '\n')
		# Output:
		# array([[ 1.04565272],
		# [ 0.62555148],
		# [ 0.38387466],
		# [ 0.15622435],
		# [-0.45990099]])

	# Example 3:
	Y_hat = mylr.predict_(X)
	print(Y_hat, '\n')
		# Output:
		# array([[0.72865802],
		# [0.40550072],
		# [0.45241588]])

	# Example 4:
	print('Loss after training', mylr.loss_(Y,Y_hat))
		# Output:
		# 0.5432466580663214

if __name__ == '__main__':
	main()

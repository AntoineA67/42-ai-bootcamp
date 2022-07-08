from loss import loss_
import numpy as np

def main():

	X = np.array([0, 15, -9, 7, 12, 3, -21]).reshape((-1, 1))
	Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))

	# Example 1:
	print(f'{loss_(X, Y)}\n')
		# Output:
		# 2.142857142857143

	# Example 2:
	print(f'{loss_(X, X)}\n')
		# Output:
		# 0.0

if __name__ == '__main__':
	main()

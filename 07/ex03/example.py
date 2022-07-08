from gradient import gradient
import numpy as np

def main():
	x = np.array([
	[ -6, -7, -9],
	[ 13, -2, 14],
	[ -7, 14, -1],
	[ -8, -4, 6],
	[ -5, -9, 6],
	[ 1, -5, 11],
	[ 9, -11, 8]])

	y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))

	# OUBLI DANS LE SUJET
	theta1 = np.array([3, 0.5, -6, -25]).reshape((-1, 1))

	# Example :
	print(f'Theta 1:\n{gradient(x, y, theta1)}\n\n')
		# Output:
		# PAS DANS LE SUJET
		# array([[ -33.71428571], [ -37.35714286], [183.14285714], [-393.]])

	# Example :
	theta2 = np.array([0, 0, 0, 0]).reshape((-1, 1))
	print(f'Theta 2:\n{gradient(x, y, theta2)}')
		# Output:
		# array([[ -0.71428571], [ 0.85714286], [23.28571429], [-26.42857143]])

if __name__ == '__main__':
	main()

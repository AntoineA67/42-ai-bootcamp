import numpy as np
from loss import loss_, loss_elem_
from prediction import predict_
from plot import plot

def main():
	x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
	theta1 = np.array([[2.], [4.]])
	y_hat1 = predict_(x1, theta1)
	y1 = np.array([[2.], [7.], [12.], [17.], [22.]])

	print(f'x1:\n{x1}\n\ntheta1:\n{theta1}\n\ny_hat1:\n{y_hat1}\n\ny1:\n{y1}\n\n')

	# Example 1:
	print(f'Loss elem y1 y_hat1:\n{loss_elem_(y1, y_hat1)}\n\n')
		# Output:
		# array([[0.], [1], [4], [9], [16]])

	# Example 2:
	print(f'Loss y1 y_hat1:\n{loss_(y1, y_hat1)}\n\n')
		# Output:
		# 3.0

	x2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
	theta2 = np.array([[0.05], [1.], [1.], [1.]])
	y_hat2 = predict_(x2, theta2)
	y2 = np.array([[19.], [42.], [67.], [93.]])
	print(f'x2:\n{x2}\n\ntheta2:\n{theta2}\n\ny_hat2:\n{y_hat2}\n\ny2:\n{y2}\n\n')

	# Example 3:
	print(f'Loss_elem y2 y_hat2:\n{loss_elem_(y2, y_hat2)}\n\n')
		# Output:
		# array([[10.5625], [ 6.0025], [ 0.1225], [17.2225]])

	# Example 4:
	print(f'Loss y2 y_hat2:\n{loss_(y2, y_hat2)}\n\n')
		# Output:
		# 4.238750000000004
	x3 = np.array([0, 15, -9, 7, 12, 3, -21])
	# theta3 = np.array([[0.], [1.]])
	theta3 = np.array([[0.], [1.]])
	y_hat3 = predict_(x3, theta3)
	y3 = np.array([2, 14, -13, 5, 12, 4, -19])
	print(f'x3:\n{x3}\n\ntheta3:\n{theta3}\n\ny_hat3:\n{y_hat3}\n\ny3:\n{y3}\n\n')

	# Example 5:
	print(f'Loss y3 y_hat3:\n{loss_(y3, y_hat3)}\n\n')
		# Output:
		# 2.142857142857143

	# Example 6:
	print(f'Loss y3 y3:\n{loss_(y3, y3)}\n\n')
		# Output:
		# 0.0

if __name__ == '__main__':
	main()

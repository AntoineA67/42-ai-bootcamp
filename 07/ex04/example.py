from fit import fit_
from prediction import predict_
import numpy as np
from loss import loss_
import matplotlib.pyplot as plt

def main():
	x = np.random.rand(4, 3)
	y = np.random.rand(4, 1)
	theta = np.array([[42.], [1.], [1.], [1.]])
	# Can also try with random theta
	# theta = np.random.rand(4)[:, np.newaxis]

	# Example 0:
	theta2 = fit_(x, y, theta, alpha = 0.0005, max_iter=42000)
	print(f'Theta after training:\n{theta2}\n')

	# Example 1:
	print(f'Predict after training:\n{predict_(x, theta2)}\n')
	print(f'Loss before training: {loss_(y, predict_(x, theta))}\nLoss after training: {loss_(y, predict_(x, theta2))}')

if __name__ == '__main__':
	main()

from my_linear_regression import MyLinearRegression as MyLR
import matplotlib.pyplot as plt
import numpy as np

def main():
	x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
	y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])
	lr1 = MyLR([2, 0.7])

	# Example 0.0:
	print(f'lr1.predict_(x):\n{lr1.predict_(x)}\n\n')
	# Output:
		# array([[10.74695094],
		# [17.05055804],
		# [24.08691674],
		# [36.24020866],
		# [42.25621131]])

	# Example 0.1:
	print(f'MyLR.loss_elem_(y, lr1.predict_(x)):\n{MyLR.loss_elem_(y, lr1.predict_(x))}\n\n')
	# Output:
		# array([[710.45867381],
		# [364.68645485],
		# [469.96221651],
		# [108.97553412],
		# [299.37111101]])

	# Example 0.2:
	print(f'MyLR.loss_(y, lr1.predict_(x)):\n{MyLR.loss_(y, lr1.predict_(x))}\n\n')
	# Output:
		# 195.34539903032385

	# Example 1.0:
	lr2 = MyLR([1, 1], 5e-5, 150000)
	lr2.fit_(x, y)
	print(f'lr2.thetas after lr2.fit_():\n{lr2.thetas}\n\n')
	# lr2 = MyLR([1, 1], 5e-8, 1500000)
	# lr2.fit_(x, y)
	# print(f'lr2.thetas after lr2.fit_():\n{lr2.thetas}\n\n')
	# Output:
		# array([[1.40709365],
		# [1.1150909 ]])

	# Example 1.1:
	print(f'lr2.predict_(x):\n{lr2.predict_(x)}\n\n')
	# Output:
		# array([[15.3408728 ],
		# [25.38243697],
		# [36.59126492],
		# [55.95130097],
		# [65.53471499]])

	# Example 1.2:
	print(f'MyLR.loss_elem_(y, lr2.predict_(x)):\n{MyLR.loss_elem_(y, lr2.predict_(x))}\n\n')
	# Output:
		# array([[486.66604863],
		# [115.88278416],
		# [ 84.16711596],
		# [ 85.96919719],
		# [ 35.71448348]])

	# Example 1.3:
	print(f'MyLR.loss_(y, lr2.predict_(x)):\n{MyLR.loss_(y, lr2.predict_(x))}')
	# Output:
		# 80.83996294128525
	_, ax = plt.subplots(ncols=2)
	lr1.plot_with_loss_(x, y, ax[0])
	lr2.plot_with_loss_(x, y, ax[1])
	plt.show()

if __name__ == '__main__':
	main()

import numpy as np
from multi_linear_regression import MyLinearRegression as MyLR
import pandas as pd
from multivariate_linear_model import model

def main():
	
	data = pd.read_csv("../resources/spacecraft_data.csv")
	X = np.array(data[['Age']])
	Y = np.array(data[['Sell_price']])

	myLR_age = MyLR(theta = [[1000.0], [-1.0]], alpha = 2.5e-5, max_iter = 100000)
	myLR_age.fit_(X[:,0].reshape(-1,1), Y)
	print(myLR_age.mse_(X[:,0].reshape(-1,1),Y))
		#Output
		# 57636.77729...

	# model(data)

if __name__ == '__main__':
	main()

import matplotlib.pyplot as plt
import numpy as np
from ScrapBooker import ScrapBooker
from ImageProcessor import ImageProcessor

def main():
	spb = ScrapBooker()
	arr1 = np.arange(0,25).reshape(5,5)
	print('Arr1:\n', arr1, '\n')
	print(spb.crop(arr1, (7, 1), (1, 0)), '\n')
	print(spb.crop(arr1, (3,1),(1,0)), '\n')
	#Output :
		# array([[ 5],
		# [10],
		# [15]])

	arr2 = np.array("A B C D E F G H I J K".split() * 6).reshape(-1,11)
	print('Arr2:\n', arr2, '\n')
	print(spb.thin(arr2,11,0), '\n')
	print(spb.thin(arr2,3,0), '\n')
	#Output :
		# array([[’A’, ’B’, ’D’, ’E’, ’G’, ’H’, ’J’, ’K’],
		# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’, ’J’, ’K’],
		# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’, ’J’, ’K’],
		# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’, ’J’, ’K’],
		# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’, ’J’, ’K’],
		# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’, ’J’, ’K’]], dtype=’<U1’)

	arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
	print('Arr3:\n', arr3, '\n')
	print(spb.juxtapose(arr3, -1, 1), '\n')
	print(spb.juxtapose(arr3, 3, 1), '\n')
	spb.juxtapose(arr3, 3, 1)
	#Output :
		# array([[1, 2, 3, 1, 2, 3, 1, 2, 3],
		# [1, 2, 3, 1, 2, 3, 1, 2, 3],
		# [1, 2, 3, 1, 2, 3, 1, 2, 3]])

	arr4 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
	print('Arr4:\n', arr4, '\n')
	print(spb.mosaic(arr4, (-1, 1)), '\n')
	print(spb.mosaic(arr4, (3, 2)), '\n')

	imp = ImageProcessor()
	arr = imp.load("../resources/42AI.png")
	_, ax = plt.subplots(2, 2)
	ax[0, 0].imshow(spb.crop(arr, (150, 20), (20, 20)))
	ax[0, 1].imshow(spb.thin(arr, 4, 0))
	ax[1, 0].imshow(spb.juxtapose(arr, 2, 0))
	plt.show()
	



if __name__ =='__main__':
	main()
import numpy as np
from ScrapBooker import ScrapBooker

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

	arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
	print('Arr2:\n', arr2, '\n')
	print(spb.thin(arr2,9,0), '\n')
	print(spb.thin(arr2,3,0), '\n')
	spb.thin(arr2,3,0)
	#Output :
		# array([[’A’, ’B’, ’D’, ’E’, ’G’, ’H’, ’J’, ’K’],
		# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’, ’J’, ’K’],
		# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’, ’J’, ’K’],
		# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’, ’J’, ’K’],
		# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’, ’J’, ’K’],
		# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’, ’J’, ’K’]], dtype=’<U1’)

	arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
	# spb.juxtapose(arr3, 3, 1)
	#Output :
		# array([[1, 2, 3, 1, 2, 3, 1, 2, 3],
		# [1, 2, 3, 1, 2, 3, 1, 2, 3],
		# [1, 2, 3, 1, 2, 3, 1, 2, 3]])


if __name__ =='__main__':
	main()
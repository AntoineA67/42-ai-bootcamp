import numpy as np

class ScrapBooker:
	def __init__(self) -> None:
		pass

	def crop(self, array: np.ndarray, dim: tuple, position: tuple=(0,0)) -> np.ndarray:
		"""
		Crops the image as a rectangle via dim arguments (being the new height
		and width of the image) from the coordinates given by position arguments.
		Args:
		-----
		array: numpy.ndarray
		dim: tuple of 2 integers.
		position: tuple of 2 integers.
		Return:
		-------
		new_arr: the cropped numpy.ndarray.
		None (if combinaison of parameters not compatible).
		Raise:
		------
		This function should not raise any Exception.
		"""
		s = array.shape
		if len(dim) != 2 or len(position) != 2 or any(d < 0 for d in dim) or any(d < 0 for d in position) or s[0] < position[0] or s[0] < dim[0] + position[0] or s[1] < position[1] or s[1] < dim[1] + position[1]:
			return None
		return array[position[0]:dim[0] + position[0], position[1]:dim[1] + position[1]]

	def thin(self, array: np.ndarray, n: int, axis: int) -> np.ndarray:
		"""
		Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
		Args:
		-----
		array: numpy.ndarray.
		n: non null positive integer lower than the number of row/column of the array
		(depending of axis value).
		axis: positive integer.
		Return:
		-------
		new_arr: thined numpy.ndarray.
		None (if combinaison of parameters not compatible).
		Raise:
		------
		This function should not raise any Exception.
		"""
		s = array.shape
		axis = (axis - 1) * -1
		if n <= 0 or axis not in (0, 1) or n > s[axis]:
			return None
		return np.delete(array, range(n - 1, s[axis], n), axis)


	def juxtapose(self, array, n, axis):
		"""
		Juxtaposes n copies of the image along the specified axis.
		Args:
		-----
		array: numpy.ndarray.
		n: positive non null integer.
		axis: integer of value 0 or 1.
		Return:
		-------
		new_arr: juxtaposed numpy.ndarray.
		None (combinaison of parameters not compatible).
		Raises:
		-------
		This function should not raise any Exception.
		"""
		pass
	def mosaic(self, array, dim):
		"""
		Makes a grid with multiple copies of the array. The dim argument specifies
		the number of repetition along each dimensions.
		Args:
		-----
		array: numpy.ndarray.
		dim: tuple of 2 integers.
		Return:
		-------
		new_arr: mosaic numpy.ndarray.
		None (combinaison of parameters not compatible).
		Raises:
		-------
		This function should not raise any Exception.
		"""
		pass

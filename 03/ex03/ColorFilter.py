import numpy as np

class ColorFilter:
	def invert(self, array: np.ndarray):
		"""
		Inverts the color of the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		new_arr = array.copy()
		new_arr[:, :, :3] = 1 - new_arr[:, :, :3]
		return new_arr

	def to_blue(self, array):
		"""
		Applies a blue filter to the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		new_arr = np.dstack((np.zeros((array.shape[0], array.shape[1], 2)), array.copy()[:, :, 2:]))
		return new_arr

	def to_green(self, array):
		"""
		Applies a green filter to the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		new_arr = array.copy()
		new_arr[:, :, (0, 2)] *= 0
		return new_arr

	def to_red(self, array):
		"""
		Applies a red filter to the image received as a numpy array.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		# new_arr = array.copy() - (self.to_blue(array) + self.to_green(array))
		new_arr = array.copy()
		new_arr[:, :, :3] -= self.to_blue(array)[:, :, :3] + self.to_green(array)[:, :, :3]
		return new_arr
	
	def to_celluloid(self, array: np.ndarray):
		"""
		Applies a celluloid filter to the image received as a numpy array.
		Celluloid filter must display at least four thresholds of shades.
		Be careful! You are not asked to apply black contour on the object,
		you only have to work on the shades of your images.
		Remarks:
		celluloid filter is also known as cel-shading or toon-shading.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""

		def t(x: np.float64, means: np.ndarray):
			for v in means[::-1]:
				if x >= v:
					return v
			return means[0]

		new_arr: np.ndarray = array.copy()
		means = np.linspace((array[:, :, 0].min(), array[:, :, 1].min(), array[:, :, 2].min()), (array[:, :, 0].max(), array[:, :, 1].max(), array[:, :, 2].max()), num=5)
		for y in new_arr:
			for x in y:
				x[0], x[1], x[2] = t(x[0], means[:, 0]), t(x[1], means[:, 1]), t(x[2], means[:, 2])
		return new_arr

	def to_grayscale(self, array: np.ndarray, filter, **kwargs):
		"""
		Applies a grayscale filter to the image received as a numpy array.
		For filter = 'mean'/'m': performs the mean of RBG channels.
		For filter = 'weight'/'w': performs a weighted mean of RBG channels.
		Args:
		-----
		array: numpy.ndarray corresponding to the image.
		filter: string with accepted values in ['m','mean','w','weight']
		weights: [kwargs] list of 3 floats where the sum equals to 1,
		corresponding to the weights of each RBG channels.
		Return:
		-------
		array: numpy.ndarray corresponding to the transformed image.
		None: otherwise.
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if filter not in ['m','mean','w','weight']:
			return None
		
		mask = [True, True, True]
		if filter in ['m', 'mean']:
			if array.shape[2] == 4:
				mask += [False]
			new_arr: np.ndarray = array.sum(axis=(2), where=mask) / 3
		else:
			if not kwargs.get('weights') or len(kwargs['weights']) != 3:
				return None
			w = kwargs['weights']
			new_arr: np.ndarray = (array[:, :, :3] * w).sum(axis=(2), where=mask)

		new_arr = new_arr[:, :, None]
		new_arr = np.broadcast_to(new_arr, new_arr.shape[:2]+(3,))
		
		return new_arr
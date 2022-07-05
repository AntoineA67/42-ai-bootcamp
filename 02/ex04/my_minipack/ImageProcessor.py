import sys
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

class ImageProcessor():
	@staticmethod
	def load(path):
		try:
			img_array = mpimg.imread(path)

			# Trick to make it work with other formats
			if img_array.dtype == np.uint8:
				img_array = img_array.astype(np.float64) / 255

			print(f'Loading image of dimension {img_array.shape[0]}x{img_array.shape[1]}')
			return img_array
		except FileNotFoundError:
			print(f"Exception: File not found: '{path}'", file=sys.stderr)
		except SyntaxError:
			print(f"Exception: Invalid file: '{path}'", file=sys.stderr)

	@staticmethod
	def display(array):
		try:
			plt.imshow(array)
			plt.show()
		except TypeError:
			print(f"Exception: Could not display file", file=sys.stderr)
			return


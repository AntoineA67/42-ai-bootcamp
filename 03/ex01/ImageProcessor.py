import sys
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import PIL

class ImageProcessor():
	@staticmethod
	def load(path):
		try:
			img = mpimg.imread(path)
			img_array = np.array(img)
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

imp = ImageProcessor()
arr = imp.load("fef.png")
print(arr)
arr = imp.load("./empty_file.png")
print(arr)
arr = imp.load("../resources/42AI.png")
print(arr)
imp.display(arr)

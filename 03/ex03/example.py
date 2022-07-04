from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter
import matplotlib.pyplot as plt

def displays(arr, imp, cf):
	imp.display(arr)
	imp.display(cf.invert(arr))
	imp.display(cf.to_green(arr))
	imp.display(cf.to_red(arr))
	imp.display(cf.to_blue(arr))
	imp.display(cf.to_celluloid(arr))
	imp.display(cf.to_grayscale(arr, 'm'))
	imp.display(cf.to_grayscale(arr, 'weight', weights = [.2, 0.1, 0.7]))

def main():
	imp = ImageProcessor()
	cf = ColorFilter()

	img_paths = ["../resources/chicken.png",
		"../resources/elon_canaGAN.png",
		"../resources/42AI.png",
		"../resources/landscape.png",
		"../resources/landscape2.jpg"]
	filters = ['No filter', 'Invert', 'Blue', 'Green', 'Red', 'Celluloid', 'Grayscale mean', 'Grayscale weight'] * len(img_paths)
	imgs = []

	if input('Images gallery ?') == 'n':
		print('Showing images one by one')
		for path in img_paths:
			img = imp.load(path)
			displays(img, imp, cf)
		return 0

	print('Showing images gallery')
	for path in img_paths:
		img = imp.load(path)
		imgs += [img, cf.invert(img), cf.to_blue(img), cf.to_green(img), cf.to_red(img),\
			cf.to_celluloid(img), cf.to_grayscale(img, 'm'), cf.to_grayscale(img, 'weight', weights = [.2, 0.1, 0.7])]

	_, axs = plt.subplots(nrows=len(img_paths), ncols=8, figsize=(9, 6),
		subplot_kw={'xticks': [], 'yticks': []})
	for ax, flt, img in zip(axs.flat, filters, imgs):
		ax.imshow(img)
		ax.set_title(str(flt))
	plt.tight_layout()
	plt.show()
	
if __name__ == '__main__':
	main()

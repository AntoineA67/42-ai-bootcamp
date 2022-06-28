from ImageProcessor import ImageProcessor

def main():
	imp = ImageProcessor()
	arr = imp.load("fef.png")
	print(arr)
	arr = imp.load("./empty_file.png")
	print(arr)
	arr = imp.load("../resources/42AI.png")
	print(arr)
	imp.display(arr)

if __name__ == '__main__':
	main()

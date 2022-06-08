import sys

def main():
	if (len(sys.argv) != 2):
		print("Wrong number of arguments")
	else:
		print(sys.argv[1].swapcase()[::-1])

if __name__ == "__main__":
	main()

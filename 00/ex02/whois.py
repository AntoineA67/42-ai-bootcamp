import sys

def main():
	if len(sys.argv) == 1:
		print("Please provide an argument")
	elif len(sys.argv) > 2:
		print("Too many arguments")
	elif not sys.argv[1].isdigit():
		print(sys.argv[1] + " is not a number")
	else:
		n = int(sys.argv[1])
		print(f'I\'m {"Zero" if n == 0 else "Even" if n % 2 == 0 else "Odd"}')


if __name__ == "__main__":
	main()

import sys

def main():
	if len(sys.argv) < 3:
		print("Please provide two argument")
	elif len(sys.argv) > 3:
		print("Too many arguments")
	elif not sys.argv[1].isdigit():
		print(sys.argv[1] + " is not a number")
	elif not sys.argv[2].isdigit():
		print(sys.argv[2] + " is not a number")
	else:
		a, b = int(sys.argv[1]), int(sys.argv[2])
		print(f'''Sum:		{a + b}
Difference:	{a - b}
Product:	{a * b}
Quotient:	{a / b if b != 0 else "ERROR (division by zero)"}
Remainder:	{a % b if b != 0 else "ERROR (division by zero)"}''')


if __name__ == "__main__":
	main()

from curses.ascii import islower, ispunct, isspace, isupper
import sys

def text_analyzer(s: str) -> None:
	"""
	input: String
	output: String
	Analyze print data about the input string:
		- Number of characters
		- Number of:
			- upper letters
			- lower letters
			- punctuation marks
			- spaces
	"""
	count, f = [0 for i in range(4)], [isupper, islower, ispunct, isspace]
	n = 0
	for letter in s:
		for i in range(4):
			count[i] += 1 if f[i](letter) else 0
		n += 1
	print(f'''The text contains {n} charater{"s" if n > 1 else ""}:
- {count[0]} upper letter{"s" if count[0] > 1 else ""}
- {count[1]} lower letter{"s" if count[1] > 1 else ""}
- {count[2]} punctuation mark{"s" if count[2] > 1 else ""}
- {count[3]} space{"s" if count[3] > 1 else ""}''')



def main():
	if len(sys.argv) == 1:
		s = input("What is the text to analyze ?\n")
	elif len(sys.argv) > 2:
		print("Too many arguments")
		return
	else:
		s = sys.argv[1]
	text_analyzer(s)


if __name__ == "__main__":
	main()

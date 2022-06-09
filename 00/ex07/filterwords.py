from curses.ascii import ispunct
import sys

def main():
	if len(sys.argv) != 3:
		print("Wrong number of arguments")
		return
	elif not sys.argv[2].isdigit():
		print(sys.argv[1] + " is not a number")
		return
	lst = []
	for elem in [word for word in sys.argv[1].split(" ")]:
		w = "".join(l if not ispunct(l) else "" for l in elem)
		if len(w) > int(sys.argv[2]):
			lst.append(w)
	print(lst)

if __name__ == "__main__":
	main()
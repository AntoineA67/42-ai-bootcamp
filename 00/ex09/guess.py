from random import randint

def main():
	print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!""")
	n, c = randint(1, 99), 0
	while 1:
		i = input("\nWhat's your guess between 1 and 99?\n")
		if i == "exit":
			print('Bye!')
			return
		elif not i.isnumeric():
			print('Not a number')
		elif int(i) == n:
			print(f'You got it in {c + 1} tr{"y" if c == 0 else "ies"}, congratulations!')
			return
		else:
			c += 1
			print('Too high!' if int(i) > n else 'Too low!' if int(i) < n else "")



if __name__ == "__main__":
	main()
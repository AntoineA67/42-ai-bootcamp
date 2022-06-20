from requests import head
from csvreader import CsvReader

def main():
	print('' == None)
	good = 'good.csv'
	print(f'Testing {good}')
	with CsvReader(good, header=True) as file:
		data = file.getdata()
		print('\n'.join(' '.join(w for w in l) for l in data) )
		header = file.getheader()
		print(' '.join(header))

	input('\nsucces, enter to continue\n')

	bad = 'bad.csv'
	print(f'\nTesting {bad}')
	with CsvReader(bad) as file:
		if file is None:
			print('File is corrupted')

if __name__ == '__main__':
	main()

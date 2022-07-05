from FileLoader import FileLoader
from ProportionBySport import proportion_by_sport

def main():
	loader = FileLoader()
	data = loader.load('../data/athlete_events.csv')
	print(f"2004, Tennis, F: {proportion_by_sport(data, 2004, 'Tennis', 'F')}")
	print(f"1980, Basket, M: {proportion_by_sport(data, 1980, 'Basketball', 'M')}")

if __name__ == '__main__':
	main()

from FileLoader import FileLoader
from YoungestFellah import youngest_fellah

def main():
	data = FileLoader.load('../data/athlete_events.csv')
	print('2004:', youngest_fellah(data, 2004))
	print('2012:', youngest_fellah(data, 2012))

if __name__ == '__main__':
	main()

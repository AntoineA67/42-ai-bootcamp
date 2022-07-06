from FileLoader import FileLoader
from HowManyMedals import how_many_medals

def main():
	loader = FileLoader()
	data = loader.load("../data/athlete_events.csv")
	print('Kjetil Andr Aamodt', how_many_medals(data, 'Kjetil Andr Aamodt'))
	print('Edgar Lindenau Aabye', how_many_medals(data, 'Edgar Lindenau Aabye'))

if __name__ == '__main__':
	main()

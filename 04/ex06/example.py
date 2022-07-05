from FileLoader import FileLoader
from MyPlotLib import MyPlotLib

def main():
	loader = FileLoader()
	data = loader.load("../data/athlete_events.csv")

if __name__ == '__main__':
	main()

from FileLoader import FileLoader
from MyPlotLib import MyPlotLib

def main():
	loader = FileLoader()
	data = loader.load("../data/athlete_events.csv").drop_duplicates(subset='Name')
	MyPlotLib.histogram(data, ['Height', 'Weight', 'Age'])
	MyPlotLib.density(data, ['Height', 'Weight'])
	MyPlotLib.pair_plot(data, ['Height', 'Weight', 'Age'])
	MyPlotLib.box_plot(data, ['Height', 'Weight'])

if __name__ == '__main__':
	main()

from FileLoader import FileLoader
from Komparator import Komparator

def main():
	loader = FileLoader()
	data = loader.load("../data/athlete_events.csv").drop_duplicates(subset='Name').drop_duplicates(subset='Name')
	komp = Komparator(data)
	komp.compare_box_plots('Sex', 'Weight')
	komp.compare_box_plots('Sex', ['Height', 'Weight'])
	komp.density('Sex', 'Height')
	komp.density('Sex', ['Height', 'Weight'])
	komp.compare_histograms('Sex', 'Weight')
	komp.compare_histograms('Sex', ['Height', 'Weight'])

if __name__ == '__main__':
	main()

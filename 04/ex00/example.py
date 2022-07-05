from FileLoader import FileLoader

def main():
	loader = FileLoader()
	data = loader.load("../data/athlete_events.csv")
	loader.display(data, 12)

if __name__ == '__main__':
	main()

from FileLoader import FileLoader
from SpatioTemporalData import SpatioTemporalData

def main():
	loader = FileLoader()
	data = loader.load("../data/athlete_events.csv")
	sp = SpatioTemporalData(data)
	print(f"Where 1896: {sp.where(1896)}")
	print(f"Where 2016: {sp.where(2016)}")
	print(f"When Athina: {sp.when('Athina')}")
	print(f"When Paris: {sp.when('Paris')}")

if __name__ == '__main__':
	main()

import pandas as pd
import sys

class SpatioTemporalData:
	def __init__(self, df: pd.DataFrame) -> None:
		self.df = df

	def when(self, location: str):
		if type(location) != str:
			print('When: wrong argument', file=sys.stderr)
		return self.df.loc[self.df['City'] == location]['Year'].drop_duplicates().to_list()

	def where(self, date: int):
		if type(date) != int:
			print('Where: wrong argument', file=sys.stderr)
		return self.df.loc[self.df['Year'] == date]['City'].drop_duplicates().to_list()

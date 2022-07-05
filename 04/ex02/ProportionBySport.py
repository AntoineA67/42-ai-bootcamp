import pandas as pd
import sys

def proportion_by_sport(df: pd.DataFrame, year: int, sport: str, gender: str):
	if type(df) != pd.DataFrame or type(year) != int or type(sport) != str or gender not in ['M', 'F']:
		print('proportion_by_sport: invalid arguments', file=sys.stderr)
		return
	
	return len(df.loc[(df['Year'] == year) & (df['Sport'] == sport) & (df['Sex'] == gender)].drop_duplicates(subset='Name', keep='first'))\
		/ len(df.loc[(df['Year'] == year) & (df['Sex'] == gender)].drop_duplicates(subset='Name', keep='first'))

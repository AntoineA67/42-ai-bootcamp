import pandas as pd
import sys

def how_many_medals(df: pd.DataFrame, name: str):
	if type(df) != pd.DataFrame or type(name) != str:
		print('how_many_medals: invalid arguments', file=sys.stderr)
		return
	
	dct = df.loc[(df['Name'] == name)].groupby('Year')['Medal'].apply(list).to_dict()
	for k, v in dct.items():
		dct[k] = {
		'G': len([1 for elem in v if elem == 'Gold']),
		'S': len([1 for elem in v if elem == 'Silver']),
		'B': len([1 for elem in v if elem == 'Bronze'])
		}
	return dct

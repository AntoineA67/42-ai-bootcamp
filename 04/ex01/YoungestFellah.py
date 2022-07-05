import pandas as pd
import sys

def youngest_fellah(df: pd.DataFrame, year: int):
	if type(df) != pd.DataFrame or type(year) != int:
		print('Youngest_felllah: invalid arguments', file=sys.stderr)
		return

	return {'f': df.loc[(df.loc[:, 'Year'] == year) & (df.loc[:, 'Sex'] == 'F'), 'Age'].sort_values(axis=0).iloc[0],\
			'm': df.loc[(df.loc[:, 'Year'] == year) & (df.loc[:, 'Sex'] == 'M'), 'Age'].sort_values(axis=0).iloc[0]}
 
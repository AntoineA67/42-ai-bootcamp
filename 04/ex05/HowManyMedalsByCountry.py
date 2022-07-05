import pandas as pd

def how_many_medals_by_country(df: pd.DataFrame, team: str):
	team_sports = ['Basketball', 'Football',  'Tug-Of-War', 'Badminton', 'Sailing',
                'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh', 'Softball',
                 'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens',
                 'Rugby', 'Lacrosse', 'Polo']

	dct: dict = df.loc[(df['Team'] == team) & (df['Sport'].apply(lambda x: x in team_sports))].dropna().drop_duplicates(subset='Sport').groupby('Year')['Medal'].apply(list).to_dict()
	dct2 = df.loc[(df['Team'] == team) & (df['Sport'].apply(lambda x: x not in team_sports))].dropna().groupby('Year')['Medal'].apply(list).to_dict()

	for k, v in dct2.items():
		if not dct.get(k):
			dct[k] = v
		else:
			dct[k] += v
	for k, v in dct.items():
		dct[k] = {
		'G': len([1 for elem in v if elem == 'Gold']),
		'S': len([1 for elem in v if elem == 'Silver']),
		'B': len([1 for elem in v if elem == 'Bronze'])
		}
	return {k: dct[k] for k in sorted(dct)}

import pandas as pd
from pandas.io.parsers.readers import sys

class FileLoader:
	@staticmethod
	def load(path: str):
		if not path or path == '' or type(path) != str:
			print(f'Invalid path "{path}"', file=sys.stderr)
			return None
		try:
			file: pd.DataFrame = pd.read_csv(path)
		except FileNotFoundError:
			print(f'File not found: "{path}"', file=sys.stderr)
			return
		except FileExistsError:
			print(f'File could not be opened: "{path}"', file=sys.stderr)
			return
		except IsADirectoryError:
			print(f'Path is a directory: "{path}"', file=sys.stderr)
			return
		except PermissionError:
			print(f'Cannot open this file: permission denied: "{path}"', file=sys.stderr)
			return
		print(f'Loading dataset of dimensions {file.shape[0]} x {file.shape[1]}')
		return file

	@staticmethod
	def display(df: pd.DataFrame, n: int):
		if type(n) != int or type(df) != pd.DataFrame:
			print(f'Error: received invalid arguments when displaying dataframe', file=sys.stderr)
			return
		if n > 0:
			print(df.head(n))
		else:
			print(df.tail(-n))

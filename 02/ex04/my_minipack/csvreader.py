from sys import stderr
import sys


class CsvReader:
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0) -> None:
		try:
			self.file = open(filename, 'r')
		except FileNotFoundError:
			print(f'File not found {filename}', file=sys.stderr)
			return
		if sep == '':
			raise ValueError('Separator can not be empty')
		self.file = open(filename, 'r')
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.sep = sep

	def __enter__(self):
		if not hasattr(self, 'file'):
			print('Error: Could not open file', file=sys.stderr)
			return None
		if self.header:
			self.header = self.file.readline().strip('\n').split(self.sep)
		self.data = [line.strip('\n').split(self.sep) for line in self.file]
		l_line = len(self.data[0]) if len(self.data) else 0
		if self.header and len(self.header) != l_line:
			print('Error: wrong header', file=sys.stderr)
			return None
		for line in self.data:
			if len(line) != l_line or '' in line:
				print('Error: all lines have not the same length', file=sys.stderr)
				return None
		return self

	def __exit__(self, type, value, traceback):
		if hasattr(self, 'file') and self.file:
			self.file.close()

	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom.
		Return:
		nested list (list(list, list, ...)) representing the data.
		"""
		return self.data[self.skip_top:-self.skip_bottom if self.skip_bottom else None]

	def getheader(self):
		""" Retrieves the header from csv file.
		Returns:
		list: representing the data (when self.header is True).
		None: (when self.header is False).
		"""
		if not self.header:
			return None
		return self.header

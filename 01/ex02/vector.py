
class Vector:
	def __init__(self, data) -> None:
		if type(data) == int:
			if data < 0:
				raise ValueError('Size should be positive')
			self.values = [[float(i)] for i in range(data)]
			self.shape = (data, 1)
		elif type(data) == tuple:
			if len(data) != 2: raise ValueError('Range should only have start and end values')
			elif type(data[0]) != int or type(data[1]) != int: raise TypeError('Range start and end should be integers')
			elif data[0] > data[1]: raise ValueError('Start should be lower than end')
			self.values = [[float(i)] for i in range(data[0], data[1])]
			self.shape = (data[1] - data[0], 1)
		elif type(data) == list:
			if len(data) == 1:
				if not all(map(lambda x: type(x) == float, data[0])): raise TypeError('All values in a row vector should be floats')
				self.values = [[i for i in data[0]]]
				self.shape = (1, len(data[0]))
			else:
				if not all(map(lambda x: type(x) == list and len(x) == 1 and type(x[0]) == float, data)): raise TypeError('All lists in a column vector should be of length 1 and value inside should be a float')
				self.values = [[i[0]] for i in data]
				self.shape = (len(data), 1)
		else:
			raise TypeError('Type not recognized, please check the doc on how to initialize a vector')
	
	def dot(self, v2:'Vector') -> 'Vector':
		if not isinstance(v2, Vector): raise TypeError('Dot product need another Vector class instance')
		elif v2.shape != self.shape: raise ValueError('Dot product should be done with vectors of same shape')


	def __str__(self) -> str:
		return str(self.values)

	def __repr__(self) -> str:
		return self.__str__()
class Matrix:
	"""Matrix

	Args:
	Matrix can be initialized by:
		- Shape (tuple(int, int)): Creates a matrix of given shape filled with 0.0 : Ex: type(self)((2, 3)) -> type(self)([0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
		- List of lists of floats or integers (list[[float, float], [float, int], ...]) ex: type(self)([[5.0, 2.0], [8.0, 4.0], [9.0, 5]]) => [[5.0, 2.0], [8.0, 4.0], [9.0, 5]]

	Attributes:
		data: List of lists of floats or integers (list[[float, float], [float, int], ...])
		shape: Tuple(m, n)
	"""
	def __init__(self, data) -> None:
		if type(data) == tuple:
			if len(data) != 2: raise ValueError('Shape should have length 2')
			elif type(data[0]) != int or type(data[1]) != int: raise TypeError('Shape should be integers')
			self.data = [[0.0 for _ in range(data[1])] for _ in range(data[0])]
			self.shape = (data[0], data[1])
		elif type(data) == list:
			if not all(map(lambda x: type(x) == list, data)): raise TypeError('Matrix should be a list of lists')
			l = len(data[0]) if len(data) else 0
			for elem in data:
				if not all(map(lambda x: type(x) == float or type(x) == int, elem)): raise TypeError('All values in a matrix should be floats or integers')
				if len(elem) != l: raise ValueError(f'All rows in a matrix should have same length but row `{elem}` has different length')
			self.data = [[float(x) for x in elem] for elem in data]
			self.shape = (len(data), l)
		else:
			raise TypeError('Type not recognized, please check the doc on how to initialize a matrix')

	def T(self):
		return type(self)([[elem[i]  for elem in self.data] for i in range(self.shape[1])])

	def __add__(self, v2):
		if not isinstance(v2, type(self)): raise TypeError(f'Added {type(v2)} should be a {type(self)} class instance')
		elif v2.shape != self.shape: raise ValueError(f'Added {type(self)}s should have the same shape, {self.shape} != {v2.shape}')
		return type(self)([[self.data[j][i] + v2.data[j][i] for i in range(self.shape[1])] for j in range(self.shape[0])])
	
	def __radd__(self, v2):
		return self.__add__(v2)

	def __sub__(self, v2: 'Matrix'):
		if not isinstance(v2, type(self)): raise TypeError(f'Subtracted {type(v2)} should be a {type(self)} class instance')
		elif v2.shape != self.shape: raise ValueError(f'Subtracted {type(self)}s should have the same shape, {self.shape} != {v2.shape}')
		return type(self)([[self.data[j][i] - v2.data[j][i] for i in range(self.shape[1])] for j in range(self.shape[0])])

	def __rsub__(self, v2: 'Matrix'):
		return self.__sub__(v2)

	def __mul__(self, v2):
		if isinstance(v2, (int, float)):
			return type(self)([[x * v2 for x in elem] for elem in self.data])
		if not isinstance(v2, type(self)): raise TypeError(f'Multiplied {type(v2)} should be a {type(self)} class instance')
		elif self.shape != v2.shape and self.shape[1] != v2.shape[0]: raise ValueError(f'Multiplied {type(self)}s should have compatible shapes but have {self.shape} and {v2.shape}')
		print(f'{self.shape} {v2.shape}')
		return type(v2)([[sum(self.data[l][i] * v2.data[i][j] for i in range(self.shape[1])) for j in range(v2.shape[1])] for l in range(self.shape[0])])

	def __rmul__(self, v2):
		return self.__mul__(v2)

	def __truediv__(self, scalar):
		if type(scalar) == Matrix: raise NotImplementedError('Only scalar value should be used')
		if not isinstance(scalar, (int, float)): raise TypeError(f'Scalar should be an integer or a float but is {type(scalar)}')
		if float(scalar) == .0: raise ZeroDivisionError('Division by zero')
		return type(self)([[x / scalar for x in elem] for elem in self.data])

	def __rtruediv__(self, scalar):
		raise NotImplementedError('Division of a scalar by a Matrix is not defined here.')

	def __str__(self) -> str:
		return f'{type(self).__name__}({str(self.data)})'

	def __repr__(self) -> str:
		return self.__str__()
	
	def pretty(self) -> str:
		return f'{chr(10).join(str(x) for x in self.data)}\n'

class Vector(Matrix):
	def __init__(self, data) -> None:
		super().__init__(data)
		if self.shape[0] != 1 and self.shape[1] != 1:
			raise TypeError('All lists in a column vector should be of length 1')

	def dot(self, v2: 'Vector') -> float:
		if not isinstance(v2, Vector): raise TypeError('Dot product need Vector class instance')
		elif v2.shape != self.shape: raise ValueError(f'Dot product should be done with vectors of same shape, {self.shape} != {v2.shape}')
		if self.shape[0] == 1:
			return sum([self.data[0][i] * v2.data[0][i] for i in range(self.shape[1])])
		return sum([self.data[i][0] * v2.data[i][0] for i in range(self.shape[0])])

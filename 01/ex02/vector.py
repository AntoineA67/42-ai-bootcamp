
class Vector:
	"""Row or column vector

	Args:
	Vector can be initialized by:
		- Size (int): Column vector with values from 0.0 (included) to size (excluded). ex: Vector(2) => [[0.0], [1.0]] 
		- Range (tuple(int, int)): Column vector with values from start (included) to end (excluded). Start should be lower than end. ex: Vector(-1, 1) => [[-1.0], [0.0]]
		- List of lists of floats (list[[float], [float], ...]): Column vector. ex: Vector([[5.0], [8.0], [9.0]]) => [[5.0], [8.0], [9.0]]
		- List of list of floats (list[float, float, ...]): Row vector. ex: Vector([[1.0, 10.0]]) => [[1.0, 10.0]]

	Attributes:
		values: List of lists of floats (list[[float], [float], ...]) for column vector or List of list of floats(list[float, float, ...]) for row vector
		shape: (n, 1) for column vector or (1, n) for row vector
	"""
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
	
	def dot(self, v2: 'Vector') -> float:
		if not isinstance(v2, Vector): raise TypeError('Dot product need Vector class instance')
		elif v2.shape != self.shape: raise ValueError(f'Dot product should be done with vectors of same shape, {self.shape} != {v2.shape}')
		if self.shape[0] == 1:
			return sum([self.values[0][i] * v2.values[0][i] for i in range(self.shape[1])])
		return sum([self.values[i][0] * v2.values[i][0] for i in range(self.shape[0])])

	def T(self) -> 'Vector':
		if self.shape[0] == 1:
			return Vector([[i] for i in self.values[0]])
		return Vector([[i[0] for i in self.values]])

	def __add__(self, v2: 'Vector') -> 'Vector':
		if not isinstance(v2, Vector): raise TypeError('Added vector should be a Vector class instance')
		elif v2.shape != self.shape: raise ValueError(f'Added vectors should have the same shape, {self.shape} != {v2.shape}')
		if self.shape[0] == 1:
			return Vector([[self.values[0][i] + v2.values[0][i] for i in range(self.shape[1])]])
		return Vector([[self.values[i][0] + v2.values[i][0]] for i in range(self.shape[0])])
	
	def __radd__(self, v2: 'Vector') -> 'Vector':
		return self.__add__(v2)

	def __sub__(self, v2: 'Vector') -> 'Vector':
		if not isinstance(v2, Vector): raise TypeError('Subtracted vector should be a Vector class instance')
		elif v2.shape != self.shape: raise ValueError(f'Subtracted vectors should have the same shape, {self.shape} != {v2.shape}')
		if self.shape[0] == 1:
			return Vector([[self.values[0][i] - v2.values[0][i] for i in range(self.shape[1])]])
		return Vector([[self.values[i][0] - v2.values[i][0]] for i in range(self.shape[0])])

	def __rsub__(self, v2: 'Vector') -> 'Vector':
		return self.__sub__(v2)

	def __mul__(self, scalar) -> 'Vector':
		if type(scalar) == Vector: raise NotImplementedError('Only scalar value should be used')
		if not isinstance(scalar, (int, float)): raise TypeError(f'Scalar should be an integer or a float but is {type(scalar)}')
		if self.shape[0] == 1:
			return Vector([[self.values[0][i] * float(scalar) for i in range(self.shape[1])]])
		return Vector([[self.values[i][0] * float(scalar)] for i in range(self.shape[0])])

	def __rmul__(self, scalar) -> 'Vector':
		return self.__mul__(scalar)

	def __truediv__(self, scalar) -> 'Vector':
		if type(scalar) == Vector: raise NotImplementedError('Only scalar value should be used')
		if not isinstance(scalar, (int, float)): raise TypeError(f'Scalar should be an integer or a float but is {type(scalar)}')
		if float(scalar) == .0: raise ZeroDivisionError('Division by zero')
		if self.shape[0] == 1:
			return Vector([[self.values[0][i] / float(scalar) for i in range(self.shape[1])]])
		return Vector([[self.values[i][0] / float(scalar)] for i in range(self.shape[0])])

	def __rtruediv__(self, scalar) -> 'Vector':
		raise NotImplementedError('Division of a scalar by a Vector is not defined here.')

	def __str__(self) -> str:
		return f'Vector({str(self.values)})'

	def __repr__(self) -> str:
		return self.__str__()
import numpy as np

class NumpyCreator:
	def __init__(self) -> None:
		pass

	def from_list(self, lst, dtype=None):
		return np.array(lst, dtype=dtype) if np.asarray(lst, dtype=dtype).dtype != object and type(lst) == list else None

	def from_tuple(self, tpl, dtype=None):
		return np.array(tpl, dtype=dtype) if np.asarray(tpl, dtype=dtype).dtype != object and type(tpl) == tuple else None

	def from_iterable(self, itr, dtype=None):
		return np.fromiter(itr, dtype=dtype) if np.asarray(itr, dtype=dtype).dtype != object else None

	def from_shape(self, shape, value=0, dtype=int):
		return np.full(shape, value, dtype=dtype)

	def random(self, shape, dtype=float):
		return np.random.rand(*shape) if dtype == float else np.random.randint(shape) if dtype == int else None

	def identity(self, n, dtype=float):
		return np.identity(n, dtype=dtype)

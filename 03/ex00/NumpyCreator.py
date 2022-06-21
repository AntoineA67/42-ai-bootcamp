import numpy as np

class NumpyCreator:
	def __init__(self) -> None:
		pass

	def from_list(self, lst, dtype=None):
		return np.array(lst, dtype=dtype) if np.asarray(lst, dtype=dtype).dtype != object else None

	def from_tuple(self, tpl, dtype=None):
		pass

	def from_iterable(self, itr, dtype=None):
		pass

	def from_shape(self, shape, value, dtype=None):
		pass

	def random(self, shape, dtype=None):
		pass

	def identity(self, n, dtype=float):
		pass


npc = NumpyCreator()
print(npc.from_list([[1,2,3],[6,3,4]]))

print(npc.from_list([[1,2,3],[6,4]]))
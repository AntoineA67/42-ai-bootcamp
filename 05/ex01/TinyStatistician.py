import numpy as np

class TinyStatistician:
	@staticmethod
	def mean(x: np.ndarray):
		if (type(x) != np.ndarray and type(x) != list) or len(x) == 0: return None
		n = 0
		for i in x:
			n += i
		return n / len(x)

	@staticmethod
	def median(x: np.ndarray):
		if (type(x) != np.ndarray and type(x) != list) or len(x) == 0: return None
		x1 = sorted(x)
		if len(x1) % 2 == 0:
			return (x1[len(x1) // 2 - 1] + x1[len(x1) // 2]) / 2
		return float(x1[len(x1) // 2])

	@staticmethod
	def quartile(x: np.ndarray):
		if (type(x) != np.ndarray and type(x) != list) or len(x) == 0: return None
		return [TinyStatistician.median(np.array(sorted(x)[:(len(x) + 1) // 2])), TinyStatistician.median(np.array(sorted(x)[len(x) // 2:]))]


	@staticmethod
	def percentile(x: np.ndarray, p):
		if (type(x) != np.ndarray and type(x) != list) or (type(p) != int and type(p) != float) or len(x) == 0 or p > 100 or p < 0: return None		
		x1 = sorted(x)
		if p == 100:
			return x1[-1]
		k: float = (p / 100) * (len(x1) - 1)
		ki, kf = int(k), k % 1
		return x1[ki] + kf * (x1[ki + 1] - x1[ki])

	@staticmethod
	def var(x: np.ndarray):
		if (type(x) != np.ndarray and type(x) != list) or len(x) == 0: return None
		var, m = 0.0, TinyStatistician.mean(x)
		for n in x:
			var += pow(n - m, 2)
		return var / len(x)

	@staticmethod
	def std(x: np.ndarray):
		if (type(x) != np.ndarray and type(x) != list) or len(x) == 0: return None
		std, m = 0.0, TinyStatistician.mean(x)
		for n in x:
			std += pow(n - m, 2)
		return np.sqrt(std / len(x))

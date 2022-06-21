from numpy import sqrt

class TinyStatistician:
	@staticmethod
	def mean(x):
		mean = 0.0
		for n in x:
			mean += n
		return mean / len(x) if len(x) > 0 else None

	@staticmethod
	def median(x):
		return float((sorted(x)[len(x) // 2]) if (len(x) % 2 == 1) else ((sorted(x)[(len(x) - 1) // 2] + sorted(x)[len(x) // 2]) / 2)) if len(x) > 0 else None

	@staticmethod
	def quartiles(x):
		return [TinyStatistician.median(sorted(x)[:(len(x) + 1) // 2]), TinyStatistician.median(sorted(x)[len(x) // 2:])] if len(x) > 0 else None

	@staticmethod
	def var(x):
		var, m = 0.0, TinyStatistician.mean(x)
		for n in x:
			var += pow(n - m, 2)
		return float(var / len(x)) if len(x) > 0 else None

	@staticmethod
	def std(x):
		std, m = 0.0, TinyStatistician.mean(x)
		for n in x:
			std += pow(n - m, 2)
		return float(sqrt(std / len(x))) if len(x) > 0 else None
class TinyStatistician:
	def mean(self, x):
		mean = 0.0
		for n in x:
			mean += n
		return mean / len(x) if len(x) > 0 else None

	def median(self, x):
		return float((sorted(x)[len(x) // 2]) if (len(x) % 2 == 1) else ((sorted(x)[(len(x) - 1) // 2] + sorted(x)[len(x) // 2]) / 2)) if len(x) > 0 else None

	def quartiles(self, x):
		return [self.median(sorted(x)[:(len(x) + 1) // 2]), self.median(sorted(x)[len(x) // 2:])] if len(x) > 0 else None

	def var(self, x):
		var, m = 0.0, self.mean(x)
		for n in x:
			var += pow(n - m, 2)
		return float(var / len(x)) if len(x) > 0 else None

	def std(self, x):
		pass
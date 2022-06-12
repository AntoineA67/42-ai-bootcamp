class Evaluator:
	@staticmethod
	def check(coefs:list, words:list)-> int:
		if type(coefs) != list or not all(map(lambda x: isinstance(x, float), coefs)): raise TypeError('Coefs should be a list of floats')
		if type(words) != list or not all(map(lambda x: isinstance(x, str), words)): raise TypeError('Words should be a list of strings')
		if len(coefs) != len(words): return -1

	@classmethod
	def zip_evaluate(cls, coefs:list, words:list):
		if cls.check(coefs, words) == -1: return -1
		return sum([x[0] * x[1] for x in zip(coefs, [len(word) for word in words])])

	@classmethod
	def enumerate_evaluate(cls, coefs:list, words: list):
		if cls.check(coefs, words) == -1: return -1
		return sum([coefs[i] * len(word) for i, word in enumerate(words)])

	@classmethod
	def bonus_evaluate(cls, coefs:list, words: list):
		if cls.check(coefs, words) == -1: return -1
		return sum([len(words[i]) * coefs[i] for i in range(len(coefs))])


def main():
	words = ["Le", "Lorem", "Ipsum", "est", "simple"]
	coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
	print(Evaluator.zip_evaluate(coefs, words))

if __name__ == "__main__":
	main()
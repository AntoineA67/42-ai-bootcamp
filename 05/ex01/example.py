import numpy as np
from TinyStatistician import TinyStatistician

def main():
	a = np.array([1.0, 2.0, 3.0, 4.0])
	a2 = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
	print(f'a: {a}\na2: {a2}')
	print(f'mean a: {TinyStatistician.mean(a)}\nmean a2: {TinyStatistician.mean(a2)}')
	print(f'median a: {TinyStatistician.median(a)}\nmedian a2: {TinyStatistician.median(a2)}')
	print(f'quartile a: {TinyStatistician.quartile(a)}\nquartile a2: {TinyStatistician.quartile(a2)}')
	a, a2 = np.arange(99), np.arange(100)
	print(f'a: {a}\na2: {a2}')
	print(f'40th percentile a: {TinyStatistician.percentile(a, 40)}\n40th percentile a2: {TinyStatistician.percentile(a2, 40)}')
	print(f'40th percentile a: {TinyStatistician.percentile(a, 100)}\n40th percentile a2: {TinyStatistician.percentile(a2, 0)}')
	print(f'var a: {TinyStatistician.var(a)}\nvar a2: {TinyStatistician.var(a2)}')
	print(f'std a: {TinyStatistician.std(a)}\nstd a2: {TinyStatistician.std(a2)}')

if __name__ == '__main__':
	main()

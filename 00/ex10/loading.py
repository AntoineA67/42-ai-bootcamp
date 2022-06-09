from time import sleep


def ft_progress(lst):
	for i in lst:
		print(f"\r{i} / {len(lst)} {'.' * int(100 * (i + 1) / len(lst))}", end='')
		yield i


listy = range(8000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	sleep(0.01)
print()
print(ret)
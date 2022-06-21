from time import sleep, time

def ft_progress(lst):
	start = time()
	for i in lst:
		m, s, ms = int((time() - start) / 60), int(time() - start) % 60, int((time() - start) * 10)  % 10
		eta = (time() - start) * len(lst) / (i + 1) - (time() - start)
		print(f"\r{(str(m) + 'm ' if m > 0 else '') + str(s).zfill(2) + ('.' + str(ms) if not m else '') + 's':^9} \
{str(i + 1) + '/' + str(len(lst)):^10} \
{'{'}{'=' + '=' * int(20 * (i + 1) / len(lst)) + ('>' if int(20 * (i + 1) / len(lst)) < 20 else ''):21}{'}'} \
{'ETA: ' + (str(int(eta / 60)).zfill(2) + 'm' if int(eta / 60) > 0 else '') + str(int(eta % 60)).zfill(2) + 's' if i != len(lst) - 1 else 'Finished':^10} \
{str(int(i / len(lst) * 100)) + '%' if i < len(lst) - 1 else '':^5}", end='')
		yield i


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	sleep(.01)
print()
print(ret)
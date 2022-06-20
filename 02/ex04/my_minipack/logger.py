import time
import os

def log(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		r = func(*args, **kwargs)
		with open('./machine.log', 'a') as log_file:
			n = time.time() - start
			log_file.write(f'({os.environ["USER"]})Running: {func.__name__.replace("_", " ").title():<19}[ exec-time = {n * (1000 if n < 1 else 1):.3f} {"ms" if n < 1 else "s"} ]\n')
			log_file.close()
		return r

	return wrapper

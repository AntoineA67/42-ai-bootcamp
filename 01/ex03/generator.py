from random import randint

def generator(text:str, sep:str=' ', option=None):
	"""
	Splits the text according to sep value and yield the substrings.
	Option precise if a action is performed to the substrings before it is yielded.
	"""
	if type(text) != str or type(sep) != str or not option in [None, 'shuffle', 'unique', 'ordered']: return 'ERROR'
	splitted = text.split(sep=sep)
	if option == 'ordered':
		splitted.sort()
	elif option == 'unique':
		splitted = list(dict.fromkeys(splitted))
	elif option == 'shuffle':
		for i in range(len(splitted)):
			r = randint(i, len(splitted) - 1)
			splitted[r], splitted[i] = splitted[i], splitted[r] 
	for word in splitted:
		yield word

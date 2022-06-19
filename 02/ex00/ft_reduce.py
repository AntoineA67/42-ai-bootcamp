def ft_reduce(function_to_apply, iterable):
	"""Apply function of two arguments cumulatively.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	A value, of same type of elements in the iterable parameter.
	None if the iterable can not be used by the function.
	"""
	try:
		iter(iterable)
	except TypeError:
		raise TypeError(f"Given iterable of type '{type(iterable).__name__}' does not support iteration")
	if len(iterable) < 1:
		raise TypeError('ft_reduce() with empty sequence')
	acc = next(iter(iterable))
	for elem in iterable[1:]:
		acc = function_to_apply(acc, elem)
	return acc
	
from vector import Vector

def main():
	gen = 4
	v1 = Vector(gen)
	print(f'V1: {gen}:\n  {v1}\n  {v1.shape}\n')

	gen = (-1, 4)
	v2 = Vector(gen)
	print(f'V2: {gen}:\n  {v2}\n  {v2.shape}\n')

	gen = [[.1, .2, .5]]
	v3 = Vector(gen)
	print(f'V3: {gen}:\n  {v3}\n  {v3.shape}\n')

	gen = [[.4], [.6], [.8]]
	v4 = Vector(gen)
	print(f'V4: {gen}:\n  {v4}\n  {v4.shape}\n')


if __name__ == '__main__':
	main()
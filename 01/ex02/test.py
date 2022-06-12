from vector import Vector

def main():
	gen = 4
	v1 = Vector(gen)
	print(f'V1: {gen}:\n  {v1}\n  {v1.shape}\n')

	gen = (-1, 3)
	v2 = Vector(gen)
	print(f'V2: {gen}:\n  {v2}\n  {v2.shape}\n')

	gen = [[1.0, 2.0, 5.0]]
	v3 = Vector(gen)
	print(f'V3: {gen}:\n  {v3}\n  {v3.shape}\n')

	gen = [[.4, .6, .8]]
	v4 = Vector(gen)
	print(f'V4: {gen}:\n  {v4}\n  {v4.shape}\n')

	print(f'Dot product: {v1} ⋅ {v2} => {v1.dot(v2)}')
	print(f'Dot product: {v3} ⋅ {v4} => {v3.dot(v4)}\n')

	print(f'Transposition: {v1} => {v1.T()}\n')
	print(f'Transposition: {v3} => {v3.T()}\n\n')

	print(f'Addition:\n	{v1}\n+	{v2}\n=	{v1 + v2}\n')
	print(f'Addition:\n	{v3}\n+	{v4}\n=	{v3 + v4}\n\n')

	print(f'Subtraction:\n	{v1}\n-	{v2}\n=	{v1 - v2}')
	print(f'Subtraction:\n	{v3}\n-	{v4}\n=	{v3 - v4}\n')

	print(f'Multiplication:\n	{v1}\n*	5\n=	{5 * v1}\n')
	print(f'Multiplication:\n	{v3}\n*	.2\n=	{v3 * .2}\n\n')

	print(f'Division:\n	{v1}\n/	5\n=	{v1 / 5}\n')
	print(f'Division:\n	{v3}\n/	.2\n=	{v3 / .2}\n\n')

if __name__ == '__main__':
	main()
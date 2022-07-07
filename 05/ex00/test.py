from matrix import Matrix, Vector

def main():

	m0 = Matrix((5, 2))
	print(f'm0:\n{m0.pretty()}\n')
	m1 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
	print(f'm1.shape:\n{m1.shape}\n')
		# Output:
		# (3, 2)
	print(f'm1:\n{m1.pretty()}\n')
	print(f'm1.T():\n{m1.T().pretty()}\n')
		# Output:
		# Matrix([[0., 2., 4.], [1., 3., 5.]])
	print(f'm1.T().shape:\n{m1.T().shape}\n')
		# Output:
		# (2, 3)

	m2 = Matrix([[0., 2., 4.], [1., 3., 5.]])
	print(f'm2.shape:\n{m2.shape}\n')
		# Output:
		# (2, 3)
	print(f'm2:\n{m2.pretty()}\n')
	print(f'm2.T():\n{m2.T().pretty()}\n')
		# Output:
		# Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
	print(f'm2.T().shape:\n{m2.T().shape}\n')
		# Output:
		# (3, 2)

	m3 = Matrix([[0.0, 2.0, 4.0],
				 [8.0, 10.0, 12.0]])
	m4 = Matrix([[1.0, 3.0],
				 [5.0, 7.0],
				 [9.0, 11.0]])
	print(f'm3:\n{m3.pretty()}\n')
	print(f'm4:\n{m4.pretty()}\n')
	print(f'm4.T() + m3:\n{(m4.T() + m3).pretty()}\n')
	print(f'm4.T() - m3:\n{(m4.T() - m3).pretty()}\n')
	print(f'm3 * 2.0:\n{(m3 * 2.0).pretty()}\n')
	print(f'm3 * m4:\n{(m3 * m4).pretty()}\n')
		# Output:
		# Matrix([[28., 34.], [56., 68.]])

	m5 = Matrix([[0.0, 1.0, 2.0],
				 [0.0, 2.0, 4.0]])
	v1 = Vector([[1], [2], [3]])
	print(f'm5:\n{m5.pretty()}\n')
	print(f'v1:\n{v1.pretty()}\n')
	print(f'm5 * v1:\n{(m5 * v1).pretty()}\n')
		# Output:
		# Matrix([[8], [16]])
		# Or: Vector([[8], [16]

	v2 = Vector([[1], [2], [3]])
	v3 = Vector([[2], [4], [8]])
	print(f'v2:\n{v2.pretty()}\n')
	print(f'v3:\n{v3.pretty()}\n')
	print(f'v2 + v3:\n{(v2 + v3).pretty()}\n')
		# Output:
		# Vector([[3],[6],[11]])

if __name__ == '__main__':
	main()

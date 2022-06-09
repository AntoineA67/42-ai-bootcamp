kata = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
}

print(f'{chr(10).join([name + " was created by " +  creator for name, creator in kata.items()])}')

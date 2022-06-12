class Recipe:
	def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, recipe_type: str, description: str = '') -> None:
			if type(name) != str: raise TypeError('Name should be a string')
			if cooking_lvl not in range(1, 6): raise TypeError('Cooking level should be a number between 1 and 5')
			if type(cooking_time) != int or cooking_time < 0: raise TypeError('Cooking time should be a positive number')
			if type(ingredients) != list or any(map(lambda x: type(x) == str, ingredients)) is False: raise TypeError('Ingredients should be a list of strings')
			if recipe_type not in ['starter', 'lunch', 'dessert'] != str: raise TypeError('Recipe type should be either starter, lunch or dessert')
			if type(description) != str: raise TypeError('Description should be a string')
			self.name = name
			self.cooking_lvl = cooking_lvl
			self.cooking_time = cooking_time
			self.ingredients = ingredients
			self.description = description
			self.recipe_type = recipe_type
	def __str__(self) -> str:
		"""
		Return the string to print with the recipe info
		"""
		return f'{"-" * 20}\n{self.name.capitalize()} {"*" * self.cooking_lvl}/5\n\nIngredient{"s" if len(self.ingredients) > 1 else ""}:\n{"  - " + (chr(10) + "  - ").join(self.ingredients)}\n\nDescription:\n{self.description}\n\nPrep time: {self.cooking_time}m\nUsually eaten as {self.recipe_type}\n{"-" * 20}\n\n'

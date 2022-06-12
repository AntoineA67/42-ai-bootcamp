from datetime import datetime
from recipe import Recipe

class Book:
	def __init__(self, name: str) -> None:
		if type(name) != str: raise TypeError('Name should be a string')
		self.name = name
		self.creation_date = datetime.now()
		self.last_update = self.creation_date
		self.recipes_list = {'starter': [], 'lunch': [], 'dessert': []}


	def get_recipe_by_name(self, name: str) -> Recipe:
		"""
		Prints a recipe with the name text{name} and returns the instance
		"""
		if type(name) != str: raise TypeError('Name should be a string when searching for a recipe by name')
		for type_list in self.recipes_list.values():
			for recipe in type_list:
				if recipe.name == name:
					print(recipe)
					return recipe
		print(f'Recipe not found: "{name}"')
		return None


	def get_recipes_by_types(self, recipe_type: str) -> list:
		"""
		Get all recipe names for a given recipe_type
		"""
		if type(recipe_type) != str: raise TypeError('Type should be a string when searching for a recipe by type')
		if recipe_type not in ['starter', 'lunch', 'dessert']: raise ValueError('Recipe type should be either starter, lunch or dessert')
		return self.recipes_list.get(recipe_type)
		


	def add_recipe(self, recipe: Recipe) -> None:
		"""
		Add a recipe to the book and update last_update
		"""
		if type(recipe) != Recipe: raise TypeError('Recipe type should be from Recipe class type when adding a recipe')
		if recipe in self.recipes_list.get(recipe.recipe_type):
			if input('Recipe already in book, do you want to overwrite it ? (n to cancel)') == 'n': return
		self.recipes_list.get(recipe.recipe_type).append(recipe)
		self.last_update = datetime.now()


from book import Book
from recipe import Recipe

def main():
	book = Book('My Recipe Book')
	gato = Recipe("Gato", 4, 8, ["chaukola", "des e", "dulai"], "dessert", "c du bon gato o choquolas")
	duri = Recipe("Duri", 4, 8, ["ri", "delo", "dusel"], "lunch", "C du riz")

	print(gato)

	book.add_recipe(gato)
	book.add_recipe(duri)
	print(', '.join(recipe.__str__() for recipe in book.get_recipes_by_types('lunch')))
	book.get_recipe_by_name("Duri")
	book.get_recipe_by_name('non')

if __name__ == '__main__':
	main()
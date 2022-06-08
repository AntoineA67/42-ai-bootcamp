from curses.ascii import isdigit


cookbook = {
	"Sandwich": {
		"ingredients": ["ham", "bread", "cheese", "tomatoes"],
		"meal": "lunch",
		"prep_time": 10
	},
	"Oui": {
		"ingredients": ["non", "oui-oui", "peut-etre"],
		"meal": "non-non",
		"prep_time": 56155
	}
}

print(cookbook)

def printAllRecipeNames():
	print("\n".join(r for r in cookbook))


def printRecipe(recipe:str):
	r = cookbook.get(recipe)
	if r and type(r) == dict:
		print(f'''Ingredients: {r.get("Ingredients")}
To be eaten for {r.get("Meal")}.
Takes {r.get("prep_time")} of cooking.''')
	else:
		print("Recipe not found")


def deleteRecipe(recipe:str):
	print(f'Removed {recipe}' if cookbook.pop(recipe, False) else "Recipe not found")


def addRecipe():
	r, name = {'ingredients': []}, input("Enter recipe name:\n")
	if cookbook.get(name):
		if input("Warning: already existing recipe, do you want to overwrite it ? (n to cancel)") == "n":
			return
	print("Enter ingredients list:")
	i = "oui"
	while i:
		i = input("\n	->")
		r['ingredients'].append(i)
	r['meal'] = input("\nEnter a meal type:\n")
	r['prep_time'] = input("Enter a preparation time:\n")
	cookbook[name] = r


def main():
	options = ["Add a recipe", "Delete a recipe", "Print a recipe", "Print the cookbook", "Quit"]
	optionsStr = "\n".join(options)
	print('Welcome to the Python Cookbook !')
	print(optionsStr)
	i = 0
	while i != 5:
		i = input("Select an option:")
		if not i.isdigit() or int(i) not in range(1, 6):
			print("This option does not exist\n")
			print(optionsStr)
			continue
		i = int(i)
		if i == 1:
			addRecipe()
		elif i == 2:
			deleteRecipe(input("Delete recipe: "))
		elif i == 3:
			printRecipe(input("Print a recipe: "))
		elif i == 4:
			printAllRecipeNames()
		
		


if __name__ == "__main__":
	main()
from colorama import init, Fore as fg

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

def printAllRecipeNames():
	print(fg.CYAN + "\nShowing all recipes:\n" + fg.GREEN + "\n".join(r for r in cookbook) + "\n")


def printRecipe(recipe:str):
	r = cookbook.get(recipe)
	if r and type(r) == dict:
		print(fg.GREEN + f'''
Ingredients: {(chr(10) + "	➜ ").join(r.get("ingredients"))}
To be eaten for {r.get("meal")}.
Takes {r.get("prep_time")} minutes of cooking.
''' + fg.RESET)
	else:
		print("Recipe not found")


def deleteRecipe(recipe:str):
	print(f'\nRemoved {recipe}\n' if cookbook.pop(recipe, False) else "\nRecipe not found\n")


def addRecipe():
	r, name = {'ingredients': []}, input(fg.GREEN + "\nEnter recipe name:\n" + fg.RESET)
	if cookbook.get(name):
		if input(fg.YELLOW + "Warning: already existing recipe, do you want to overwrite it ? (n to cancel)") == "n":
			return
	print(fg.GREEN + "Enter ingredients list:")
	i = "oui"
	while i:
		i = input("->")
		r['ingredients'].append(i)
	r['meal'] = input(fg.GREEN + "\nEnter a meal type:\n" + fg.RESET)
	r['prep_time'] = input(fg.GREEN + "Enter a preparation time:\n" + fg.RESET)
	cookbook[name] = r
	print()


def main():
	init(autoreset=True)
	options = ["Add a recipe", "Delete a recipe", "Print a recipe", "Print the cookbook", "Quit"]
	optionsStr = fg.LIGHTCYAN_EX + "\n".join([str(i + 1) + ": " + options[i] for i in range(len(options))]) + "\n" + fg.RESET
	print(fg.MAGENTA + '\nWelcome to the Python Cookbook !\n')
	print(optionsStr)
	i = 0
	while i != 5:
		i = input(fg.LIGHTBLUE_EX + "Select an option:" + fg.RESET)
		if not i.isdigit() or int(i) not in range(1, 6):
			print(fg.YELLOW + "This option does not exist\n" + fg.RESET)
			print(optionsStr)
			continue
		i = int(i)
		if i == 1:
			addRecipe()
		elif i == 2:
			deleteRecipe(input(fg.GREEN + "Delete recipe: " + fg.RESET))
		elif i == 3:
			printRecipe(input(fg.GREEN + "Print a recipe: " + fg.RESET))
		elif i == 4:
			printAllRecipeNames()


if __name__ == "__main__":
	main()

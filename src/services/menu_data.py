# Req 3
import csv

from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path):
        # Initializes sets to store dishes
        self.dishes = set()
        # Load menu data from the specified source file
        self.load_menu_data(source_path)

    def load_menu_data(self, source_path):
        # Opens the CSV file containing the menu data
        with open(source_path, newline="") as csvfile:
            # Creates a reader object to read the CSV file
            reader = csv.DictReader(csvfile)
            # Creates a dictionary to store dishes
            dishes = {}
            # Iterates over each row in the CSV file
            for index in reader:
                # Extracts dish name, price, ingredient,
                #  and recipe amount from the row
                dish_name = index["dish"]
                price = float(index["price"])
                ingredient_name = index["ingredient"]
                recipe_amount = int(index["recipe_amount"])

                # Checks if the dish already exists in the dishes dictionary
                dish = dishes.get(dish_name)
                if dish is None:
                    # If the dish doesn't exist, creates a new Dish object
                    dish = Dish(dish_name, price)
                    dishes[dish_name] = dish
                    # Adds the dish to the set of dishes in the MenuData object
                    self.dishes.add(dish)
                # Creates a new Ingredient object for the ingredient in the row
                ingredient = Ingredient(ingredient_name)
                # Adds the ingredient and recipe amount to the dish's recipe
                dish.add_ingredient_dependency(ingredient, recipe_amount)

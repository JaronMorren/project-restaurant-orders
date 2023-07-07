from csv import DictReader
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1
    def check_recipe_availability(self, recipe: Recipe) -> bool:
        # Iterates over each ingredient and its required amount in the recipe
        for ingredient, amount in recipe.items():
            # Checks if the ingredient is not in the inventory
            #  or the available amount is less than the required amount
            if (
                ingredient not in self.inventory
                or self.inventory[ingredient] < amount
            ):
                # Returns False if any ingredient
                #  is unavailable or insufficient
                return False
        # If all ingredients are available in sufficient amounts, return True
        return True

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        # Checks if the recipe is available in the inventory
        if not self.check_recipe_availability(recipe):
            # Raises a ValueError if the recipe is not available
            raise ValueError("Recipe is not available")

        # Iterates over each ingredient and its required amount in the recipe
        for ingredient, amount in recipe.items():
            # Subtracts the required amount
            # of each ingredient from the inventory
            self.inventory[ingredient] -= amount

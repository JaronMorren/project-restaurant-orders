from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        # Creates an empty list to store the menu items
        main_menu = [
            {
                "dish_name": dish.name,
                # Stores the name of the dish
                "ingredients": dish.get_ingredients(),
                # Stores the ingredients of the dish
                "price": dish.price,
                # Stores the price of the dish
                "restrictions": dish.get_restrictions(),
                # Stores the dietary restrictions of the dish
            }
            for dish in self.menu_data.dishes
            # Iterates over each dish in the menu_data
            if (
                restriction is None
                # If no dietary restriction is specified
                or restriction not in dish.get_restrictions()
                # or the dish does not have the specified restriction
            )
            and all(
                self.inventory.inventory.get(ingredient, 0) > 0
                # Check if each ingredient in the dish
                #  is available in the inventory
                for ingredient in dish.get_ingredients()
                # Iterates over each ingredient in the dish
            )
        ]
        # Returns the main menu list
        return main_menu

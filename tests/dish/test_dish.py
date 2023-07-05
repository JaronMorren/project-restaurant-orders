from models.ingredient import Ingredient
import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501


# Req 2
def test_dish():
    # test  valid dish creation:
    dish = Dish("Pizza", 14.99)
    assert dish.name == "Pizza"
    assert dish.price == 14.99

    # test dish creation with invalid price type:
    with pytest.raises(TypeError):
        Dish("Burger", "8.99")

    # test dish creation with invalid price value:
    with pytest.raises(ValueError):
        Dish("Salad", -13.99)

    # test dish representation:
    dish = Dish("Spaghetti", 15.5)
    assert repr(dish) == "Dish('Spaghetti', R$15.50)"

    # test dish equality:
    dish1 = Dish("Cake", 15.99)
    dish2 = Dish("Cake", 15.99)
    assert dish1 == dish2

    # test dish hash:
    dish1 = Dish("Salmon", 19.99)
    dish2 = Dish("Salmon", 19.99)
    dish3 = Dish("Tuna", 19.99)
    assert hash(dish1) == hash(dish2)
    assert hash(dish1) != hash(dish3)

    # test add ingredient dependency:
    dish = Dish("Soup", 5.99)
    ingredient1 = Ingredient("Carrots")
    ingredient2 = Ingredient("Onions")
    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 1)
    assert dish.recipe == {ingredient1: 2, ingredient2: 1}

    # test get ingredients method:
    expected_ingredients = {ingredient1, ingredient2}
    assert dish.get_ingredients() == expected_ingredients

    # test get restrictions method:
    dish = Dish("Burger", 8.99)
    ingredient1 = Ingredient("Beef")
    ingredient2 = Ingredient("Cheese")
    ingredient3 = Ingredient("Lettuce")
    ingredient4 = Ingredient("Tomato")
    ingredient1.restrictions = {"Animal Meat", "Animal Derived"}
    ingredient2.restrictions = {"Lactose", "Animal Derived"}
    dish.add_ingredient_dependency(ingredient1, 1)
    dish.add_ingredient_dependency(ingredient2, 1)
    dish.add_ingredient_dependency(ingredient3, 1)
    dish.add_ingredient_dependency(ingredient4, 1)
    assert dish.get_restrictions() == {
        "Animal Meat",
        "Animal Derived",
        "Lactose",
    }

from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():

    ## test hash equality:
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("camarão")
    assert hash(ingredient1) == hash(ingredient1)
    assert hash(ingredient2) == hash("camarão")

    ## test ingredient equality:
    ingredient1 = Ingredient("farinha")
    assert ingredient1 == ingredient1
    assert ingredient1 != ingredient2

    ## test ingredient repr method:
    ingredient = Ingredient("farinha")
    assert repr(ingredient) == "Ingredient('farinha')"
    
    ## test ingredient restrictions:
    ingredient2_restrictions = {
            Restriction.ANIMAL_MEAT,
            Restriction.SEAFOOD,
            Restriction.ANIMAL_DERIVED,
        }
    assert ingredient2.name == "camarão"
    assert ingredient2.restrictions == ingredient2_restrictions

   

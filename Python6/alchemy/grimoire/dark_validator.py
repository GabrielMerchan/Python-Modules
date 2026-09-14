from .dark_spellbook import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    val_ing = dark_spell_allowed_ingredients()
    ing = ingredients.split()
    result = "INVALID"
    for i in ing:
        if i in val_ing:
            result = "VALID"
    ingredients = ingredients + " - " + result
    return ingredients
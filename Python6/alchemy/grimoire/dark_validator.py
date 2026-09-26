from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    val_ing = dark_spell_allowed_ingredients()
    result = "INVALID"
    for i in val_ing:
        if i in ingredients.lower():
            result = "VALID"
    ingredients = ingredients + " - " + result
    return ingredients

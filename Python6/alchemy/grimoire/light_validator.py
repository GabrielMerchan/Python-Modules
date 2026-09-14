from .light_spellbook import light_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    val_ing = light_spell_allowed_ingredients()
    ing = ingredients.split()
    result = "INVALID"
    for i in val_ing:
        if i in ingredients.lower():
            result = "VALID"
    return f'{ingredients} - {result}'
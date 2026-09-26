def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    ing = validate_ingredients(ingredients)
    val = ing.split()
    if "VALID" in val:
        return (f'Spell recorded: {spell_name} ({ing})')
    else:
        return (f'Spell rejected: {spell_name} ({ing})')

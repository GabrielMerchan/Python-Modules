from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:

    ing = validate_ingredients(ingredients)
    ing_lst = ing.split()
    if "VALID" in ing_lst:
        return (f"Spell recorded: {spell_name} ({ing})")
    else:
        return (f"Spell rejected: {spell_name} ({ing})")

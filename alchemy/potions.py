from .elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion() -> str:
    str = f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"
    return str


def strength_potion() -> str:
    str = (f"Strength potion brewed with '{create_fire()}' "
           f"and '{create_water()}'")
    return str

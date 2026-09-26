from ..potions import strength_potion
from ..elements import create_air
import elements


def lead_to_gold() -> str:
    str = (f"Recipe transmuting Lead to Gold: brew '{create_air()}' "
           f"and '{strength_potion()}' mixed with '{elements.create_fire()}'")
    return str

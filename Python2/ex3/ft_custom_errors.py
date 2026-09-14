#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, err: str = "Unknown plant error"):
        super().__init__(err)


class PlantError(GardenError):
    def __init__(self, err: str = "Unknown plant error"):
        super().__init__(err)


class WaterError(GardenError):
    def __init__(self, err: str = "Unknown plant error"):
        super().__init__(err)


def life(name: str, state: bool) -> None:
    if state is False:
        raise PlantError(f"The {name} plant is wilting!")
    else:
        print(f"{name} plant is fine")


def watering(state: bool) -> None:
    if state is False:
        raise WaterError("Not enough water in the tank")
    else:
        print("Tank is okay")


def testing_err(name: str) -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        life(name, False)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    print("\nTesting WaterError...")
    try:
        watering(False)
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")

    def life_error() -> None:
        life("tomato", False)

    def water_error() -> None:
        watering(False)

    errors = [life_error, water_error]
    print("\nTesting catching all garden errors...")
    for i in errors:
        try:
            i()
        except (WaterError, PlantError) as e:
            print(f"Caught {e.__class__.__name__}: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    testing_err("tomato")

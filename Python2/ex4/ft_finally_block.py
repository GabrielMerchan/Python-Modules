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


def water_plant(plant_name: str) -> None:
    cap_name = plant_name.capitalize()
    if cap_name == plant_name:
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plant: str, plant1: str, plant2: str) -> None:
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    print("Opening watering system")
    plants = [plant, plant1, plant2]
    try:
        for i in plants:
            water_plant(i)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    print("Opening watering system")
    plants2 = [plant, plant1.lower(), plant2]
    try:
        for i in plants2:
            water_plant(i)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system("Tomato", "Lettuce", "Carrots")

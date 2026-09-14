#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: float) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    banana = Plant("Banana", 35, 58)
    Plant.show(banana)
    sunflower = Plant("sunflower", 23, 89)
    Plant.show(sunflower)
    cactus = Plant("cactus", 12, 6)
    Plant.show(cactus)

#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_old: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age_old = age_old

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_old} days old")

    def grow(self, growth: float, days: int) -> None:
        print("=== Garden Plant Growth ===")
        print(f"{self.name}: {self.height:.1f}cm, {self.age_old} days old")
        for i in range(1, days+1):
            print(f"=== Day {i} ===")
            self.height += growth
            Plant.age(self, self.age_old, 1)
            round(self.height, 1)
            print(f"{self.name}: {self.height:.1f}cm, {self.age_old} days old")

    def age(self, age: int, cicle: int) -> None:
        age += cicle
        self.age_old = age


if __name__ == "__main__":
    banana = Plant("Banana", 25, 30)
    cactus = Plant("cactus", 10, 3)
    oak = Plant("oak", 150, 3)
    olive = Plant("olive", 30, 200)
    almond = Plant("almond", 47, 145)
    # print("=== Plant Factory Output ===")
    # print(f"Created: {banana.name}:
    #  {banana.height:.1f}cm, {banana.age_old} days old")
    # print(f"Created: {cactus.name}:
    #  {cactus.height:.1f}cm, {cactus.age_old} days old")
    # print(f"Created: {oak.name}:
    #  {oak.height:.1f}cm, {oak.age_old} days old")
    # print(f"Created: {olive.name}:
    #  {olive.height:.1f}cm, {olive.age_old} days old")
    # print(f"Created: {almond.name}:
    #  {almond.height:.1f}cm, {almond.age_old} days old")
    # Plant.grow(olive, 4.3, 7)
    # print(f"Created: {olive.name}:
    #  {olive.height:.1f}cm, {olive.age_old} days old")

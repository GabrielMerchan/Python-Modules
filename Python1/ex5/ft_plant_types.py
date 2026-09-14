#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_old: int) -> None:
        if self.security(height, age_old, name) == 1:
            self._name = name.capitalize()
            self._height = 10.0
            self._age_old = 15
            return
        self._name = name.capitalize()
        self._height = height
        self._age_old = age_old

    def security(self, height: float, age: int, name: str) -> int:
        if height < 0 or age < 0:
            print(f"{name.capitalize()}: Error. Invalid values")
            return 1
        else:
            return 0

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height:.1f}cm")

    def get_height(self) -> float:
        height = self._height
        return height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_old = new_age
            print(f"Age updated: {self._age_old} days")

    def get_age(self) -> float:
        age = self._age_old
        return age

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age_old} days old")

    def grow(self, growth: float, days: int) -> None:
        print("=== Garden Plant Growth ===")
        print(f"{self._name}: {self._height:.1f}cm, {self._age_old} days old")
        for i in range(1, days+1):
            print(f"=== Day {i} ===")
            self._height += growth
            self.age(1)
            round(self._height, 1)
            print(f"{self._name}: {self._height:.1f}cm,"
                  f" {self._age_old} days old")

    def age(self, cicle: int) -> None:
        self._age_old += cicle


class Flower(Plant):
    def __init__(self, name: str,
                 height: float, age_old: int, color: str) -> None:
        super().__init__(name, height, age_old)
        self._color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._bloomed is True:
            print(f" {self._name} is blooming beautifuly!")
        else:
            print(f" {self._name} has not bloomed yet")

    def bloom(self) -> None:
        print(f"[asking the {self._name.lower()} to bloom]")
        self._bloomed = True


class Tree(Plant):
    def __init__(self, name: str,
                 height: float, age_old: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age_old)
        self._trunk_diameter = trunk_diameter
        self._shading = False

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")
        if self._shading is True:
            print(f"Tree {self._name} now produces a shade of "
                  f"{self._height:.1f}cm long and "
                  f"{self._trunk_diameter:.1f}cm wide")
        else:
            print(f"{self._name} is not producing shade")

    def produce_shade(self) -> None:
        print(f"[asking the {self._name.lower()} to produce shade]")
        self._shading = True


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age_old: int, harvest_season: str) -> None:
        super().__init__(name, height, age_old)
        self._harvest_season = harvest_season.capitalize()
        self._nutritional_values = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_values}")

    def grow(self, growth: float, days: int) -> None:
        print(f"[make {self._name.lower()} grow and age for {days} days]")
        for i in range(1, days+1):
            self._height += growth
            self._nutritional_values += 1
            Plant.age(self, 1)
            round(self._height, 1)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("rose", 15, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print("")
    print("=== Tree")
    oak = Tree("oak", 200, 365, 5)
    oak.show()
    oak.produce_shade()
    oak.show()
    print("")
    print("=== Vegetable")
    tomato = Vegetable("tomato", 5, 10, "april")
    tomato.show()
    tomato.grow(2.1, 20)
    tomato.show()

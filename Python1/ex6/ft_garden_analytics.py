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
        self.show_cont = 0
        self.statistics = self.Statistics()

    @classmethod
    def cr_anonym(cls) -> "Plant":
        unk = cls("unknown plant", 0.0, 0)
        return unk

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
        self.statistics._show_cont += 1

    def grow(self, growth: float, days: int) -> None:
        for i in range(1, days+1):
            self._height += growth
            round(self._height, 1)
        self.statistics._grow_cont += 1

    def age(self, cicle: int) -> None:
        self._age_old += cicle
        self.statistics._age_cont += 1

    @staticmethod
    def age_is_year(days_age: int) -> bool:
        if days_age > 365:
            return True
        else:
            return False

    class Statistics:
        def __init__(self) -> None:
            self._grow_cont = 0
            self._age_cont = 0
            self._show_cont = 0
            self._shade_cont = 0


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
        self._bloomed = True


class Seed(Flower):
    def __init__(self, name, height, age_old, color, seeds: int) -> None:
        super().__init__(name, height, age_old, color)
        self._seeds = seeds

    def show(self):
        super().show()
        if self._bloomed is True:
            print(f" Seeds: {self._seeds}")


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
        self._shading = True
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height:.1f}cm long and "
              f"{self._trunk_diameter:.1f}cm wide")
        self.statistics._shade_cont += 1


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
        for i in range(1, days+1):
            self._height += growth
            self._nutritional_values += 1
            round(self._height, 1)


def show_stats(plant: Plant, type: str) -> None:
    print(f"[statistics for {plant._name}]")
    print(f"Stats: {plant.statistics._grow_cont} grow, "
          f"{plant.statistics._age_cont} age,"
          f" {plant.statistics._show_cont} show")
    if type == "tree":
        print(f"{plant.statistics._shade_cont} shade")


# if __name__ == "__main__":
#     print("=== Garden statistic ===")
#     print("=== Check year-old")
#     days = 30
#     print(f"Is {days} days more than a year? -> {Plant.age_is_year(days)}")
#     days = 400
#     print(f"Is {days} days more than a year? -> {Plant.age_is_year(days)}")
#     rose = Flower("rose", 15, 10, "red")
#     print("")
#     print("=== Flower")
#     rose.show()
#     show_stats(rose, "flower")
#     print(f"[asking the {rose._name.lower()} to grow and bloom]")
#     rose.bloom()
#     rose.grow(8,1)
#     rose.show()
#     show_stats(rose, "flower")
#     print("")
#     print("=== Tree")
#     oak = Tree("oak", 200, 365, 5)
#     oak.show()
#     show_stats(oak, "tree")
#     print(f"[asking the {oak._name.lower()} to produce shade]")
#     oak.produce_shade()
#     show_stats(oak, "tree")
#     print("")
#     print("=== Anonymous")
#     unk = Plant.cr_anonym()
#     unk.show()
#     show_stats(oak, "unk")

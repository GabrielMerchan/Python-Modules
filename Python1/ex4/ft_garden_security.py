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
            print(f"Height updated: {self._height}cm")

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
            Plant.age(self, self._age_old, 1)
            round(self._height, 1)
            print(f"{self._name}: {self._height:.1f}cm,"
                  f" {self._age_old} days old")

    def age(self, age: int, cicle: int) -> None:
        age += cicle
        self._age_old = age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("rose", 15, 10)
    print(f"Plant created: {rose._name}:"
          f"{rose._height:.1f}cm, {rose._age_old} days old")
    print("")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-25)
    rose.set_age(-30)
    print("")
    print(f"Current state: {rose._name}:"
          f" {rose._height:.1f}cm, {rose._age_old} days old")

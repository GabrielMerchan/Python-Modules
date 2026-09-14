#!/usr/bin/env python3

def plant_info(name: str, height: int, age: int) -> None:
    name = name.capitalize()

    print("=== Welcome to My Garden ===")
    print("Plant: " + name)
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("")
    print("=== End of Program ===")


if __name__ == "__main__":
    name = "rose"
    height = 23
    age = 12
    plant_info(name, height, age)

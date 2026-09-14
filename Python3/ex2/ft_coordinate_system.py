#!/usr/bin/env python3

import math


class err_syntax(Exception):
    def __init__(self, msg: str = "Invalid syntax"):
        super().__init__(msg)


def check_elements(val_list: list[str]) -> None:
    if len(val_list) != 3:
        raise err_syntax()


def ask_coord() -> tuple[float, float, float]:
    val_str = input("Enter new coordinates as floats in format "
                    "'x,y,z': ").split(",")
    try:
        check_elements(val_str)
    except err_syntax as e:
        print(f"{e}")
        return ask_coord()
    val_int = []
    try:
        for i in val_str:
            val_int.append(round(float(i), 1))
    except ValueError:
        print(f"Error on parameter '{i}': could "
              f"not convert string to float: '{i}'")
        return ask_coord()
    if len(val_int) != 3:
        raise err_syntax()
    x, y, z = val_int
    values = (x, y, z)
    return values


def distance_form(
    tuple1: tuple[float, float, float],
    tuple2: tuple[float, float, float]
) -> float:
    distance = round(float(math.sqrt((tuple1[0]-tuple2[0]) ** 2
                                     + (tuple1[1]-tuple2[1]) ** 2
                                     + (tuple1[2]-tuple2[2]) ** 2)), 4)
    return distance


def display_coords() -> None:
    print("=== Gamer Coordinate System ===\n")
    print("Get a first set of coordinates")
    coord1 = ask_coord()
    print(f"Got a first tuple: ({coord1})")
    print(f"It includes: X={coord1[0]}, Y={coord1[1]}, Z={coord1[2]}")
    center = (0.0, 0.0, 0.0)
    distance = distance_form(coord1, center)
    print(f"Distance to center: {distance}\n")
    print("Get a second set of coordinates")
    coord2 = ask_coord()
    distance = distance_form(coord1, coord2)
    print(f"Distance between the 2 sets of coordinates: {distance}")


if __name__ == "__main__":
    display_coords()

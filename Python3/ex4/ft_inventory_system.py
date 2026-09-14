#!/usr/bin/env python3

import sys


class RedundantError(Exception):
    def __init__(self, msg: str = 'Unknown error'):
        super().__init__(msg)


def parser() -> dict[str, int]:
    inventory: dict[str, int] = {}
    lst = sys.argv[1:]
    for i in lst:
        try:
            arg_syntax(i)
            command = i.split(':')
            arg_redun(command[0], list(inventory.keys()))
            inventory[command[0]] = int(command[1])
        except (SyntaxError, ValueError, RedundantError) as e:
            print(f"{e}")
    return inventory


def count_item(inventory: dict[str, int]) -> None:
    sum(inventory.values())


def maxmin_item(inventory: dict[str, int], order: str) -> dict[str, int]:
    cont_lst = list(inventory.values())
    cont = cont_lst[0]
    key_lst = list(inventory.keys())
    key = key_lst[0]
    if order == "max":
        for i in inventory:
            if inventory[i] > cont:
                cont = inventory[i]
                key = i
    elif order == 'min':
        for i in inventory:
            if inventory[i] < cont:
                cont = inventory[i]
                key = i
    maxmin_item = {key: cont}
    return maxmin_item


def arg_syntax(arg: str) -> None:
    if ':' not in arg:
        raise SyntaxError(f"Error - invalid parameter '{arg}'")
    args = arg.split(':')
    try:
        int(args[1])
    except ValueError as e:
        raise ValueError(f"Quantity error for '{args[0]}': {e}")
    if int(args[1]) < 0:
        raise ValueError(f"Quantity error for '{args[0]}': "
                         f"value cant be negative ({args[1]})")


def arg_redun(arg: str, arg_lst: list[str]) -> None:
    for i in arg_lst:
        if arg in arg_lst:
            raise RedundantError(f"Redundant item '{i} - discarding'")


def display() -> None:
    print("=== Inventory System Analysis ===")
    invent = parser()
    print(f"Got inventory: {invent}")
    keys_lst = list(invent.keys())
    print(f"Item list: {keys_lst}")
    val_sum = sum(invent.values())
    print(f"Total quantity of the {len(invent)} items: {val_sum}")
    for i in keys_lst:
        print(f"Item {i} represents "
              f"{round(float((invent[i] / val_sum)*100), 1)}%")
    cont_invent = maxmin_item(invent, 'max')
    keys_lst = list(cont_invent.keys())
    val_lst = list(cont_invent.values())
    print(f"Item most abundant: {keys_lst[0]} with quantity {val_lst[0]}")
    cont_invent = maxmin_item(invent, 'min')
    keys_lst = list(cont_invent.keys())
    val_lst = list(cont_invent.values())
    print(f"Item least abundant: {keys_lst[0]} with quantity {val_lst[0]}")
    invent.update({'bow': 2, 'arrow': 10})
    print(f"Updated inventory: {invent}")


if __name__ == "__main__":
    display()

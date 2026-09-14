#!/usr/bin/env python3

import random


achievements = ["Harder", "Better", "Faster", "Stronger", "Buy it",
                "Use it", "Break it", "Fix it", "Trash it",
                "Change it", "Mail", "Upgrade it"]


def gen_player_achievements() -> set[str]:
    achv_cont = random.randint(5, 9)
    player = set(random.sample(achievements, achv_cont))
    return player


def display_achvs() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print(f"\nAll distinct achievements: {alice | bob | charlie | dylan}")
    print(f"Common achievements: {alice & bob & charlie & dylan}\n")
    print(f"Only Alice has: {alice - (bob | charlie | dylan)}")
    print(f"Only Bob has: {bob - (alice | charlie | dylan)}")
    print(f"Only Charlie has: {charlie - (bob | alice | dylan)}")
    print(f"Only Dylan has: {dylan - (bob | charlie | alice)}\n")
    all_achvs = set(achievements)
    print(f"Alice is missing: {all_achvs - alice}")
    print(f"Bob is missing: {all_achvs - bob}")
    print(f"Charlie is missing: {all_achvs - charlie}")
    print(f"Dylan is missing: {all_achvs - dylan}")


if __name__ == "__main__":
    display_achvs()

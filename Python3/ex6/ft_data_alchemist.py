#!/usr/bin/env python3

import random

players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
           'Gregory', 'jonh', 'kevin', 'Liam']


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {players}")
    cap_pl = [pl.capitalize() for pl in players]
    cap_on_pl = [pl for pl in players if pl == pl.capitalize()]

    print(f"New list with all names capitalized: {cap_pl}")
    print(f"New list of capitalized names only: {cap_on_pl}")

    cap_dict = {i: (random.randint(0, 500)) for i in cap_pl}
    print(f"Score dict: {cap_dict}")
    score_avg = round(sum(cap_dict.values()) / len(cap_dict.values()), 2)
    print(f"Score average is {score_avg}")
    cap_high_dict = {key: value for (key, value)
                     in cap_dict. items() if value > int(score_avg)}
    print(f"High scores: {cap_high_dict}")

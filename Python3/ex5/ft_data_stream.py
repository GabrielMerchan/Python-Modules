#!/usr/bin/env python3

import typing
import random

names = ['bob', 'alice', 'dylan', 'charlie']

actions = ['run', 'eat', 'sleep', 'grab', 'climb', 'swim', 'use', 'release']


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        event = (random.choice(names), random.choice(actions))
        yield event


def consume_event(
        act_lst: list[tuple[str, str]]
                  ) -> typing.Generator[list[tuple[str, str]], None, None]:
    while len(act_lst) != 0:
        removed = random.choice(act_lst)
        print(f"Got event from list: {removed}")
        act_lst.remove(removed)
        yield act_lst


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    event = gen_event()
    for i in range(1000):
        name, action = next(event)
        print(f"Event {i}: Player {name} did action {action}")
    act_lst = []
    for i in range(1, 11):
        act_lst.append(next(event))
    print(f"Built list of {i} events: {act_lst}")
    ev = consume_event(act_lst)
    for a in ev:
        print(f"Remains in list: {a}")

#!/usr/bin/env python3

import sys


class Usage(Exception):
    def __init__(self, err: str = "unknown error"):
        super().__init__(err)


def input_score(score_str: str) -> int:
    num = int(score_str)
    return num


def check_scores(scores: list[str]) -> list[int]:
    if len(scores) == 0:
        raise Usage("python3 ft_score_analytics.py <score1> <score2> ...")
    score_good = []
    cont = len(scores)
    for i in scores:
        try:
            score_good.append(input_score(i))
        except ValueError:
            print(f"Invalid parameter: '{i}'")
            cont -= 1
    if cont == 0 or len(score_good) == 0:
        raise Usage("python3 ft_score_analytics.py <score1> <score2> ...")
    return score_good


def add_scores() -> list[int]:
    score_list = sys.argv[1:]
    scores = []
    try:
        scores = check_scores(score_list)
    except Usage as e:
        print(f"No scores provided. {e.__class__.__name__}: {e}")
        sys.exit()
    return scores


def display_scores(scores: list[int]) -> None:
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scoring = add_scores()
    display_scores(scoring)

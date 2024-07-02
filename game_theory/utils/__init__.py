from enum import Enum, auto


class PlayerDecision(Enum):
    COOPERATE = "Cooperate"
    DEFECT = "Defect"


def is_even(num: int):
    return num % 2 == 0


def is_odd(num: int):
    return num % 2 != 0

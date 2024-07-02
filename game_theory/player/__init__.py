from abc import ABC

from game_theory.utils import PlayerDecision


# Abstract Player Class, should not be used in actual implementation
class Player(ABC):
    def __init__(self, name="Default"):
        self.points = 0
        self.name = name

    def add_points(self, points: int):
        self.points += points

    def next_move(self, opponent_decisions: list[PlayerDecision]) -> PlayerDecision:
        return PlayerDecision.COOPERATE

    def cleanup_round(self):
        return

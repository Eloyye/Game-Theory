# decides based on
from random import randint

from game_theory import Player
from game_theory.utils import PlayerDecision


class RandomPlayer(Player):
    def __init__(self, name="Random"):
        super().__init__(name)

    def next_move(self, opponent_decisions: list[PlayerDecision]) -> PlayerDecision:
        return PlayerDecision.COOPERATE if randint(0, 1) == 0 else PlayerDecision.DEFECT

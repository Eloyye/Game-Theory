from game_theory import Player
from game_theory.utils import PlayerDecision


class ForgivingPlayer(Player):
    def __init__(self, name="Forgiving"):
        super().__init__(name)

    def next_move(self, opponent_decisions: list[PlayerDecision]) -> PlayerDecision:
        return PlayerDecision.COOPERATE
        
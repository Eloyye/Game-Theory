from game_theory import Player
from game_theory.utils import PlayerDecision


class DefectingPlayer(Player):
    def __init__(self, name="Defect"):
        super().__init__(name)

    def next_move(self, opponent_decisions: list[PlayerDecision]) -> PlayerDecision:
        return PlayerDecision.DEFECT

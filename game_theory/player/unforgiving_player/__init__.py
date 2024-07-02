from game_theory import Player
from game_theory.utils import PlayerDecision


class UnforgivingPlayer(Player):
    def __init__(self, name="Unforgiving"):
        super().__init__(name)
        # threshold where if the opponent retaliates greater than this, then player will retaliate
        self.unforgiving_mode = False

    def next_move(self, opponent_decisions: list[PlayerDecision]) -> PlayerDecision:
        if self.unforgiving_mode:
            return PlayerDecision.DEFECT
        if len(opponent_decisions) >= 1 and opponent_decisions[-1] == PlayerDecision.DEFECT:
            self.unforgiving_mode = True
            return PlayerDecision.DEFECT
        return PlayerDecision.COOPERATE

    def cleanup_round(self):
        self.unforgiving_mode = False

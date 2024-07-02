from random import randint

from game_theory import Player
from game_theory.utils import PlayerDecision


# decides based on
class PavlovPlayer(Player):
    def __init__(self, name="Pavlov"):
        super().__init__(name)
        self.previous_move = None

    def next_move(self, opponent_decisions: list[PlayerDecision]) -> PlayerDecision:
        if opponent_decisions and self.previous_move:
            opponent_prev_move = opponent_decisions[-1]
            if self.previous_move == opponent_prev_move:
                self.previous_move = PlayerDecision.COOPERATE
                return PlayerDecision.COOPERATE
            if self.previous_move != opponent_prev_move:
                self.previous_move = PlayerDecision.DEFECT
                return PlayerDecision.DEFECT
        #     case where both doesn't cooperate
        decision = PlayerDecision.COOPERATE if randint(0, 1) == 0 else PlayerDecision.DEFECT
        self.previous_move = decision
        return decision

    def cleanup_round(self):
        self.previous_move = None

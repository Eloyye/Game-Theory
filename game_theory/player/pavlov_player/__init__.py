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
            # concedes when punished
            if self.previous_move == opponent_prev_move:
                self.previous_move = PlayerDecision.COOPERATE
                return PlayerDecision.COOPERATE
        #     case where both doesn't cooperate
            if self.previous_move != opponent_prev_move:
                self.previous_move = PlayerDecision.DEFECT
                return PlayerDecision.DEFECT
        #     case where both doesn't cooperate
        return PlayerDecision.COOPERATE

    def cleanup_round(self):
        self.previous_move = None

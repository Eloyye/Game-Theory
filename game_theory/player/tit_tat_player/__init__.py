from game_theory import Player
from game_theory.utils import PlayerDecision


class TitTatPlayer(Player):
    def __init__(self, name="TitTat", opponent_def_thresh=1):
        super().__init__(name)
        # threshold where if the opponent retaliates greater than this, then player will retaliate
        self.opponent_def_thresh = opponent_def_thresh

    def next_move(self, opponent_decisions: list[PlayerDecision]) -> PlayerDecision:
        if len(opponent_decisions) >= self.opponent_def_thresh:
            latest_decisions = opponent_decisions[::-1][:self.opponent_def_thresh]
            for decision in latest_decisions:
                if decision == PlayerDecision.COOPERATE:
                    return PlayerDecision.COOPERATE
            return PlayerDecision.DEFECT
        return PlayerDecision.COOPERATE

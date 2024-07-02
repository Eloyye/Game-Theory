from game_theory.utils import PlayerDecision


class PayoffMatrix:
    def __init__(self, cooperation_outcome=5, uneven_defect_outcome = (10, 0), all_defect_outcome = 0):
        self.cooperation_outcome = cooperation_outcome
        self.uneven_defect_outcome = uneven_defect_outcome
        self.all_defect_outcome = all_defect_outcome

    def evaluate(self, player1_move: PlayerDecision, player2_move: PlayerDecision) -> tuple[int, int]:
        if player1_move == player2_move and player1_move == PlayerDecision.COOPERATE:
            return self.cooperation_outcome, self.cooperation_outcome
        if player1_move == player2_move and player1_move == PlayerDecision.DEFECT:
            return self.all_defect_outcome, self.all_defect_outcome
        if player1_move == PlayerDecision.DEFECT:
            return self.uneven_defect_outcome[0], self.uneven_defect_outcome[1]
        return self.uneven_defect_outcome[1], self.uneven_defect_outcome[0]

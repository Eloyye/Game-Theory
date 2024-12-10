from random import randint
from logging import getLogger

from game_theory.payoff_matrix import PayoffMatrix
from game_theory.player import Player
from game_theory.utils import is_odd, PlayerDecision

logger = getLogger(__name__)

class GameTheory:
    def __init__(self, rounds=10, players=None, payoff_matrix=None, random_ratio=0):
        if players is None:
            players = []
        if payoff_matrix is None:
            payoff_matrix = PayoffMatrix()
        self.players = players
        self.rounds = rounds
        self.payoff_matrix = payoff_matrix
        self.random_ratio = random_ratio

    def add_players(self, players: list[Player]):
        self.players += players

    def play(self) -> dict[str, int]:
        if is_odd(len(self.players)):
            error_message = "The number of players must be even"
            raise RuntimeError(error_message)
        logger.info("Game Starting")
        for i, pair_players in enumerate(self._assign_players()):
            logger.info(f"======= Start of Round {i + 1} =======")
            for player1, player2 in pair_players:
                self._face_off(player1, player2)
            logger.info(f"======= End of Round {i + 1} =======")
        self.players = sorted(self.players, key=lambda pyr: pyr.points, reverse=True)
        player_points = {player.name: player.points for player in self.players}
        return player_points

    def __str__(self):
        players = []
        for position, player in enumerate(self.players):
            players.append(f"{position + 1}. {player.name}: {player.points} points\n")
        return "".join(players)

    def _assign_players(self):
        num_players = len(self.players)
        for i in range(num_players - 1):
            current_pairs = []
            for j in range((num_players // 2)):
                current_pairs.append([self.players[j], self.players[num_players - 1 - j]])
            yield current_pairs
            self.players = [self.players[0]] + [self.players[-1]] + self.players[1: -1]

    def _face_off(self, player1: Player, player2: Player):
        logger.info("*" * 20)
        logger.info(f"{player1.name} vs. {player2.name}")
        if randint(0, 1) == 0:
            player1, player2 = player2, player1
        player1_moves, player2_moves = [], []
        init_points_p1, init_points_p2 = player1.points, player2.points
        # randomize which players go first because there might be some bias in who goes first
        for _ in range(self.rounds):
            p1_move, p2_move = self._player_moves(player1, player2_moves), self._player_moves(player2, player1_moves)
            p1_points, p2_points, = self.payoff_matrix.evaluate(p1_move, p2_move)
            logger.info(
                f"{player1.name} has received {p1_points} points and {player2.name} has received {p2_points} points")
            # appends at the end to make sure that moves happen simultaneously
            player1_moves.append(p1_move)
            player2_moves.append(p2_move)
            player1.add_points(p1_points)
            player2.add_points(p2_points)
        p1_points_earned_in_round, p2_points_earned_in_round = player1.points - init_points_p1, player2.points - init_points_p2
        # assert p1_points_earned_in_round >= 0 and p2_points_earned_in_round >= 0
        logger.info(
            f"{player1.name} has earned in total: {p1_points_earned_in_round}, {player2.name} has earned in total: {p2_points_earned_in_round}")
        logger.info("*" * 20)
        #     make sure players reset context/ history for upcoming player
        player1.cleanup_round()
        player2.cleanup_round()

    def _player_moves(self, player1, player2_moves):
        if self.random_ratio:
            tries = self.random_ratio * 100
            rand_num = randint(1, 100)
            if rand_num <= tries:
                move = PlayerDecision.COOPERATE if randint(0, 1) == 0 else PlayerDecision.DEFECT
                logger.info(f"{player1.name} has chosen {move}")
                return move
        p1_move = player1.next_move(player2_moves)
        logger.info(f"{player1.name} has chosen {p1_move}")
        return p1_move

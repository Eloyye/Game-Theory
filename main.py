import logging

from game_theory import GameTheory
from game_theory.player.player_factory import PlayerFactory

logger = logging.getLogger(__name__)
def main():
    logging.basicConfig(filename='game_theory.log', level=logging.INFO)
    game = GameTheory()
    for _ in range(10):
        game.add_players([PlayerFactory.get_player("tittat")])
        game.add_players([PlayerFactory.get_player("pavlov")])
        game.add_players([PlayerFactory.get_player("defect")])
        game.add_players([PlayerFactory.get_player("forgive")])
        game.add_players([PlayerFactory.get_player("random")])
        game.add_players([PlayerFactory.get_player("unforgiving")])
    game.play()


if __name__ == '__main__':
    main()

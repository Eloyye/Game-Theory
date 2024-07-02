import logging

from game_theory import GameTheory
from game_theory.player.player_factory import PlayerFactory

logger = logging.getLogger(__name__)
def main():
    logging.basicConfig(filename='game_theory.log', level=logging.INFO)
    game = GameTheory()
    game.add_players([PlayerFactory.get_player('unforgiving'), PlayerFactory.get_player('tittat'), PlayerFactory.get_player('forgive'), PlayerFactory.get_player('defect')])
    game.play()


if __name__ == '__main__':
    main()

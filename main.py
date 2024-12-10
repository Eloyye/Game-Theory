import logging

from config_parsing import ConfigParsing
from game_theory import GameTheory
from game_theory.player.player_factory import PlayerFactory

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(filename='game_theory.log', level=logging.INFO)
    config_parsing = ConfigParsing()
    game = config_parsing.parse_to_game()
    game.play()
    print(game)


if __name__ == '__main__':
    main()

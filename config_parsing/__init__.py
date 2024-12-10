from json import load

from game_theory import GameTheory
from game_theory.player.player_factory import PlayerFactory


class ConfigParsing:
    def __init__(self, config_file_path: str = "config.json"):
        self.config_file_path = config_file_path

    def parse_to_game(self) -> GameTheory:
        with open(self.config_file_path) as config_file:
            parsed_data = load(config_file)
            random_ratio = float(parsed_data["random_ratio"])
            players = []
            for player_object in parsed_data["players"]:
                for _ in range(int(player_object["amount"])):
                    players.append(PlayerFactory.get_player(player_object["player_type"]))
            game = GameTheory(random_ratio=random_ratio)
            game.add_players(players)
            return game

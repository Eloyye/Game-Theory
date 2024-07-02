from game_theory import Player
from game_theory.player.always_defect_player import DefectingPlayer
from game_theory.player.always_forgive_player import ForgivingPlayer
from game_theory.player.pavlov_player import PavlovPlayer
from game_theory.player.random_player import RandomPlayer
from game_theory.player.tit_tat_player import TitTatPlayer
from game_theory.player.unforgiving_player import UnforgivingPlayer


class PlayerFactory:
    @staticmethod
    def get_player(player_name: str) -> Player:
        match player_name:
            case "unforgiving":
                return UnforgivingPlayer()
            case "tittat":
                return TitTatPlayer()
            case "forgive":
                return ForgivingPlayer()
            case "defect":
                return DefectingPlayer()
            case "pavlov":
                return PavlovPlayer()
            case "random":
                return RandomPlayer()
            case _:
                raise NameError(f"{player_name} does not match any player received")

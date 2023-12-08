"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Game: Initialisation et gestion du jeu
"""

# -----------------------------------------------------------------------------------------------
#  imports:
from player import Player

# -----------------------------------------------------------------------------------------------

class Game():
    def __init__(self, players=[]):
        self.players = players
        self.nb_players = len(self.players)
    
    def get_player_by_id(self, id):
        for player in self.players:
            if player.id == id:
                return player
        return None
    
    def get_player_id_by_id_client(self, id):
        for i, player in enumerate(self.players):
            if player.id == id:
                return i
        return None
    
    def add_player(self, id, pseudo):
        player = Player(id, pseudo)
        self.players.append(player)
        return {"addPlayer" : {
                        "id": player.id,
                        "pseudo": player.pseudo,
                        "player_nb_room" : player.player_nb_room,
                        "player_position" : player.player_position,
                        "player_coord": player.player_coord,
                        "player_orientation": player.player_orientation,
                        # "player_nb_medaillon": player.player_nb_medaillon,
                    }
                }
    
    def sup_player(self, id):
        player = self.get_player_by_id(id)
        if player:
            self.players.remove(player)
            return {"supPlayer" : player.id,}
        else:
            return None
    
    def update_player(self, id, data):
        player = self.get_player_by_id(id)
        if player:
            player.player_nb_room = data["player_nb_room"]
            player.player_position = data["player_position"]
            player.player_coord = data["player_coord"]
            player.player_orientation = data["player_orientation"]
            # player.player_nb_medaillon = data["player_nb_medaillon"]
            return {"player" : {
                        "id": player.id,
                        "pseudo": player.pseudo,
                        "player_nb_room" : player.player_nb_room,
                        "player_position" : player.player_position,
                        "player_coord": player.player_coord,
                        "player_orientation": player.player_orientation,
                        # "player_nb_medaillon": player.player_nb_medaillon,
                    }
                }
        else:
            return None
    
    def init_players(self):
        players = []
        for player in self.players:
            players.append({
                            "id": player.id,
                            "pseudo": player.pseudo,
                            "player_nb_room" : player.player_nb_room,
                            "player_position" : player.player_position,
                            "player_coord": player.player_coord,
                            "player_orientation": player.player_orientation,
                            # "player_nb_medaillon": player.player_nb_medaillon,
                            })
        return {"init_players" : players}
    
    def init_levels(self):
        pass
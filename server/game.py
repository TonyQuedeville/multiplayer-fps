"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Game: Initialisation et gestion du jeu
"""

# -----------------------------------------------------------------------------------------------
#  imports:
from player import Player
# from token import Tokens

# -----------------------------------------------------------------------------------------------

class Game():
    def __init__(self, players=[], tokens=[]):
        # Joueurs
        self.players = players
        self.nb_players = len(self.players)
        # Médaillons
        self.tokens = [
            [[4,0,4]], # Level0
            [[9,0,11],[11,0,4],[9,0,9],[6,0,10],[3,0,9],[2,0,9],[8,0,4]], # Level1
            [[1,0,1],[11,0,9],[12,0,10],[11,0,7],[10,0,10],[5,0,9],[5,0,7],[11,0,3],[12,0,5]], # Level2
            [[2,0,1],[9,0,1],[14,0,1],[7,0,11],[12,0,9],[14,0,13],[14,0,5]], # Level3
            [[5,0,5],[2,0,13],[7,0,8],[9,0,2],[8,0,3],[13,0,6],[14,0,1],[14,0,8],[14,0,11], [14,0,13]], # Level4
            [[13,0,2],[3,0,6],[9,0,8],[2,0,9],[13,0,12],[5,0,14],[13,0,16],[6,0,17],[10,0,20],[13,0,20]], # Level5
            [[1,0,2],[13,0,2],[4,0,5],[8,0,5],[9,0,6],[3,0,7],[6,0,9],[1,0,12],[12,0,13],[4,0,15],[10,0,17],[12,0,17],[4,0,19],[11,0,20],[3,0,24],[5,0,24],[13,0,24]], # Level6
            [[8,0,2],[7,0,3],[11,0,3],[6,0,6],[7,0,7],[10,0,8],[2,0,8],[3,0,9],[1,0,13],[4,0,14],[1,0,15],[7,0,15],[8,0,16],[10,0,16],[12,0,16],[5,0,17],[7,0,15],[3,0,18],[10,0,20],[9,0,21],[2,0,24],[9,0,24],[11,0,24],[13,0,24],[1,0,25],[1,0,27],[13,0,27],[10,0,23],[6,0,16]], # Level7
            [[1,0,1],[5,0,1],[10,0,1],[13,0,1],[4,0,2],[12,0,3],[11,0,4],[6,0,5],[1,0,6],[1,0,8],[7,0,9],[10,0,11],[1,0,12],[5,0,12],[2,0,13],[4,0,14],[9,0,14],[11,0,14],[3,0,15],[13,0,15],[8,0,17],[1,0,18],[4,0,18],[11,0,18],[8,0,19],[11,0,20],[3,0,22],[11,0,23],[1,0,26],[6,0,26],[8,0,26],[13,0,26],[1,0,28],[10,0,28],[4,0,29],[9,0,29],[13,0,29],[11,0,2],[3,0,12],[10,0,19],[11,0,29]], # Level8
        ]
    
    def get_player_by_id(self, id):
        for player in self.players:
            if player.id_client == id:
                return player
        return None
    
    def get_player_by_id_client(self, id_client):
        for player in self.players:
            if player.id_client == id_client:
                return player
        return None
    
    def add_player(self, id_client, pseudo):
        player = Player(len(self.players), id_client, pseudo)
        self.players.append(player)
        return {"addPlayer" : {
                        "id": player.id,
                        "id_client": player.id_client,
                        "pseudo": player.pseudo,
                        "player_nb_room" : player.player_nb_room,
                        "player_position" : player.player_position,
                        "player_coord": player.player_coord,
                        "player_orientation": player.player_orientation,
                        # "player_nb_medaillon": player.player_nb_medaillon,
                    }
                }
    
    def sup_player(self, id_client):
        player = self.get_player_by_id_client(id_client)
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
            return {"play" : {
                        "id": player.id,
                        "id_client": player.id_client,
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
    
    def init_game(self, id):
        players = []
        for player in self.players:
            players.append({
                            "id": player.id,
                            "id_client": player.id_client,
                            "pseudo": player.pseudo,
                            "player_nb_room" : player.player_nb_room,
                            "player_position" : player.player_position,
                            "player_coord": player.player_coord,
                            "player_orientation": player.player_orientation,
                            # "player_nb_medaillon": player.player_nb_medaillon,
                            })
        return {
            "my_id" : id,
            "init_players" : players,
            "init_tokens" : self.tokens,
            }

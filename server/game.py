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
        found_player = next((player for player in self.players if player.id == id), None)
        return found_player
    
    def add_player(self, id, pseudo):
        player = Player(id, pseudo)
        self.players.append(player)
        return {"addPlayer" : "Bienvenu " + pseudo + ", bonne visite !"}
    
    def sup_player(self, id, pseudo):
        player = self.get_player_by_id(id)
        if player:
            self.players.remove(player)
            return {"supPlayer" : pseudo + " a quitté le jeu !"}
        else:
            return None
    
    def update_player(self, id, data):
        player = self.get_player_by_id(id)
        if player:
            player.nb_room = data["player_nb_room"]
            player.player_position = data["player_position"]
            player.player_coord = data["player_coord"]
            player.player_orientation = data["player_orientation"]
            player.nb_medaillon = data["player_nb_medaillon"]
            return {"players" : self.players}
        else:
            return None
        
    
    def set_medaillon(self, id):
        player = self.get_player_by_id(id)
        player.set_medaillon()
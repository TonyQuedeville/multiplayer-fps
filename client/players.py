"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    players: liste des joueurs
"""

# -----------------------------------------------------------------------------------------------
# imports:

class Player():
    def __init__(self, id, pseudo="", nb_room=0, position=[4,0,4], coord=[4.5, 0, 3.5], orientation = 90):
        self.id = id                            # Numero du joueur
        self.pseudo = pseudo                    # Pseudo du joueur
        self.player_nb_room = nb_room           # numero de salle dans laquelle le joueur se trouve
        self.player_position = position         # Position matricielle initiale level 0 (int)
        self.player_coord = coord               # Coordonnée initiale level 0 (float)
        self.player_orientation = orientation   # Orientation initiale level 0
        # self.player_nb_medaillon = 0          # Nombre de médaillons
        
# -----------------------------------------------------------------------------------------------

class Players():
    def __init__(self, players=[]):
        self.players = players
        self.nb_players = len(self.players)
    
    def init_players(self, players):
        for pl in players:
            self.add_player(pl)
    
    def get_player_by_id(self, id):
        for player in self.players:
            if player.id == id:
                return player
        return None
    
    def add_player(self, data):
        player = Player(data["id"], data["pseudo"])
        player.player_nb_room = data["player_nb_room"]
        player.player_position = data["player_position"]
        player.player_coord = data["player_coord"]
        player.player_orientation = data["player_orientation"]
        # player.player_nb_medaillon = data["player_nb_medaillon"]
        self.players.append(player)
    
    def sup_player(self, id):
        player = self.get_player_by_id(id)
        if player:
            self.players.remove(player)
    
    def update_player(self, data):
        player = self.get_player_by_id(data["id"])
        if player:
            player.nb_room = data["player_nb_room"]
            player.player_position = data["player_position"]
            player.player_coord = data["player_coord"]
            player.player_orientation = data["player_orientation"]
            # player.player_nb_medaillon = data["player_nb_medaillon"]

# -----------------------------------------------------------------------------------------------


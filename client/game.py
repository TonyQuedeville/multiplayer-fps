"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    players: liste des joueurs
"""

# -----------------------------------------------------------------------------------------------
# imports:
from player import Player

# -----------------------------------------------------------------------------------------------
class Game():
    def __init__(self, players=[], tokens=[]):
        # Moi
        self.id = None
        # Joueurs
        self.players = players
        self.nb_players = len(self.players)
        # Médaillons
        self.tokens = tokens
    
    # Setter
    def set_id(self, id):
        self.id = id
    
    # Joueurs
    def init_players(self, players):
        for player in players:
            self.add_player(player)
    
    def get_player_by_id(self, id):
        for player in self.players:
            if player.id == id:
                return player
        return None
    
    def add_player(self, data):
        player = Player(data["id"], data["id_client"], data["pseudo"])
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
    
    # Medaillons
    def init_tokens(self, tokens):
        self.tokens = tokens
    
    def get_token_by_id(self, id):
        for token in self.tokens:
            if token.id == id:
                return token
        return None
    
    def sup_token(self, id):
        token = self.get_token_by_id(id)
        if token:
            self.tokens.remove(token)

"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Class Player: Défini le joueur
"""

# -----------------------------------------------------------------------------------------------

class Player():
    def __init__(self, id, id_client, pseudo=""):
        self.id = id                        # Numero du joueur
        self.id_client = id_client          # Numero client
        self.pseudo = pseudo                # Pseudo du joueur
        self.player_nb_room = 0             # numero de salle dans laquelle le joueur se trouve
        self.player_position = [4, 0, 4]    # Position matricielle initiale level 0 (int)
        self.player_coord = [4.5, 0, 3.5]   # Coordonnée initiale level 0 (float)
        self.player_orientation = 90        # Orientation initiale level 0
        self.player_nb_medaillon = 0        # Nombre de médaillons

"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Class Player: Défini le joueur
"""

# ------------------------------------------------------------------------------------------------------------------------

class Player():
    def __init__(self, id=0, id_client=0, pseudo="", nb_room=0, position=[4,0,4], coord=[4.5, 0, 3.5], orientation = 90):
        self.id = id                            # Numero du joueur
        self.id_client = id_client              # Numero client
        self.pseudo = pseudo                    # Pseudo du joueur
        self.player_nb_room = nb_room           # numero de salle dans laquelle le joueur se trouve
        self.player_position = position         # Position matricielle initiale level 0 (int)
        self.player_coord = coord               # Coordonnée initiale level 0 (float)
        self.player_orientation = orientation   # Orientation initiale level 0
        # self.player_nb_medaillon = 0          # Nombre de médaillons
        
# ------------------------------------------------------------------------------------------------------------------------
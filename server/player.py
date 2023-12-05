"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Class Player: Défini le joueur
"""

# -----------------------------------------------------------------------------------------------

class Player():
    def __init__(self, id, pseudo=""):
        self.id = id                    # Numero du joueur
        self.pseudo = pseudo            # Pseudo du joueur
        self.nb_room = 0                # numero de salle dans laquelle le joueur se trouve
        self.position = [4, 0, 4]       # Position matricielle initiale level 0 (int)
        self.coord = [4.5, 0, 3.5]      # Coordonnée initiale level 0 (float)
        self.orientation = 90           # Orientation initiale level 0
        self.nb_medaillon = 0           # Nombre de médaillons

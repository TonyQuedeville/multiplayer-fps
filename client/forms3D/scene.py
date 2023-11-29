"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Scene: Labyrinthes
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import random

from OpenGL.GL import *
# from OpenGL.GLU import *
# from OpenGL.GLUT import *

from forms3D.plane import plane
from forms3D.cube import cube
from forms3D.sphere import sphere
from forms3D.cylindre import cylindre
from forms3D.tetra import tetra
from forms3D.texte import texte3D

from forms3D.levels.level0 import *
from forms3D.levels.level1 import *
from forms3D.levels.level2 import *
from forms3D.levels.level3 import *
from forms3D.levels.level4 import *
from forms3D.levels.level5 import *
from forms3D.levels.level6 import *
from forms3D.levels.level7 import *
from forms3D.levels.level8 import *

# -----------------------------------------------------------------------------------------------
# globals:

levels = {
    0: (level0, player_position_init_0),
    1: (level1, player_position_init_1),
    2: (level2, player_position_init_2),
    3: (level3, player_position_init_3),
    4: (level4, player_position_init_4),
    5: (level5, player_position_init_5),
    6: (level6, player_position_init_6),
    7: (level7, player_position_init_7),
    8: (level8, player_position_init_8),
}

chiffre_orientation = {
    0: 0,
    1: 0,
    2: 0,
    3: 90,
    4: 90,
    5: 180,
    6: 180,
    7: -90,
    8: -90,
    9: 0,
}

class Scene():
    def __init__(self, room=0, texture=None):
        level = levels.get(room) # Niveau
        self.room = level[0] # Salle d'exposition
        self.player_position = level[1] # position initial du joueur
        self.player_x = self.player_position[0] + .5
        self.player_y = self.player_position[1]
        self.player_z = self.player_position[2] - .5
        self.texture = texture # texture active
        self.med_rotate = 0 # Angle actuel des medaillons
        self.med_rotate_angle = .1 # Angle de rotation des medaillons
        self.med_rotate_axis = (1,0,0) # Axe de rotation des medaillons
        self.chiffre_rotate = 0 # Orientation des numero d'entrée au sol du hall d'accueil
    
    def set_room(self, room):
        self.room = levels.get(room)[0]
    
    def set_player_position(self, player_position):
        self.player_x = player_position[0]
        self.player_z = player_position[2]
    
    def set_texture(self, texture):
        self.texture = texture # texture active
    
    def set_med_rotate(self, angle):
        self.med_rotate = angle
    
    def set_med_rotate_axis(self, axis):
        self.med_rotate_axis = axis

    def display_scene(self):
        # Formes en fonction de la salle
        value_change = ""
        for y, lig in enumerate(self.room):
            for x, value in enumerate(lig):
                if value_change != value:
                    prefixe_form = value.split('-')[0]
                    if prefixe_form != "  ":
                        nb = int(value.split('-')[-1])
                        
                        if prefixe_form == "sl" or prefixe_form == "ml" or prefixe_form == "sp" or prefixe_form == "cl":
                            self.texture.apply_sols(nb)
                        elif prefixe_form == "pl":
                            self.texture.apply_eyes(nb)
                        elif prefixe_form == "bl" or prefixe_form == "md":
                            self.texture.apply_theme(nb)
                        elif prefixe_form == "ch":
                            self.texture.apply_chiffre(nb)
                            self.chiffre_rotate = chiffre_orientation.get(nb)
                        else:
                            print("erreur prefixe !")
                        
                self.forms(prefixe_form, (x-self.player_x, -0.5, y-self.player_z))
                value_change = value                    

    def forms(self, prefixe_form, coord):
        switcher = {
            "sl": lambda: plane(coord),
            "ml": lambda: cube(coord),
            "bl": lambda: cube(coord),
            "ch": lambda: cube((coord[0], -1, coord[2]), (.98, .01, .98), self.chiffre_rotate),
            "sp": lambda: sphere(coord, .5),
            "pl": lambda: sphere(coord, .10, 2),
            "cl": lambda: cylindre(coord, .5, .2),
            "md": lambda: cylindre((coord[0], -.1, coord[2]), .05, .01, self.med_rotate),
        }

        func = switcher.get(prefixe_form, lambda: "nb_form invalide")
        return func()

    # Répartition aleatoire des oeuvres dans la salle
    def random_theme(self):
        nb_tex = len(self.texture.theme_id)-1
        
        if self.room:
            for y, row in enumerate(self.room):
                for x, value in enumerate(row):
                    prefixe_form = value.split('-')[0]
                    
                    if prefixe_form == "sl":
                        self.room[y][x] = "sl-0"
                    elif prefixe_form == "ml":
                        self.room[y][x] = "ml-0"
                    elif prefixe_form == "sp":
                        self.room[y][x] = "sp-0"
                    elif prefixe_form == "pl":
                        self.room[y][x] = "pl-0"
                    elif prefixe_form == "bl":
                        self.room[y][x] = f"bl-{random.randint(0, nb_tex)}"
                    elif prefixe_form == "cl":
                        self.room[y][x] = "cl-0"
                    elif prefixe_form == "md":
                        self.room[y][x] = f"md-{random.randint(0, nb_tex)}"
        else:
            print("Niveau non trouvé pour cet étage.")

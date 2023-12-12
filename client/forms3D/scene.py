"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Scene: Labyrinthes
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import random
import threading, time

from OpenGL.GL import *
# from OpenGL.GLU import *
# from OpenGL.GLUT import *

from forms3D.camera import Camera
from forms3D.textures import Texture

from forms3D.plane import couloir, porte
from forms3D.cube import cube
from forms3D.groom import groom
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
    0: (level0, player_position_init_0, player_orientation_init_0),
    1: (level1, player_position_init_1, player_orientation_init_1),
    2: (level2, player_position_init_2, player_orientation_init_2),
    3: (level3, player_position_init_3, player_orientation_init_3),
    4: (level4, player_position_init_4, player_orientation_init_4),
    5: (level5, player_position_init_5, player_orientation_init_5),
    6: (level6, player_position_init_6, player_orientation_init_6),
    7: (level7, player_position_init_7, player_orientation_init_7),
    8: (level8, player_position_init_8, player_orientation_init_8),
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
    def __init__(self, nb_room=0, nb_player=1):
        self.nb_room = nb_room
        
        level = levels.get(nb_room) # Niveau
        self.room = level[0] # Salle d'exposition
        self.size_room = (len(self.room[0]), len(self.room))

        self.player_position = level[1]                 # Position initial du joueur
        self.player_x = self.player_position[0] + .5
        self.player_y = self.player_position[1] 
        self.player_z = self.player_position[2] - .5
        self.player_orientation = level[2]              # Orientation initial du joueur
        self.player_nb_medaillon = 0                    # Nombre de médaillons
        self.player = {
            "player_nb_room" : self.nb_room,
            "player_position" : self.player_position,
            "player_coord" : (self.player_x, self.player_y, self.player_z),
            "player_orientation" : self.player_orientation,
            "player_nb_medaillon": 0,
        }
        
        self.radius_eyes = .1       # Rayon des yeux
        self.radius_token = .05     # Rayon des médaillons
        self.token_id = None        # Médaillon pris
        
        self.camera = Camera(position=(self.player_x, self.player_y, self.player_z))
        
        self.texture = Texture(nb_room, nb_player) # Textures
        self.texture.load_sols()
        self.texture.load_eyes()
        self.texture.load_chiffre()
        self.texture.load_grooms()
        self.texture.load_theme()
        
        self.med_rotate = 0 # Angle actuel des medaillons
        self.med_rotate_angle = .1 # Angle de rotation des medaillons
        self.med_rotate_axis = (1,0,0) # Axe de rotation des medaillons
        
        self.chiffre_rotate = 0 # Orientation des numero d'entrée au sol du hall d'accueil
    
    def animations_scene(self, timer=2):
        if timer == 0:
            self.random_theme()
        else:
            # Changement aléatoire de projection des oeuvres à intervals régulier
            self.theme_thread = threading.Thread(target=self.image_random, args=(timer,))
            self.theme_thread.daemon = True
            self.theme_thread.start()
        
            # Rotation des médaillons    
            med_thread = threading.Thread(target=self.objet_rotate)
            med_thread.daemon = True
            med_thread.start()
    
    def set_room(self, nb_room):
        self.nb_room = nb_room
        self.texture.nb_room = nb_room
        level = levels.get(nb_room)
        self.room = level[0]
        self.size_room = (len(self.room[0]), len(self.room))
        
        self.player_position = level[1] # Position initial du joueur
        self.player_x = self.player_position[0] + .5
        self.player_y = self.player_position[1]
        self.player_z = self.player_position[2] - .5
        self.camera.position = (self.player_x, self.player_y, self.player_z)
        
        self.texture.delete_theme()
        self.texture.load_theme()
    
    def set_player_position(self):
        self.player_x = self.camera.position[0]
        self.player_y = self.camera.position[1]
        self.player_z = self.camera.position[2]
        self.player = {
            "player_nb_room" : self.nb_room,
            "player_position" : self.player_position,
            "player_coord" : (self.player_x, self.player_y, self.player_z),
            "player_orientation" : self.player_orientation,
            "player_nb_medaillon": self.player_nb_medaillon,
        }
    
    def set_player_orientation(self, angle):
        self.player_orientation += angle
        if self.player_orientation >= 360: self.player_orientation -= 360
        elif self.player_orientation < 0: self.player_orientation += 360
    
    def set_token_id(self, id):
        self.token_id = id
    
    def move_test(self, avance):
        out_room = 0
        block = False
        
        el_actuel = self.room[int(self.player_z+1)][int(self.player_x)] # Elément sur ma position
        # print("ma position:", el_actuel, "x:",int(self.player_x), "z:",int(self.player_z+1), "Orientation:", self.camera.rotate_angle)
        
        try:
            z_plus = self.room[int(self.player_z+1.8)][int(self.player_x)] # Elément Arrière (de la scene) par rapport à ma position
        except:
            if self.nb_room != 0:
                z_plus = "rm-0"
        
        if self.player_z+.2 >= 0:
            z_moins = self.room[int(self.player_z+.2)][int(self.player_x)] # Elément Avant (de la scene) par rapport à ma position
        else:
            if self.nb_room != 0:
                z_moins = "rm-0"
        
        try:
            x_plus = self.room[int(self.player_z+1)][int(self.player_x+.8)] # Elément Droite (de la scene) par rapport à ma position
        except:
            if self.nb_room != 0:
                x_plus = "rm-0"
        
        if int(self.player_x-.2) >= 0:
            x_moins = self.room[int(self.player_z+1)][int(self.player_x-.2)] # Elément Gauche (de la scene) par rapport à ma position
        else:
            if self.nb_room != 0:
                x_moins = "rm-0"
        
        if el_actuel.split('-')[0] == "sl" or el_actuel.split('-')[0] == "ch": # Si je suis sur le sol
            out_room = -1
            
            if avance < 0: # Si j'avance
                # Labyrinth Avant
                if self.camera.rotate_angle == 90 and self.player_z+1 < int(self.player_z+1)+.2:
                    if z_moins.split('-')[0] != "sl" and z_moins.split('-')[0] != "ch" and z_moins.split('-')[0] != "rm":
                        block = True
                    elif z_moins.split('-')[0] == "rm":
                        out_room = int(z_moins.split('-')[1])
                        return out_room, True                    
                # Labyrinth Arrière
                elif self.camera.rotate_angle == 270 and self.player_z+1 > int(self.player_z+1)+.8:
                    if z_plus.split('-')[0] != "sl" and z_plus.split('-')[0] != "ch" and z_plus.split('-')[0] != "rm":
                        block = True
                    elif z_plus.split('-')[0] == "rm":
                        out_room = int(z_plus.split('-')[1])
                        return out_room, True                    
                # Labyrinth Gauche
                elif self.camera.rotate_angle == 0 and self.player_x < int(self.player_x)+.2:
                    if x_moins.split('-')[0] != "sl" and x_moins.split('-')[0] != "ch" and x_moins.split('-')[0] != "rm":
                        block = True
                    elif x_moins.split('-')[0] == "rm":
                        out_room = int(x_moins.split('-')[1])
                        return out_room, True
                # Labyrinth Droite
                elif self.camera.rotate_angle == 180 and self.player_x > int(self.player_x)+.8:
                    if x_plus.split('-')[0] != "sl" and x_plus.split('-')[0] != "ch" and x_plus.split('-')[0] != "rm":
                        block = True
                    elif x_plus.split('-')[0] == "rm":
                        out_room = int(x_plus.split('-')[1])
                        return out_room, True
                else:
                    block = False
            
            else: # Si je recule (comment veux tu ... ?)
                # Labyrinth Avant
                if self.camera.rotate_angle == 270 and self.player_z+1 < int(self.player_z+1)+.2:
                    if z_moins.split('-')[0] != "sl" and z_moins.split('-')[0] != "ch":
                        block = True
                # Labyrinth Arrière
                elif self.camera.rotate_angle == 90 and self.player_z+1 > int(self.player_z+1)+.8:
                    if z_plus.split('-')[0] != "sl" and z_moins.split('-')[0] != "ch":
                        block = True
                # Labyrinth Gauche
                elif self.camera.rotate_angle == 180 and self.player_x < int(self.player_x)+.2:
                    if x_moins.split('-')[0] != "sl" and z_moins.split('-')[0] != "ch":
                        block = True
                # Labyrinth Droite
                elif self.camera.rotate_angle == 0 and self.player_x > int(self.player_x)+.8:
                    if x_plus.split('-')[0] != "sl" and z_moins.split('-')[0] != "ch":
                        block = True
                else:
                    block = False
        else:
            out_room = 0
            block = True
        
        self.player_position = (int(self.player_x), 0, int(self.player_z+1))
        self.player_orientation = self.camera.rotate_angle
        return out_room, block
        
    # Test collision médaillon
    def collision_test(self, game):
        self.set_token_id(None)
        if game.tokens:
            for token in game.tokens[self.nb_room]:
                dif_x = abs(token[0]+.5 - self.player_x)
                dif_z = abs(token[2]-.5 - self.player_z)
                if dif_x <= self.radius_eyes + self.radius_token and dif_z <= self.radius_eyes + self.radius_token:
                    self.set_token_id(token[3])
        return self.token_id
    
    def set_texture(self, texture):
        self.texture = texture # texture active
    
    def set_med_rotate(self, angle):
        self.med_rotate = angle
    
    def set_med_rotate_axis(self, axis):
        self.med_rotate_axis = axis

    def display_scene(self, game):
        # Formes en fonction de la salle
        value_change = ""
        for y, lig in enumerate(self.room):
            for x, value in enumerate(lig):
                if value_change != value:
                    prefixe_form = value.split('-')[0]
                    if prefixe_form != "  ":
                        nb = int(value.split('-')[-1])
                        
                        if prefixe_form == "sl" or prefixe_form == "sp" or prefixe_form == "ml" or prefixe_form == "cl":
                            self.texture.apply_sols(nb)                            
                        elif prefixe_form == "bl":
                            self.texture.apply_theme(nb)
                        elif prefixe_form == "ch":
                            self.texture.apply_chiffre(nb)
                            self.chiffre_rotate = chiffre_orientation.get(nb)
                        elif prefixe_form == "rm":
                            self.texture.apply_groom(nb)
                            self.chiffre_rotate = chiffre_orientation.get(nb)
                
                self.forms(prefixe_form, (x-self.player_x, -0.5, y-self.player_z))
                value_change = value 
        
        # Médaillons
        if game.tokens:
            for token in game.tokens[self.nb_room]:
                if token:
                    self.texture.apply_chiffre(self.nb_room)
                    cylindre((token[0], -.1, token[2]), (self.player_x, -0.5, self.player_z), self.radius_token, .01, self.med_rotate)
        
        # Joueurs
        if game.players:
            for player in game.players:
                if player.id != game.id:
                    self.texture.apply_eyes(player.id)
                    sphere(player.id, player.player_coord, player.player_orientation, (self.player_x, -0.5, self.player_z), self.radius_eyes, 2), # Oeil de player
        
        # Score Board
        self.texture.apply_sols(1)
        texte3D("Jeton : " + str(self.player_nb_medaillon) + " ", self.player_orientation) # nombre de medaillon

    def forms(self, prefixe_form, coord):
        switcher = {
            "sl": lambda: couloir(coord), # Sol + plafond
            "ml": lambda: cube(coord), # Block mur
            "bl": lambda: cube(coord), # Block image
            "ch": lambda: porte(coord, (.98, .01, .98), self.chiffre_rotate), # Chiffre au sol + plafond
            "rm": lambda: groom(coord, (.5, .5, 0), self.chiffre_rotate, self.nb_room), # Groom aux portes des rooms
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
            print("Niveau non trouvé pour cette salle !")
            
    # Changement de projection des oeuvres à intervals régulier
    def image_random(self, timer=0):
        if timer > 0:
            while True:
                self.random_theme()
                time.sleep(timer)
        else:
            self.random_theme()

    # Rotation d'un objet
    def objet_rotate(self, timer=.1):
        if timer > 0 and self.med_rotate_angle != 0 and self.med_rotate_axis != (0,0,0):
            while True:
                self.set_med_rotate(self.med_rotate + self.med_rotate_angle)
                if self.med_rotate >= 360:
                    self.med_rotate = 0
                time.sleep(timer)

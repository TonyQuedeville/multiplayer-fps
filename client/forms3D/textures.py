"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Textures: liste des textures de forme
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import os
import pygame
from OpenGL.GL import *

from forms3D.levels.level1 import level1

# -----------------------------------------------------------------------------------------------

class Texture():
    def __init__(self, room=0, player_nb=0) -> None:
        self.room = room # Numero d'étage
        
        # Texture des sols
        self.dir_sols = "textures"
        self.sols = [
            "ardoise.jpg",
        ]
        self.sols_id = []
        
        # Texture des eyes des joueurs
        self.dir_eyes = "eyes"
        self.eyes = [
            "eye-1.jpg",
        ] 
        self.eyes_id = []
        
        # Oeuvres du theme d'exposition
        self.dir_theme = ""
        self.theme = []
        self.theme_id = []
        
        # Texture des chiffres
        self.dir_chiffres = "chiffres"
        self.chiffres = [
            "chiffre0.jpg",
            "chiffre1.jpg",
            "chiffre2.jpg",
            "chiffre3.jpg",
            "chiffre4.jpg",
            "chiffre5.jpg",
            "chiffre6.jpg",
            "chiffre7.jpg",
            "chiffre8.jpg",
            "chiffre9.jpg",
        ] 
        self.chiffres_id = []

    # Chargement des sols
    def load_sols(self):
        self.sols_id = self.load_textures(self.dir_sols, self.sols)
    
    # Chargement des yeux des joueurs
    def load_eyes(self):
        self.eyes_id = self.load_textures(self.dir_eyes, self.eyes)
    
    # Chargement des oeuvres en fonction du theme d'exposition
    def load_theme(self):
        if self.room == 0:
            # hall d'accueil
            self.dir_theme = "museum"
        elif self.room == 1:
            # 1ère salle, fusion
            self.dir_theme = "fusion"
        elif self.room == 2:
            # 2ème salle, tableaux
            self.dir_theme = "tableaux"
        elif self.room == 3:
            # 3ème salle, danse
            self.dir_theme = "danse"
        elif self.room == 4:
            # 4ème salle, jump
            self.dir_theme = "jump"
        elif self.room == 5:
            # 5ème salle, abstrait
            self.dir_theme = "abstrait"
        elif self.room == 6:
            # 6ème salle, fantaisie
            self.dir_theme = "fantaisie"
        elif self.room == 7:
            # 7ème salle, noir-et-blanc
            self.dir_theme = "noir-et-blanc"
        elif self.room == 8:
            # 8ème salle, swim
            self.dir_theme = "swim"
        self.read_folder()
        self.theme_id = self.load_textures(self.dir_theme, self.theme)
        
    # Chargement des chiffres
    def load_chiffre(self):
        self.chiffres_id = self.load_textures(self.dir_chiffres, self.chiffres)
    
    # Récuration de la liste des fichiers du theme
    def read_folder(self):
        for root, dirs, files in os.walk("img/" + self.dir_theme):
            self.theme = files
    
    # Chargement des textures
    def load_textures(self, dir, images): 
        textures_id = []
        for img in images:
            textureSurface = pygame.image.load('img/'+ dir + "/" + img)
            textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
            width = textureSurface.get_width()
            height = textureSurface.get_height()

            glEnable(GL_TEXTURE_2D)
            tex_id = glGenTextures(1)
            
            glBindTexture(GL_TEXTURE_2D, tex_id)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

            textures_id.append(tex_id)
            
        return textures_id
    
    # Application des sols
    def apply_sols(self, id):
        glBindTexture(GL_TEXTURE_2D, self.sols_id[id])

    # Application de l'oeil du joueur
    def apply_eyes(self, id):
        glBindTexture(GL_TEXTURE_2D, self.eyes_id[id])
    
    # Application de l'oeuvre
    def apply_theme(self, id):
        glBindTexture(GL_TEXTURE_2D, self.theme_id[id])
        
    # Application des chiffres
    def apply_chiffre(self, id):
        glBindTexture(GL_TEXTURE_2D, self.chiffres_id[id])

# -----------------------------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------------------------

class Texture():
    def __init__(self, nb_room=0, nb_player=1) -> None:
        self.nb_room = nb_room # Numero de la salle
        
        # Texture des sols
        self.dir_sols = "textures"
        self.sols = [
            "ardoise.jpg",
        ]
        self.sols_id = []
        
        # Texture des eyes, joueurs
        self.dir_eyes = "eyes"
        self.eyes = [
            "eye-1.jpg",
            "eye-2.jpg",
            "eye-3.jpg",
            "eye-4.jpg",
        ] 
        self.eyes_id = []
        
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
        
        # Texture des grooms
        self.dir_grooms = "grooms"
        self.grooms = [
            "groom-0.png",
            "groom-1.png",
            "groom-2.png",
            "groom-3.png",
            "groom-4.png",
            "groom-5.png",
            "groom-6.png",
            "groom-7.png",
            "groom-8.png",
        ] 
        self.grooms_id = []
        
        # Oeuvres du theme d'exposition
        self.dir_theme = ""
        self.theme = []
        self.theme_id = []

    # Chargement des sols
    def load_sols(self):
        self.sols_id = self.load_textures(self.dir_sols, self.sols)
    
    # Chargement des yeux des joueurs
    def load_eyes(self):
        self.eyes_id = self.load_textures(self.dir_eyes, self.eyes)
        
    # Chargement des chiffres
    def load_chiffre(self):
        self.chiffres_id = self.load_textures(self.dir_chiffres, self.chiffres)
    
    # Chargement des grooms
    def load_grooms(self):
        self.grooms_id = self.load_textures(self.dir_grooms, self.grooms)
    
    # Chargement des oeuvres en fonction du theme d'exposition
    def load_theme(self):
        if self.nb_room == 0:
            # hall d'accueil
            self.dir_theme = "museum"
        elif self.nb_room == 1:
            # 1ère salle, fusion
            self.dir_theme = "fusion"
        elif self.nb_room == 2:
            # 2ème salle, tableaux
            self.dir_theme = "tableaux"
        elif self.nb_room == 3:
            # 3ème salle, danse
            self.dir_theme = "danse"
        elif self.nb_room == 4:
            # 4ème salle, jump
            self.dir_theme = "jump"
        elif self.nb_room == 5:
            # 5ème salle, abstrait
            self.dir_theme = "abstrait"
        elif self.nb_room == 6:
            # 6ème salle, fantaisie
            self.dir_theme = "fantaisie"
        elif self.nb_room == 7:
            # 7ème salle, noir-et-blanc
            self.dir_theme = "noir-et-blanc"
        elif self.nb_room == 8:
            # 8ème salle, swim
            self.dir_theme = "swim"
            
        if self.dir_theme != "":
            self.read_folder()
            self.theme_id = self.load_textures(self.dir_theme, self.theme)
    
    # Supprimer les textures theme
    def delete_theme(self):
        for texture_id in self.theme_id:
            error = glDeleteTextures(texture_id)
            if error:
                print("Erreur delete_theme:", error)
        self.theme = []
        self.theme_id = []
    
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
    
    # Application des chiffres
    def apply_chiffre(self, id):
        glBindTexture(GL_TEXTURE_2D, self.chiffres_id[id])
    
    # Application des grooms
    def apply_groom(self, id):
        glBindTexture(GL_TEXTURE_2D, self.grooms_id[id])
    
    # Application de l'oeuvre
    def apply_theme(self, id):
        glBindTexture(GL_TEXTURE_2D, self.theme_id[id])

# -----------------------------------------------------------------------------------------------

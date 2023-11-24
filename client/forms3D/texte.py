"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Textes: Texte dans l'espace 3D
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import pygame
from OpenGL.GL import *

# -----------------------------------------------------------------------------------------------
# globals:

# -----------------------------------------------------------------------------------------------

def texte3D(text, x, y, z):
    font = pygame.font.Font("board2D/police/explore.ttf", 24)  # Sélectionnez la police et la taille souhaitées
    text_surface = font.render(text, False, (255, 255, 255))  # Couleur du texte: blanc
    text_surface.set_colorkey((0, 0, 0))  # Définir la couleur noire comme transparente
    text_data = pygame.image.tostring(text_surface, "RGBA", True)

    glPushMatrix()
    glRasterPos3f(x, y, z)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
    glPopMatrix()
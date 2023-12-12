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

def texte3D(text, coord=(-.075, .05, -.1), orientation=90):
    font = pygame.font.Font("board2D/police/explore.ttf", 20)  # Sélectionnez la police et la taille souhaitées
    x,y,z = coord

    text_surface = font.render(text, False, (255, 255, 255))  # Couleur du texte: blanc
    text_surface.set_colorkey((0, 0, 0))  # Définir la couleur noire comme transparente
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    

    glPushMatrix()
    glRotatef((orientation-90)*-1, 0, 1, 0)
    glRasterPos3f(x, y, z)
    glEnable( GL_BLEND )
    glBlendFunc( GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA )
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
    glPopMatrix()
    
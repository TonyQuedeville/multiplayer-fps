"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Forms3D: Sphère
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import random
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
# from OpenGL.GLUT import *


# -----------------------------------------------------------------------------------------------
# globals:

# -----------------------------------------------------------------------------------------------

def sphere(position=(0, 0, 0), radius=0.25, tremblote=0, slices=30, stacks=30, lines=False):        
    sphere_surface = gluNewQuadric()
    gluQuadricTexture(sphere_surface, GL_TRUE)

    glPushMatrix()
    glTranslatef(position[0]+0.5, position[1]+0.5, position[2]-0.5)
    
    glRotatef(50+random.randint(-tremblote, tremblote), 1, 0, 0)
    glRotatef(5+random.randint(-tremblote, tremblote), 0, 1, 0)
    glRotatef(-30+random.randint(-tremblote, tremblote), 0, 0, 1)

    if lines:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    gluSphere(sphere_surface, radius, slices, stacks)

    glPopMatrix()



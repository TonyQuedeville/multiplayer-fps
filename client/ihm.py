"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    IHM: Interface graphique du jeu
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective, gluLookAt
# import pyBullet # simulation physique

from forms3D.camera import Camera
from forms3D.scene import scene
from forms3D.textures import texture1

# -----------------------------------------------------------------------------------------------
# globals:

# Initialisation de PyOpenGL (création d'une surface OpenGL)
surface_opengl = glGenTextures(1) 

# -----------------------------------------------------------------------------------------------
# Pygame : interface 2D

def initIHM():
    camera = Camera()

    rotate_player = False
    i_rot = 0       # Iterateur de rotation
    angle = 0       # Angle de rotation
    
    pygame.init()
    largeur, hauteur = 800, 600
    fenetre_pygame = pygame.display.set_mode((largeur, hauteur), DOUBLEBUF|OPENGL)  # Créez la fenêtre Pygame
    clock = pygame.time.Clock()  # Utilisez une horloge pour contrôler la vitesse de rafraîchissement
    
    # Dessinez la fenêtre Pygame
    fenetre_pygame.fill((255, 255, 255))  # couleur de fond pygame
    
    gluPerspective(60, (largeur/hauteur), 0.1, 50.0)
    glEnable(GL_DEPTH_TEST)
    # glEnable(GL_NORMALIZE)
    # glEnable(GL_COLOR_MATERIAL)

    texture1()   

    # Méthode de deplacement et rotation de la scene
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                
                elif event.key == pygame.K_LEFT:
                    # Gauche
                    if i_rot == 0:
                        angle = -90
                        camera.rotate_camera(angle)
                        i_rot += camera.rotate_speed
                        rotate_player = True
                
                elif event.key == pygame.K_RIGHT:
                    # Droite
                    if i_rot == 0:
                        angle = 90
                        camera.rotate_camera(angle)
                        i_rot += camera.rotate_speed
                        rotate_player = True

                elif event.key == pygame.K_UP:
                    # Avancer
                    camera.move_camera(-.25)
                
                elif event.key == pygame.K_DOWN:
                    # Reculer
                    camera.move_camera(.25)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # Rotation
        if rotate_player:
            print("rotation camera -> position:", camera.position, "lookAt:", camera.lookAt, "rotate_angle:", camera.rotate_angle, "angle:", angle)
            if i_rot > 0:            
                glRotatef(angle/12, 0, 1, 0)
                i_rot -=1            
            else:
                scene(camera.position[0], camera.position[2])
                rotate_player = False
        
        scene(camera.position[0], camera.position[2])
        
        pygame.display.flip()
        clock.tick(50)  # Limitez le framerate à 60 FPS

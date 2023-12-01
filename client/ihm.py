"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    IHM: Interface graphique du jeu
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import numpy as np
import pygame
import threading, time

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective, gluLookAt
# import pyBullet # simulation physique

from forms3D.scene import Scene

# -----------------------------------------------------------------------------------------------
# Pygame : interface 2D

# Changement de projection des oeuvres à intervals régulier
def image_random(scene, timer=0):
    if timer > 0:
        while True:
            scene.random_theme()
            time.sleep(timer)
    else:
        scene.random_theme()

# Rotation d'un objet
def objet_rotate(scene, timer=.1):
    if timer > 0 and scene.med_rotate_angle != 0 and scene.med_rotate_axis != (0,0,0):
        while True:
            scene.set_med_rotate(scene.med_rotate + scene.med_rotate_angle)
            if scene.med_rotate >= 360:
                scene.med_rotate = 0
            time.sleep(timer)

def initIHM():
    # Fenêtre pygame
    pygame.init()
    largeur, hauteur = 1200, 600
    flags = DOUBLEBUF|OPENGL  # Mode 1200x600
    # flags = pygame.FULLSCREEN | pygame.DOUBLEBUF | OPENGL | pygame.HWSURFACE # Mode plein écran
    # Créez la fenêtre Pygame
    fenetre_pygame = pygame.display.set_mode((largeur, hauteur), flags)
    
    # Initialisation Room 0
    scene = Scene(0)

    avance = 0 # Valeur d'avance (recul si < 0)

    rotate_player = False
    i_rot = 0  # Iterateur de rotation
    angle = 0  # Angle de rotation
    
    # Timers de synchronisation
    clock = pygame.time.Clock() # Timer pour la vitesse de rafraîchissement
    last_time = time.time() # Timer pour l'appuis constant sur avance

    # Fenêtre pyOpenGL
    gluPerspective(60, (largeur/hauteur), 0.1, 50.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)
    glEnable(GL_COLOR_MATERIAL)
    
    # Changement aléatoire de projection des oeuvres à intervals régulier
    theme_thread = threading.Thread(target=image_random, args=(scene,))
    theme_thread.daemon = True
    theme_thread.start()
    
    # Rotation des médaillons    
    med_thread = threading.Thread(target=objet_rotate, args=(scene,))
    med_thread.daemon = True
    med_thread.start()

    # Méthode de deplacement et rotation de la scene
    while True:
        # Timer pour l'appuis constant sur avance
        curent_time = time.time()
        delta_time = (curent_time - last_time) 
        last_time = curent_time
        
        # Evenements
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
                        scene.camera.rotate_camera(angle)
                        i_rot += scene.camera.rotate_speed
                        rotate_player = True
                
                elif event.key == pygame.K_RIGHT:
                    # Droite
                    if i_rot == 0:
                        angle = 90
                        scene.camera.rotate_camera(angle)
                        i_rot += scene.camera.rotate_speed
                        rotate_player = True

                elif event.key == pygame.K_UP:
                    # Avancer
                    avance = -1 * delta_time
                
                elif event.key == pygame.K_DOWN:
                    # Reculer
                    avance = 1 * delta_time
                
            elif event.type == pygame.KEYUP:
                avance = 0

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # Rotation
        if rotate_player:
            # print("rotation camera -> position:", camera.position, "lookAt:", camera.lookAt, "rotate_angle:", camera.rotate_angle, "angle:", angle)
            if i_rot > 0:            
                glRotatef(angle/12, 0, 1, 0)
                i_rot -=1            
            else:
                scene.set_player_position()
                rotate_player = False
            
        if avance != 0:
            out_room, block = scene.move_test(avance)
            if not block:
                scene.camera.move_camera(avance)                
                scene.set_player_position()
            elif out_room >= 0 and out_room != scene.nb_room: # Changement de salle
                avance = 0
                scene.set_room(out_room)
                scene.set_player_position()
        
        scene.display_scene()
        
        pygame.display.flip()
        clock.tick(10)  # Limitez le framerate à 50 FPS

"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    IHM: Interface graphique du jeu
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import numpy as np
import pygame
import time
import pickle

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective, gluLookAt
# import pyBullet # simulation physique

from forms3D.scene import Scene

# -----------------------------------------------------------------------------------------------
# Pygame : interface de jeu

def send_sever(scene, serveur_port, serveur_ip, client_socket):
    data = {
            "play" : {
                "player_nb_room" : scene.nb_room,
                "player_position" : scene.player_position,
                "player_coord" : (scene.player_x, scene.player_y, scene.player_z),
                "player_orientation" : scene.player_orientation,
            }
        }
    if serveur_ip and data:
        serialized_data = pickle.dumps(data)
        client_socket.sendto(serialized_data, (serveur_ip, serveur_port))

def initIHM(serveur_port, serveur_ip, client_socket):
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
    
    scene.animations_scene()

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
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return False
                
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
                    avance = -1.5 * delta_time
                
                elif event.key == pygame.K_DOWN:
                    # Reculer
                    avance = 1.5 * delta_time
                
            elif event.type == pygame.KEYUP:
                avance = 0

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # Rotation
        if rotate_player:
            if i_rot > 0:
                glRotatef(angle/12, 0, 1, 0)
                i_rot -=1            
                scene.set_player_orientation(angle/12)
                send_sever(scene, serveur_port, serveur_ip, client_socket)
            else:
                scene.set_player_position()
                send_sever(scene, serveur_port, serveur_ip, client_socket)
                rotate_player = False
        
        if avance != 0:
            out_room, block = scene.move_test(avance)
            if not block:
                scene.camera.move_camera(avance)                
                scene.set_player_position()
                send_sever(scene, serveur_port, serveur_ip, client_socket)
            elif out_room >= 0 and out_room != scene.nb_room: # Changement de salle
                avance = 0
                scene.set_room(out_room)
                scene.random_theme()
                scene.set_player_position()
                send_sever(scene, serveur_port, serveur_ip, client_socket)
        
        scene.display_scene()
        
        pygame.display.flip()
        clock.tick(50)  # Limitez le framerate à 50 FPS

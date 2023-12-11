"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Camera: Vue du joueur
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import numpy as np

# -----------------------------------------------------------------------------------------------

class Camera():
    def __init__(self, position=[1, 0, 1], lookAt=[0, 0, -1], up=[0, 1, 0], speed=0.1, fov=60):
        self.position = position
        self.move = [0, 0, 0]   # Progression de déplacement
        self.lookAt = lookAt    # Point de regard de la camera en degré
        self.rotate = [0, 0, 0] # Progression du point de regard. (rotation)
        self.up = up            # Orientation de la camera
        self.speed = speed      # Vitesse de déplacement de la caméra
        self.rotate_angle = 90  # Direction de la camera : Angle de rotation en degré
        self.angle = 0          # Angle actuel de rotation en degré
        self.rotate_speed = 12  # Vitesse de rotation
        self.fov = fov          # Angle de vue

    def move_camera(self, avance=0):
        x,y,z = self.position
        
        if self.rotate_angle == 0:
            x += avance
            self.move = [avance*self.speed, 0, 0]
        elif self.rotate_angle == 180:
            x -= avance
            self.move = [-avance*self.speed, 0, 0]
        elif self.rotate_angle == 90:
            z += avance
            self.move = [0, 0, avance*self.speed]
        elif self.rotate_angle == 270:
            z -= avance
            self.move = [0, 0, -avance*self.speed]
        
        self.position = [x,y,z]
        self.calcul_rotate_camera(self.rotate_angle)

    def rotate_camera(self, angle=0):
        self.rotate_angle += angle
        if self.rotate_angle >= 360: 
            self.rotate_angle = 0
        if self.rotate_angle < 0: 
            self.rotate_angle = 270
        self.calcul_rotate_camera(angle)

    def calcul_rotate_camera(self, angle):        
        # Calcul du vecteur de direction initial en fonction de l'angle
        direction = np.array([np.cos(np.radians(self.rotate_angle)), 0, -np.sin(np.radians(self.rotate_angle))])
        self.lookAt = self.position + direction
        self.lookAt[0] = round(self.lookAt[0], 1)
        self.lookAt[1] = round(self.lookAt[1], 1)
        self.lookAt[2] = round(self.lookAt[2], 1)
        
        signe = 1
        if angle > 0:
            signe = -1
        self.rotate = [np.sin(np.pi/(self.rotate_speed*2))*signe, 0, -np.cos(np.pi/(self.rotate_speed*2)) ]

    def get_angle(self, lookAt):
        eye = np.array(self.position)  
        center = np.array(lookAt)
        
        direction = center - eye # Vecteur direction de la caméra
        axis_x = np.array([1, 0, 0]) # Vecteur unitaire de l'axe des x
        
        # Calcul de l'angle en degrés entre la direction de la caméra et l'axe des x
        return np.degrees(np.arccos(np.dot(direction, axis_x) / (np.linalg.norm(direction) * np.linalg.norm(axis_x))))




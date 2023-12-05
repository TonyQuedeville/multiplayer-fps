"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Forms3D: Cube
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import math
from OpenGL.GL import *
from forms3D.cube import cube
from forms3D.plane import plane

# -----------------------------------------------------------------------------------------------
def rotate_y(point, angle):
    x, y, z = point
    angle = math.radians(angle)
    new_x = x * math.cos(angle) - z * math.sin(angle)
    new_z = x * math.sin(angle) + z * math.cos(angle)
    return new_x, y, new_z

def groom(position=(0,0,0), size=(.5, .5, 0.01), rotate_angle=0, nb_room=0):
    if nb_room == 0:
        if rotate_angle == 0 or rotate_angle == 180:
            fine_size = size
        else:
            fine_size = (size[2], size[1], size[0])
    elif nb_room == 1 or nb_room == 2 or nb_room == 5 or nb_room == 6:
            fine_size = size
    elif nb_room == 3 or nb_room == 4 or nb_room == 7 or nb_room == 8:
            fine_size = (size[2], size[1], size[0])
        
    cube((position[0], position[1], position[2]), fine_size),
"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Forms3D: Cube
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import math
from OpenGL.GL import *

# -----------------------------------------------------------------------------------------------
def rotate_y(point, angle):
    x, y, z = point
    angle = math.radians(angle)
    new_x = x * math.cos(angle) - z * math.sin(angle)
    new_z = x * math.sin(angle) + z * math.cos(angle)
    return new_x, y, new_z

def cube(position=(0,0,0), size=(0.90, 0.90, 0.90), rotate_angle=0, lines=False):
    decalage_x = (1-size[0]) / 2
    decalage_y = (1-size[1]) / 2
    decalage_z = (1-size[2]) / 2
    x = position[0] + decalage_x
    y = position[1] + decalage_y
    z = position[2] - decalage_z
    
    edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )
    
    verticies = ()
    if rotate_angle == 0 or rotate_angle == 360:
        vertices = (
            (x, y, z),                          # 0
            (x+size[0], y, z),                  # 1
            (x+size[0], y+size[1], z),          # 2
            (x, y+size[1], z),                  # 3
            (x, y, z-size[2]),                  # 4
            (x, y+size[1], z-size[2]),          # 5
            (x+size[0], y+size[1], z-size[2]),  # 6
            (x+size[0], y, z-size[2]),          # 7  
        )
        verticies = vertices
    elif rotate_angle == 90:
        vertices = (
            (x, y, z-size[2]),                  # 4 - 0
            (x, y, z),                          # 0 - 1
            (x, y+size[1], z),                  # 3 - 2
            (x, y+size[1], z-size[2]),          # 5 - 3
            (x+size[0], y, z-size[2]),          # 7 - 4
            (x+size[0], y+size[1], z-size[2]),  # 6 - 5
            (x+size[0], y+size[1], z),          # 2 - 6
            (x+size[0], y, z),                  # 1 - 7
        )
        verticies = vertices
    elif rotate_angle == 180:
        vertices = (
            (x+size[0], y, z-size[2]),          # 7 - 0 
            (x, y, z-size[2]),                  # 4 - 1
            (x, y+size[1], z-size[2]),          # 5 - 2
            (x+size[0], y+size[1], z-size[2]),  # 6 - 3
            (x+size[0], y, z),                  # 1 - 4
            (x+size[0], y+size[1], z),          # 2 - 5
            (x, y+size[1], z),                  # 3 - 6
            (x, y, z),                          # 0 - 7
        )
        verticies = vertices
    elif rotate_angle == -90 or rotate_angle == 270:
        vertices = (
            (x+size[0], y, z),                  # 1 - 0
            (x+size[0], y, z-size[2]),          # 7 - 1
            (x+size[0], y+size[1], z-size[2]),  # 6 - 2
            (x+size[0], y+size[1], z),          # 2 - 3
            (x, y, z),                          # 0 - 4
            (x, y+size[1], z),                  # 3 - 5
            (x, y+size[1], z-size[2]),          # 5 - 6
            (x, y, z-size[2]),                  # 4 - 7
        )
        verticies = vertices
    
    rotated_vertices = [rotate_y(vertex, rotate_angle) for vertex in verticies]
    
    if lines:
        glBegin(GL_LINES)
        for edge in edges:
            glColor3fv((1, 1, 1))
            for vertex in edge:
                glVertex3fv(verticies[vertex])
        glEnd()
    else:
        glBegin(GL_QUADS)
        
        # Face Avant
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(verticies[0])
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(verticies[1])
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(verticies[2])
        glTexCoord2f(0.0, 1.0)
        glVertex3fv(verticies[3])
        
        # # Face Arrière
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(verticies[4])
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(verticies[5])
        glTexCoord2f(0.0, 1.0)
        glVertex3fv(verticies[6])
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(verticies[7])
        
        # Face Dessus
        glTexCoord2f(0.0, 1.0)      
        glVertex3fv(verticies[5])
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(verticies[3])       
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(verticies[2])        
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(verticies[6])
        
        # Face Dessous
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(verticies[4])
        glTexCoord2f(0.0, 1.0)
        glVertex3fv(verticies[7])
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(verticies[1])
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(verticies[0])
        
        # # Face Droite 
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(verticies[7])
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(verticies[6])
        glTexCoord2f(0.0, 1.0)
        glVertex3fv(verticies[2])
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(verticies[1])
        
        # # Face Gauche
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(verticies[4])       
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(verticies[0])       
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(verticies[3])      
        glTexCoord2f(0.0, 1.0)
        glVertex3fv(verticies[5])
        
        glEnd()

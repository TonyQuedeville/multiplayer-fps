"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Forms3D: Cylindre
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import math
from OpenGL.GL import *
# -----------------------------------------------------------------------------------------------

def cylindre(position=(0, 0, 0), macoord=(0,0,0), radius=1, height=1, rotate_angle=0, sides=60):
    x, y, z = position
    x = x+0.5 - macoord[0]
    # y = y
    z = z-0.5 - macoord[2]
    vertices = []
    step = 2 * math.pi / sides

    # Générer les points pour les côtés du cylindre
    for i in range(sides + 1):
        angle = i * step + rotate_angle  # Inclure l'angle de rotation
        
        rotated_x = x + radius * math.cos(angle + rotate_angle)  # Appliquer la rotation autour de l'axe
        rotated_y = y 
        rotated_z = z + radius * math.sin(angle + rotate_angle)
        vertices.append((rotated_x, rotated_y, rotated_z))
        
        rotated_x_top = x + radius * math.cos(angle + rotate_angle)
        rotated_y_top = y 
        rotated_z_top = z + radius * math.sin(angle + rotate_angle)
        vertices.append((rotated_x_top, rotated_y_top + height, rotated_z_top))
    
    # Dessiner les côtés du cylindre horizontal
    glBegin(GL_QUAD_STRIP)
    for i in range(len(vertices)):
        angle_ratio = i / sides
        glTexCoord2f(1.0 - angle_ratio, 0.0)
        glVertex3f(vertices[i][0], rotated_y, vertices[i][2])
        glTexCoord2f(1.0 - angle_ratio, 1.0)
        glVertex3f(vertices[i][0], rotated_y + height, vertices[i][2])
    glEnd()

    # Disque du dessus
    glBegin(GL_TRIANGLE_FAN)
    glTexCoord2f(0.5, 0.5)
    glVertex3f(x, y, z)  # Centre du cercle de la base inférieure
    for i in range(len(vertices)):
        glTexCoord2f(0.5 * math.cos(i * step) + 0.5, 0.5 * math.sin(i * step) + 0.5)
        glVertex3f(vertices[i][0], rotated_y, vertices[i][2])  # Point sur le cercle de la base inférieure
    glEnd()

    # Disque du dessous
    glBegin(GL_TRIANGLE_FAN)
    glTexCoord2f(0.5, 0.5)
    glVertex3f(x, y + height, z)  # Centre du cercle de la base supérieure
    for i in range(len(vertices)):
        glTexCoord2f(0.5 * math.cos(i * step) + 0.5, 0.5 * math.sin(i * step) + 0.5)
        glVertex3f(vertices[i][0], rotated_y + height, vertices[i][2])  # Point sur le cercle de la base supérieure
    glEnd()


def disque(position=(0, 0, -.1), orientation=90, radius=.0004, sides=30):
    x = position[0] / 1000 + .0783
    y = position[1] / -1000 -.0316
    z = position[2]
    vertices = []
    step = 2 * math.pi / sides

    # Générer les points pour les côtés du disque
    for i in range(sides + 1):
        angle = i * step 
        
        rotated_x = x + radius * math.cos(angle) 
        rotated_y = y + radius * math.sin(angle)
        rotated_z = z 
        vertices.append((rotated_x, rotated_y, rotated_z))
    
    # Disque
    glPushMatrix()
    glRotatef((orientation-90)*-1, 0, 1, 0)
    
    glBegin(GL_TRIANGLE_FAN)
    glTexCoord2f(0.5, 0.5)
    glVertex3f(x, y, z)  # Centre du cercle de la base inférieure
    
    for vertex in vertices:
        glTexCoord2f(0.5 + 0.5 * vertex[0] / radius, 0.5 + 0.5 * vertex[2] / radius)
        glVertex3f(vertex[0], vertex[1], vertex[2])  # Sommets du cercle
    glEnd()
    
    glPopMatrix()
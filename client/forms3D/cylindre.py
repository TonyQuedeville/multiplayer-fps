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

def cylindre(position=(0, 0, 0), radius=1, height=1, rotate_angle=0, sides=60):
    x, y, z = position
    x = x+0.5
    y = y
    z = z-0.5
    vertices = []
    step = 2 * math.pi / sides

    # Générer les points pour les côtés du cylindre
    for i in range(sides + 1):
        angle = i * step + rotate_angle  # Inclure l'angle de rotation
        rotated_x = x + radius * math.cos(angle + rotate_angle)  # Appliquer la rotation autour de l'axe
        rotated_z = z + radius * math.sin(angle + rotate_angle)
        vertices.append((rotated_x, y, rotated_z))
        
        rotated_x_top = x + radius * math.cos(angle + rotate_angle)
        rotated_z_top = z + radius * math.sin(angle + rotate_angle)
        vertices.append((rotated_x_top, y + height, rotated_z_top))
    
    # Dessiner les côtés du cylindre horizontal
    glBegin(GL_QUAD_STRIP)
    for i in range(len(vertices)):
        angle_ratio = i / sides
        glTexCoord2f(angle_ratio, 0.0)
        glVertex3f(vertices[i][0], y, vertices[i][2])

        glTexCoord2f(angle_ratio, 1.0)
        glVertex3f(vertices[i][0], y + height, vertices[i][2])
    glEnd()

    # Dessiner les cercles pour fermer le cylindre horizontal
    glBegin(GL_TRIANGLE_FAN)
    glTexCoord2f(0.5, 0.5)
    glVertex3f(x, y, z)  # Centre du cercle de la base inférieure
    for i in range(len(vertices)):
        glTexCoord2f(0.5 * math.cos(i * step) + 0.5, 0.5 * math.sin(i * step) + 0.5)
        glVertex3f(vertices[i][0], y, vertices[i][2])  # Point sur le cercle de la base inférieure
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glTexCoord2f(0.5, 0.5)
    glVertex3f(x, y + height, z)  # Centre du cercle de la base supérieure
    for i in range(len(vertices)):
        glTexCoord2f(0.5 * math.cos(i * step) + 0.5, 0.5 * math.sin(i * step) + 0.5)
        glVertex3f(vertices[i][0], y + height, vertices[i][2])  # Point sur le cercle de la base supérieure
    glEnd()

def cylindre_creux(position=(0, 0, 0), radius=1, height=1, sides=20):
    x, y, z = position
    y = y+1
    vertices = []
    step = 2 * math.pi / sides

    for i in range(sides):
        angle = i * step
        x_val = x + radius * math.cos(angle)
        z_val = z + radius * math.sin(angle)
        vertices.append((x_val, z_val))

    glBegin(GL_QUAD_STRIP)
    for i in range(len(vertices)):
        angle_ratio = i / sides  # Ratio pour la texture en fonction de l'angle
        glTexCoord2f(angle_ratio, 0.0)
        glVertex3f(vertices[i][0], y, vertices[i][1])
        
        glTexCoord2f(angle_ratio, 1.0)
        glVertex3f(vertices[i][0], y + height, vertices[i][1])
    glEnd()

    # Faces plates
    glBegin(GL_TRIANGLES)
    for i in range(len(vertices)):
        next_index = (i + 1) % sides
        glTexCoord2f(i / sides, 0.0)
        glVertex3f(vertices[i][0], y, vertices[i][1])
        
        glTexCoord2f(i / sides, 1.0)
        glVertex3f(vertices[i][0], y + height, vertices[i][1])

        glTexCoord2f(next_index / sides, 0.0)
        glVertex3f(vertices[next_index][0], y, vertices[next_index][1])
        
        glTexCoord2f(next_index / sides, 1.0)
        glVertex3f(vertices[next_index][0], y + height, vertices[next_index][1])

        glTexCoord2f(next_index / sides, 0.0)
        glVertex3f(vertices[next_index][0], y, vertices[next_index][1])
        
        glTexCoord2f(i / sides, 1.0)
        glVertex3f(vertices[i][0], y + height, vertices[i][1])
    glEnd()

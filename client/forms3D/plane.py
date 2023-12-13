"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Forms3D: Cube
"""

# -----------------------------------------------------------------------------------------------
#  imports:
from OpenGL.GL import *
from forms3D.cube import cube

def porte(position=(0,0,0), size=(.99, 0.01, .99), chiffre_rotate=0):
    cube((position[0], position[1]-.5, position[2]), size, chiffre_rotate),
    cube((position[0], position[1]+.5, position[2]), size, chiffre_rotate+180),

def couloir(position=(0,0,0), size=(.99, 0.01, .99)):
    plane(position, size)
    plane((position[0], position[1] + 1, position[2]), size)

def minimap(position=(0,0,0), size=(.99, 0.01, .99), orientation=90):
    coef = 670
    schema_pos = (.1176 + position[0]/coef, position[2]/-coef -.0475, -.18)
    schema_size = (size[0]/coef, size[2]/coef, .0001)
    glPushMatrix()
    glRotatef((orientation-90)*-1, 0, 1, 0)
    plane(schema_pos, schema_size, orientation) 
    glPopMatrix()

def plane(position=(0,0,0), size=(.99, 0.01, .99), orientation=90, lines=False):
    x= position[0]
    y= position[1]
    z= position[2]
    
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
    
    sols_vertices = (
        (x, y, z),                          # 0
        (x+size[0], y, z),                  # 1
        (x+size[0], y+size[1], z),          # 2
        (x, y+size[1], z),                  # 3
        (x, y, z-size[2]),                  # 4
        (x, y+size[1], z-size[2]),          # 5
        (x+size[0], y+size[1], z-size[2]),  # 6
        (x+size[0], y, z-size[2])           # 7  
    )

    if lines:
        glBegin(GL_LINES)
        for edge in edges:
            glColor3fv((1, 1, 1))
            for vertex in edge:
                glVertex3fv(sols_vertices[vertex])
        glEnd()
    else:
        glBegin(GL_QUADS)
        
        # Face Avant
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(sols_vertices[0])
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(sols_vertices[1])
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(sols_vertices[2])
        glTexCoord2f(0.0, 1.0)
        glVertex3fv(sols_vertices[3])
        
        # # Face Arrière
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(sols_vertices[4])
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(sols_vertices[5])
        glTexCoord2f(0.0, 1.0)
        glVertex3fv(sols_vertices[6])
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(sols_vertices[7])
        
        # Face Dessus
        glTexCoord2f(0.0, 1.0)      
        glVertex3fv(sols_vertices[5])
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(sols_vertices[3])    
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(sols_vertices[2]) 
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(sols_vertices[6])
        
        # Face Dessous
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(sols_vertices[4])
        glTexCoord2f(0.0, 1.0)
        glVertex3fv(sols_vertices[7])
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(sols_vertices[1])
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(sols_vertices[0])
        
        # # Face Droite 
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(sols_vertices[7])
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(sols_vertices[6])
        glTexCoord2f(0.0, 1.0)
        glVertex3fv(sols_vertices[2])
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(sols_vertices[1])
        
        # # Face Gauche
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(sols_vertices[4])   
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(sols_vertices[0])  
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(sols_vertices[3])
        glTexCoord2f(0.0, 1.0)
        glVertex3fv(sols_vertices[5])
        
        glEnd()

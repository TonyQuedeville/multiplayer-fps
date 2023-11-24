"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Forms3D: Cube
"""

# -----------------------------------------------------------------------------------------------
#  imports:
from OpenGL.GL import *

# -----------------------------------------------------------------------------------------------
# globals:

# -----------------------------------------------------------------------------------------------

def cube(position=(0,0,0), size=1, lines=False):
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
    
    verticies = (
        (x-size, y-size, z+size), # 0
        (x+size, y-size, z+size), # 1
        (x+size, y+size, z+size), # 2
        (x-size, y+size, z+size), # 3
        (x-size, y-size, z-size), # 4
        (x-size, y+size, z-size), # 5
        (x+size, y+size, z-size), # 6
        (x+size, y-size, z-size)  # 7  
    )
    
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

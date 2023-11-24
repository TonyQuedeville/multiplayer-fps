"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Forms3D: Sphère
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

# -----------------------------------------------------------------------------------------------
# globals:

# -----------------------------------------------------------------------------------------------

def sphere(position = [0.0, 0.0, 0.0], rayon = 1, divH = 50, divV = 50, rotate = [0,0,1,0], color=[0.0, 0.0, 1.0]):
    # Sphère
    gl.glPushMatrix()
    gl.glTranslatef(*position)
    gl.glRotatef(*rotate)
    gl.glColor3f(*color)
    glut.glutSolidSphere([rayon, divH, divV]) # Rayon, nb de division horizontale, nb de divisions verticales
    gl.glPopMatrix()

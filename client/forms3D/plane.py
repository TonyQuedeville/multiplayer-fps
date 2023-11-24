"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Forms3D: Cube
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

# -----------------------------------------------------------------------------------------------
# globals:

# -----------------------------------------------------------------------------------------------

def plane(position = [0.0, -1.0, 0.0], size = [10.0, 0.1, 10.0], color=[0.2, 0.2, 0.2]):
    # Plan
    gl.glPushMatrix()
    gl.glTranslatef(*position)
    gl.glScalef(*size)  # Largeur, Hauteur, Profondeur
    gl.glColor3f(*color)
    glut.glutSolidCube(1)  
    gl.glPopMatrix()
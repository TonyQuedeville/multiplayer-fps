"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Forms3D: Tétraèdre
"""

# -----------------------------------------------------------------------------------------------
#  imports:
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

# -----------------------------------------------------------------------------------------------
# globals:

# -----------------------------------------------------------------------------------------------

def tetra(position = [0.0, 0.0, 0.0], color=[0.0, 0.0, 1.0]):
    # Tétraèdre
    gl.glPushMatrix()
    gl.glTranslatef(*position)
    gl.glColor3f(*color)
    glut.glutSolidTetrahedron()
    gl.glPopMatrix()

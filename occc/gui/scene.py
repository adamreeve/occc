from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtOpenGL import *

from OpenGL.GL import *


class Scene(QGLWidget):
    """Graphics scene to be controlled by cmgui"""

    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(300, 200)

    def paintGL(self):
        glClearColor(0.2, 0.2, 0.2, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

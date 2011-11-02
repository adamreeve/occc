from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtOpenGL import *

from OpenGL import GL


class Scene(QGLWidget):
    """Graphics scene to be controlled by cmgui"""

    def __init__(self, parent=None):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(300, 200)

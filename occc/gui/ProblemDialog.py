from PySide.QtCore import *
from PySide.QtGui import *

class ProblemDialog(QDialog):
  def __init__(self,parent=None):
    super(ProblemDialog,self).__init__(parent)
    self.setWindowTitle('Create new problem')

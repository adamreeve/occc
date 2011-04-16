"""
Tree view of the OpenCMISS problem setup
"""

from PySide.QtCore import *
from PySide.QtGui import *

class ProblemTree(QTreeView):
  def __init__(self,parent=None):
    super(ProblemTree,self).__init__(parent)

  def createNewProblem(self):
    pass


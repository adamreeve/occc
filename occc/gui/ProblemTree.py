"""
Tree view of the OpenCMISS problem setup
"""

from PySide.QtCore import *
from PySide.QtGui import *

class ProblemTree(QTreeWidget):
  def __init__(self,parent=None):
    super(ProblemTree,self).__init__(parent)
    self.header().close()

  def add_problem(self, problem, name):
    problem_item = QTreeWidgetItem(self, )
    problem_item.setText(0,"{0} ({1})".format(name,problem.problem_type))
    problem_item.setData(0,Qt.UserRole,problem(name))
    self.addTopLevelItem(problem_item)


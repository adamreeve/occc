from PySide.QtCore import *
from PySide.QtGui import *

try:
  from problems import problem_types
except ImportError:
  from ..problems import problem_types

class ProblemDialog(QDialog):
  def __init__(self,parent=None):
    super(ProblemDialog,self).__init__(parent)
    self.setWindowTitle('Create new problem')

    self.nameEdit = QLineEdit(self)
    self.classCombo = QComboBox(self)
    self.typeCombo = QComboBox(self)
    self.subtypeCombo = QComboBox(self)

    minLength=40
    self.classCombo.setMinimumContentsLength(minLength)
    self.typeCombo.setMinimumContentsLength(minLength)
    self.subtypeCombo.setMinimumContentsLength(minLength)

    for problem_class in problem_types.keys():
      self.classCombo.addItem(problem_class,userData=problem_types[problem_class])
    self.classCombo.currentIndexChanged.connect(self.updateTypes)
    self.typeCombo.currentIndexChanged.connect(self.updateSubtypes)
    self.updateTypes()

    nameLabel = QLabel('Simulation &name',self)
    nameLabel.setBuddy(self.nameEdit)
    classLabel = QLabel('Problem &class',self)
    classLabel.setBuddy(self.classCombo)
    typeLabel = QLabel('Problem &type',self)
    typeLabel.setBuddy(self.typeCombo)
    subtypeLabel = QLabel('Problem &subtype',self)
    subtypeLabel.setBuddy(self.subtypeCombo)

    buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
    buttonBox.accepted.connect(self.accept)
    buttonBox.rejected.connect(self.reject)

    nameLayout = QHBoxLayout()
    nameLayout.addWidget(nameLabel)
    nameLayout.addWidget(self.nameEdit)
    classLayout = QHBoxLayout()
    classLayout.addWidget(classLabel)
    classLayout.addWidget(self.classCombo)
    typeLayout = QHBoxLayout()
    typeLayout.addWidget(typeLabel)
    typeLayout.addWidget(self.typeCombo)
    subtypeLayout = QHBoxLayout()
    subtypeLayout.addWidget(subtypeLabel)
    subtypeLayout.addWidget(self.subtypeCombo)

    vlayout = QVBoxLayout()
    vlayout.addLayout(nameLayout)
    vlayout.addLayout(classLayout)
    vlayout.addLayout(typeLayout)
    vlayout.addLayout(subtypeLayout)
    vlayout.addStretch()
    vlayout.addWidget(buttonBox)

    self.setLayout(vlayout)

  def updateTypes(self):
    self.typeCombo.clear()
    for problem_type in self.classCombo.itemData(self.classCombo.currentIndex()).keys():
      self.typeCombo.addItem(problem_type,userData=self.classCombo.itemData(self.classCombo.currentIndex())[problem_type])

  def updateSubtypes(self):
    self.subtypeCombo.clear()
    if self.typeCombo.count() > 0:
      for problem_subtype in self.typeCombo.itemData(self.typeCombo.currentIndex()).keys():
        self.subtypeCombo.addItem(problem_subtype,userData=self.typeCombo.itemData(self.typeCombo.currentIndex())[problem_subtype])


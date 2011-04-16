from PySide.QtCore import *
from PySide.QtGui import *

from models import Problems

class ProblemDialog(QDialog):
  def __init__(self,parent=None):
    super(ProblemDialog,self).__init__(parent)
    self.setWindowTitle('Create new problem')

    self.classCombo = QComboBox(self)
    self.typeCombo = QComboBox(self)
    self.subtypeCombo = QComboBox(self)

    minLength=40
    self.classCombo.setMinimumContentsLength(minLength)
    self.typeCombo.setMinimumContentsLength(minLength)
    self.subtypeCombo.setMinimumContentsLength(minLength)

    for problemClass in Problems.ProblemClasses:
      self.classCombo.addItem(problemClass.name,userData=problemClass)
    self.classCombo.currentIndexChanged.connect(self.updateTypes)
    self.typeCombo.currentIndexChanged.connect(self.updateSubtypes)
    self.updateTypes()

    classLabel = QLabel('Problem &class',self)
    classLabel.setBuddy(self.classCombo)
    typeLabel = QLabel('Problem &type',self)
    typeLabel.setBuddy(self.typeCombo)
    subtypeLabel = QLabel('Problem &subtype',self)
    subtypeLabel.setBuddy(self.subtypeCombo)

    buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
    buttonBox.accepted.connect(self.accept)
    buttonBox.rejected.connect(self.reject)

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
    vlayout.addLayout(classLayout)
    vlayout.addLayout(typeLayout)
    vlayout.addLayout(subtypeLayout)
    vlayout.addStretch()
    vlayout.addWidget(buttonBox)

    self.setLayout(vlayout)

  def updateTypes(self):
    self.typeCombo.clear()
    for problemType in self.classCombo.itemData(self.classCombo.currentIndex()).types:
      self.typeCombo.addItem(problemType.name,userData=problemType)

  def updateSubtypes(self):
    self.subtypeCombo.clear()
    if self.typeCombo.count() > 0:
      for problemSubtype in self.typeCombo.itemData(self.typeCombo.currentIndex()).subtypes:
        self.subtypeCombo.addItem(problemSubtype.name,userData=problemSubtype)


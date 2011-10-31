from PySide.QtCore import *
from PySide.QtGui import *

import Console,ProblemTree,ProblemDialog,JobControl,Scene

class MainWindow(QMainWindow):
  def __init__(self,parent=None):
    super(MainWindow,self).__init__(parent)
    self.setWindowTitle('OpenCMISS Control Centre')

    self.graphicsWindow = Scene.Scene()
    self.setCentralWidget(self.graphicsWindow)

    self.createDocks()
    self.createActions()
    self.createMenus()

  def createDocks(self):
    self.console = Console.Console()
    self.consoleDock = QDockWidget("Console")
    self.consoleDock.setWidget(self.console)

    self.problemTree = ProblemTree.ProblemTree()
    self.problemTreeDock = QDockWidget("Problems")
    self.problemTreeDock.setWidget(self.problemTree)

    self.jobControl = JobControl.JobControl()
    self.jobsDock = QDockWidget("Jobs")
    self.jobsDock.setWidget(self.jobControl)

    self.setCorner(Qt.BottomLeftCorner,Qt.LeftDockWidgetArea)
    self.addDockWidget(Qt.LeftDockWidgetArea,self.problemTreeDock)
    self.addDockWidget(Qt.BottomDockWidgetArea,self.jobsDock)
    self.addDockWidget(Qt.BottomDockWidgetArea,self.consoleDock)
    self.tabifyDockWidget(self.jobsDock, self.consoleDock)
    self.setTabPosition(Qt.BottomDockWidgetArea, QTabWidget.TabPosition.North)

  def createActions(self):
    self.newProblemAction = QAction('&New Problem',self)
    self.newProblemAction.setShortcut('Ctrl+N')
    self.newProblemAction.setStatusTip('Create a new OpenCMISS problem')
    self.newProblemAction.setIcon(QIcon.fromTheme('document-new'))
    self.newProblemAction.triggered.connect(self.createNewProblem)

    self.exitAction = QAction('E&xit',self)
    self.exitAction.setShortcut('Ctrl+Q')
    self.exitAction.setStatusTip('Close the OpenCMISS Controle Centre')
    self.exitAction.setIcon(QIcon.fromTheme('application-exit'))
    self.exitAction.triggered.connect(self.close)

    self.aboutAction = QAction('&About',self)
    self.aboutAction.triggered.connect(self.about)
    self.aboutAction.setIcon(QIcon.fromTheme('help-about'))

  def createMenus(self):
    self.fileMenu = self.menuBar().addMenu('&File')
    self.fileMenu.addAction(self.newProblemAction)
    self.fileMenu.addSeparator()
    self.fileMenu.addAction(self.exitAction)

    self.viewMenu = self.menuBar().addMenu('&View')
    self.viewMenu.addAction(self.problemTreeDock.toggleViewAction())
    self.viewMenu.addAction(self.consoleDock.toggleViewAction())
    self.viewMenu.addAction(self.jobsDock.toggleViewAction())

    self.helpMenu = self.menuBar().addMenu('&Help')
    self.helpMenu.addAction(self.aboutAction)

  def about(self):
    about = QMessageBox.about(self,'About the OpenCMISS Control Centre',
        '<h2>OpenCMISS Control Centre</h2>' \
        '<p>A graphical interface for configuring problems to solve with OpenCMISS, ' \
        'controlling job executation and visualising solutions.</p>')

  def createNewProblem(self):
    problemDialog = ProblemDialog.ProblemDialog(self)
    if problemDialog.exec_():
      self.problemTree.add_problem(problemDialog.subtypeCombo.itemData(problemDialog.subtypeCombo.currentIndex()), problemDialog.nameEdit.text())

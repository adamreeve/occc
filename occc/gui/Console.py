"""
Console widget for running Python commands.

Will eventually provide the ability to do things like manipulating
fields and the graphical view.
"""

from PySide.QtCore import *
from PySide.QtGui import *
import sys
import traceback
import StringIO

class Console(QWidget):
  def __init__(self,parent=None):
    super(Console,self).__init__(parent)

    self.outputLog = QPlainTextEdit()
    self.outputLog.setReadOnly(True)
    self.commandLine = QLineEdit()
    self.runButton = QPushButton("Run")

    vlayout = QVBoxLayout()
    hlayout = QHBoxLayout()
    hlayout.addWidget(self.commandLine)
    hlayout.addWidget(self.runButton)
    vlayout.addWidget(self.outputLog)
    vlayout.addLayout(hlayout)

    self.setLayout(vlayout)

    self.runButton.clicked.connect(self.runCommand)
    self.commandLine.returnPressed.connect(self.runCommand)

    self.history=[]
    self.historyIndex=0
    self.namespace={}

  def runCommand(self):
    command = self.commandLine.text().strip()
    if command != '':
      tb=''
      result=''
      cmdOutput=StringIO.StringIO()
      cmdError=StringIO.StringIO()
      sys.stdout=cmdOutput
      sys.stderr=cmdError
      try:
        result = str(eval(command,self.namespace,self.namespace))
      except SyntaxError:
        try:
          exec command in self.namespace
          result = cmdOutput.getvalue()
          result += cmdError.getvalue()
        except:
          tb = traceback.format_exc()
      except SystemExit:
        pass
      except:
        tb = traceback.format_exc()
      if tb != '':
        tb = tb.strip().split('\n')
        result = '\n'.join(tb[0:1]+tb[4:])
      self.outputLog.appendPlainText('>>> '+command)
      if result != '':
        self.outputLog.appendPlainText(result.strip())
      self.history.append(command)
      self.historyIndex=len(self.history)
      self.commandLine.setText('')
      sys.stdout=sys.__stdout__
      sys.stderr=sys.__stderr__

  def keyPressEvent(self,event):
    if event.key() == Qt.Key_Up:
      if self.historyIndex > 0:
        self.commandLine.setText(self.history[self.historyIndex-1])
        self.historyIndex-=1
    elif event.key() == Qt.Key_Down:
      if self.historyIndex < len(self.history) - 1:
        self.commandLine.setText(self.history[self.historyIndex+1])
        self.historyIndex+=1
      else:
        self.commandLine.setText('')
        self.historyIndex=len(self.history)
    else:
      super(Console,self).keyPressEvent(event)

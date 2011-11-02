import sys
import traceback
import StringIO
from PySide.QtCore import *
from PySide.QtGui import *


class Console(QWidget):
    """Console widget for running Python commands.

    Will eventually provide the ability to do things like manipulating
    fields and the graphical view.
    """

    def __init__(self, parent=None):
        super(Console, self).__init__(parent)

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

        self.runButton.clicked.connect(self.runCommandLine)
        self.commandLine.returnPressed.connect(self.runCommandLine)

        self.history = []
        self.historyIndex = 0
        self.commandRunner = CommandRunner()

        self.commandRunner.finished.connect(self.updateOutput)

    def runCommandLine(self):
        command = self.commandLine.text().strip()
        if command != '':
            if not self.commandRunner.isRunning():
                self.runButton.setDisabled(True)
                self.commandRunner.setCommand(command)
                self.commandRunner.start()

    def updateOutput(self):
        result = self.commandRunner.output
        error = self.commandRunner.error_output
        self.outputLog.appendPlainText('>>> ' + self.commandRunner.command)
        if result != '':
            self.outputLog.appendPlainText(result.strip())
        if error != '':
            self.outputLog.appendPlainText(error.strip())
        self.history.append(self.commandRunner.command)
        self.historyIndex = len(self.history)
        self.runButton.setDisabled(False)
        self.commandLine.setText('')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            if self.historyIndex > 0:
                self.commandLine.setText(self.history[self.historyIndex-1])
                self.historyIndex -= 1
        elif event.key() == Qt.Key_Down:
            if self.historyIndex < len(self.history) - 1:
                self.commandLine.setText(self.history[self.historyIndex + 1])
                self.historyIndex += 1
            else:
                self.commandLine.setText('')
                self.historyIndex = len(self.history)
        else:
            super(Console, self).keyPressEvent(event)


class CommandRunner(QThread):
    """Run commands in the Python interpreter in a separate thread"""

    def __init__(self, parent=None):
        super(CommandRunner, self).__init__(parent)
        self.namespace = {}
        self.command = ''
        self.output = ''
        self.error_output = ''

    def setCommand(self, command):
        self.command = command

    def run(self):
        tb = ''
        self.output = ''
        self.error_output = ''
        cmdOutput = StringIO.StringIO()
        cmdError = StringIO.StringIO()
        sys.stdout = cmdOutput
        sys.stderr = cmdError
        try:
            self.output = str(eval(self.command, self.namespace,
                    self.namespace))
        except SyntaxError:
            try:
                exec self.command in self.namespace
                self.output = cmdOutput.getvalue()
                self.error_output = cmdError.getvalue()
            except:
                tb = traceback.format_exc()
        except SystemExit:
            pass
        except:
            tb = traceback.format_exc()
        if tb != '':
            tb = tb.strip().split('\n')
            self.error_output = '\n'.join(tb[0:1] + tb[4:])
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

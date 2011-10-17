"""
Control starting and stopping simulation jobs
"""

from PySide.QtCore import *
from PySide.QtGui import *

class JobControl(QWidget):
    def __init__(self,parent=None):
        super(JobControl,self).__init__(parent)

        self.jobs_list = QTreeWidget(self)
        self.jobs_list.setColumnCount(3)
        self.jobs_list.setHeaderLabels(["Problem", "Submitted", "Status"])

        self.runButton = QPushButton("Run")
        self.stopButton = QPushButton("Stop")
        self.removeButton = QPushButton("Remove")

        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()

        vlayout.addStretch()
        vlayout.addWidget(self.runButton)
        vlayout.addWidget(self.stopButton)
        vlayout.addWidget(self.removeButton)

        hlayout.addWidget(self.jobs_list)
        hlayout.addLayout(vlayout)

        self.setLayout(hlayout)


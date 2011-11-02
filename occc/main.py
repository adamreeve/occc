#!/usr/bin/env python

import sys
from PySide.QtCore import *
from PySide.QtGui import *

from gui import main_window


def main():
    app = QApplication(sys.argv)
    mainWin = main_window.MainWindow()
    mainWin.show()
    app.exec_()
    sys.exit()


if __name__ == '__main__':
    main()

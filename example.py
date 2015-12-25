from PyQt5 import QtGui, QtWidgets
import sys
import mainframe
class ExampleApp(QtWidgets.QMainWindow, mainframe.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
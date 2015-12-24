#
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QGridLayout, QHBoxLayout, QLabel, QLineEdit,
        QMessageBox, QPushButton, QTextEdit, QVBoxLayout, QWidget)

str = "hi"

class Application(QWidget):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)

        accountLabel = QLabel("Account:")
        self.accountLine = QLineEdit()
        #self.accountLine.setReadOnly(True)
        
        passwordLabel = QLabel("Password:")
        self.passwordLine = QLineEdit()
        #self.passwordLine.setReadOnly(True)
        
        self.submitButton = QPushButton("Log in")
        self.submitButton.show()
        
        mainLayout = QGridLayout()
        mainLayout.addWidget(accountLabel, 0, 0)
        mainLayout.addWidget(self.accountLine, 0, 1)
        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(self.passwordLine, 1, 1)
        mainLayout.addWidget(self.submitButton, 2, 1)
        #self.height = 100
        #self.setFixedSize(self.frameGeometry().height(), self.frameGeometry().width())
        print("{} {} {} {} {}".format(self.size(), self.geometry(), self.frameGeometry(), self.baseSize().width(), self.rect()))

        self.setLayout(mainLayout)
        self.setWindowTitle("Simple Book")
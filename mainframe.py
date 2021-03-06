# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import ui.homepage.displayAuthor as uihome

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 490, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.printAuthorName)
        
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(20, 10, 421, 321))
        self.listView.setStyleSheet("font: 75 italic 14pt \"Agency FB\";")
        self.listView.setObjectName("listView")
        # Create an empty model for the list's data
        self.model = QtGui.QStandardItemModel(self.listView)
        self.item = QtGui.QStandardItem("Item 1")
        # Add a checkbox to it
        self.item.setCheckable(True)
        # Add the item to the model
        self.model.appendRow(self.item)
        self.model.itemChanged.connect(self.on_item_changed)
        # Apply the model to the list view
        self.listView.setModel(self.model)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(510, 10, 256, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Address', 'Phone', 'Salary', 'Male'])
        self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem("Allan"))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 350, 141, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
    
    def printAuthorName(self):
        print("Allan Sung")
        dialog = QtWidgets.QDialog()
        dialog.ui = uihome.Ui_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.exec_()

    def on_item_changed(self, item):
        # If the changed item is not checked, don't bother checking others
        if not item.checkState():
            return
     
        # Loop through the items until you get None, which
        # means you've passed the end of the list
        i = 0
        while self.model.item(i):
            if not self.model.item(i).checkState():
                return
            print(self.model.item(i).text())
            i += 1
        print(i)
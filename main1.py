from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")               
        self.Add_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_it())
        self.Add_pushButton.setGeometry(QtCore.QRect(10, 70, 121, 31))
        self.Add_pushButton.setObjectName("Add_pushButton")
        
        self.Delete_pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.delete_it())
        self.Delete_pushButton_2.setGeometry(QtCore.QRect(140, 70, 151, 31))
        self.Delete_pushButton_2.setObjectName("Delete_pushButton_2")
               
        self.Clear_pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clear_it())      
        self.Clear_pushButton_3.setGeometry(QtCore.QRect(304, 70, 161, 31))
        self.Clear_pushButton_3.setObjectName("Clear_pushButton_3")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 29, 451, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.MY_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.MY_listWidget.setGeometry(QtCore.QRect(10, 110, 461, 192))
        self.MY_listWidget.setObjectName("MY_listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 484, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_it(self):
        # grab from the list
        item = self.lineEdit.text()   # in video additem_linedit instead use LineEdit
        # add item to list
        self.MY_listWidget.addItem(item)
        # clear the item box
        self.lineEdit.setText("")
            
    # delete Item from the list
    def delete_it(self):
        pass
        
    def clear_it(self):
        pass
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TO DO List"))
        self.Add_pushButton.setText(_translate("MainWindow", "ADD Item To list"))
        self.Delete_pushButton_2.setText(_translate("MainWindow", "Delete From the list"))
        self.Clear_pushButton_3.setText(_translate("MainWindow", "Clear =the list"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys

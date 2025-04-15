import sys
from MySQLdb import connect
from PyQt6 import QtCore, QtGui, QtWidgets
from des import *
from DB import db
from congrats import *
from error import *


class Interface(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.enter)
        self.ui.pushButton_2.clicked.connect(self.enter_ssl)
        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]

    def enter(self):
        login = self.ui.lineEdit.text().strip().replace(" ", "")
        pwd = self.ui.lineEdit_2.text().strip().replace(" ", "")
        data = db.auth(login, pwd)
        if data:
            Congrats = QtWidgets.QWidget()
            ui = Ui_Congrats()
            ui.setupUi(Congrats)
            Congrats.show()
            sys.exit(app.exec())
        else:
            errorr = QtWidgets.QWidget()
            ui = Ui_Error()
            ui.setupUi(errorr)
            errorr.show()
            sys.exit(app.exec())

    def enter_ssl(self):
        login = self.ui.lineEdit.text().strip().replace(" ", "")
        pwd = self.ui.lineEdit_2.text().strip().replace(" ", "")
        data = db.auth(login, pwd, SSL_in=True)
        return data


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec())

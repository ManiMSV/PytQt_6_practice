import sys
import random
from PySide6 import QtCore as qtc,QtWidgets as qtw,QtGui as qtg
from UI.login_ui import Ui_w_loginform

class login_form(qtw.QtWidget,Ui_w_loginform):
    def __init__(slef):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = login_form()
    window.show()
    sys.exit(app.exec())


        
import sys
import random
from PySide6 import QtCore as qtc, QtWidgets as qtw, QtGui as qtg

from UI.main_window_ui import Ui_w_mainwindow

class main_window(qtw.QWidget, Ui_w_mainwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec())
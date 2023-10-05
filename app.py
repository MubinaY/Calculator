from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QDial
from PyQt6.QtCore import QRect
from PyQt6.QtGui import QIcon, QPixmap

from sys import argv, exit 
from widgets.calcwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(argv)
    sign = MainWindow()
    sign.setWindowTitle("Mini calculator")
    sign.show()
    exit(app.exec())    
from PyQt6.QtWidgets import QApplication, QMessageBox, QPushButton, QLineEdit, QWidget, QLabel, QCheckBox
from PyQt6 import QtCore, QtGui 

class Mathmini(QWidget):

    def __init__(self, width=400, height=400) -> None:
        super().__init__()
        self.wd = width
        self.hg = height
        self.res = None
        self.ans = None
        self.logo = QLabel(self)
        self.setUI()
        self.nums.textChanged.connect(self.get_input)
        self.answer.clicked.connect(self.get_answer)

    def get_input(self, agrs):
        self.res = agrs
        
    def get_answer(self):
        self.ans = str(eval(self.res)) 
        QMessageBox.information(self, "Answer", self.ans)


    def setUI(self):
        ds_width = QApplication.primaryScreen().size().width()
        ds_height = QApplication.primaryScreen().size().height()
        self.setGeometry(ds_width//2 - self.wd//2, 
                         ds_height//2 - self.hg//2,
                         self.wd, self.hg)
        
        #input
        self.nums = QLineEdit(self)
        self.nums.setGeometry(self.width()//2 - 190, 20, 380, 50)
        self.nums.setPlaceholderText("Input here")

        #answer
        self.answer = QPushButton(self)
        self.answer.setGeometry(self.width()//2 - 190, 80, 380, 50)
        self.answer.setText("Get answer")

        #icon 
        self.logo.setPixmap(QtGui.QPixmap("icons/evaluation.png"))
        self.logo.setGeometry(self.width()//2 - 70, 180, 150, 150)
        self.logo.setScaledContents(True)

        btn_css1 = """
        QPushButton{
        border-radius:5px;
        background-color:blue;
        color:white;
        }
        """
        
        self.answer.setStyleSheet(btn_css1)

       

from sys import argv, exit

if __name__ == "__main__":
    app2 = QApplication(argv)
    ob = Mathmini()
    ob.setWindowTitle("Eval mini calculator")
    ob.show()
    exit(app2.exec())

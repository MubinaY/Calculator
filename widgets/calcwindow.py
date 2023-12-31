# Form implementation generated from reading ui file 'minicalc.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


import typing
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget

class MainWindow(QMainWindow):
        
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.zero.clicked.connect(lambda x: self.btn_clicked('0'))
        self.one.clicked.connect(lambda x: self.btn_clicked('1'))
        self.two.clicked.connect(lambda x: self.btn_clicked('2'))
        self.three.clicked.connect(lambda x: self.btn_clicked('3'))
        self.four.clicked.connect(lambda x: self.btn_clicked('4'))
        self.five.clicked.connect(lambda x: self.btn_clicked('5'))
        self.six.clicked.connect(lambda x: self.btn_clicked('6'))
        self.seven.clicked.connect(lambda x: self.btn_clicked('7'))
        self.eight.clicked.connect(lambda x: self.btn_clicked('8'))
        self.nine.clicked.connect(lambda x: self.btn_clicked('9'))
        self.minus.clicked.connect(lambda x: self.btn_clicked('-'))
        self.plus.clicked.connect(lambda x: self.btn_clicked('+'))
        self.divid.clicked.connect(lambda x: self.btn_clicked('/'))
        self.mult.clicked.connect(lambda x: self.btn_clicked('*'))
        self.dot.clicked.connect(lambda x: self.btn_clicked('.'))
        self.answer.clicked.connect(lambda x: self.btn_clicked('='))
        self.Cbtn.clicked.connect(lambda x: self.btn_clicked('C'))


    def btn_clicked(self, n:str):
        try:
            if n == "=":
                ans = eval(self.lineEdit.text())
                self.lineEdit.setText(str(ans))
            elif n == 'C':
                txt = str(self.lineEdit.text())
                self.lineEdit.setText(txt[:-1])
            else:
                self.lineEdit.setText(self.lineEdit.text() + n)
        except Exception as e:
            self.lineEdit.setText(f"{e}")
            



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 553)
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        MainWindow.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(500, 75))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(181, 181, 181);")
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.VisualMoveStyle)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.Cbtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Cbtn.setMinimumSize(QtCore.QSize(50, 50))
        self.Cbtn.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.Cbtn.setFont(font)
        self.Cbtn.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(15, 15, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 9px\n"
"}")
        self.Cbtn.setAutoExclusive(False)
        self.Cbtn.setFlat(False)
        self.Cbtn.setObjectName("Cbtn")
        self.horizontalLayout_5.addWidget(self.Cbtn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nine = QtWidgets.QPushButton(parent=self.centralwidget)
        self.nine.setMinimumSize(QtCore.QSize(50, 50))
        self.nine.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.nine.setFont(font)
        self.nine.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(15, 15, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 9px\n"
"}")
        self.nine.setAutoExclusive(False)
        self.nine.setFlat(False)
        self.nine.setObjectName("nine")
        self.horizontalLayout.addWidget(self.nine)
        self.eight = QtWidgets.QPushButton(parent=self.centralwidget)
        self.eight.setMinimumSize(QtCore.QSize(50, 50))
        self.eight.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.eight.setFont(font)
        self.eight.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(15, 15, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 9px\n"
"}")
        self.eight.setAutoExclusive(False)
        self.eight.setFlat(False)
        self.eight.setObjectName("eight")
        self.horizontalLayout.addWidget(self.eight)
        self.seven = QtWidgets.QPushButton(parent=self.centralwidget)
        self.seven.setMinimumSize(QtCore.QSize(50, 50))
        self.seven.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.seven.setFont(font)
        self.seven.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(15, 15, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 9px\n"
"}")
        self.seven.setAutoExclusive(False)
        self.seven.setFlat(False)
        self.seven.setObjectName("seven")
        self.horizontalLayout.addWidget(self.seven)
        self.mult = QtWidgets.QPushButton(parent=self.centralwidget)
        self.mult.setMinimumSize(QtCore.QSize(50, 50))
        self.mult.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.mult.setFont(font)
        self.mult.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(15, 15, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 9px\n"
"}")
        self.mult.setAutoExclusive(False)
        self.mult.setFlat(False)
        self.mult.setObjectName("mult")
        self.horizontalLayout.addWidget(self.mult)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.six = QtWidgets.QPushButton(parent=self.centralwidget)
        self.six.setMinimumSize(QtCore.QSize(50, 50))
        self.six.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.six.setFont(font)
        self.six.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(15, 15, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 9px\n"
"}")
        self.six.setAutoExclusive(False)
        self.six.setFlat(False)
        self.six.setObjectName("six")
        self.horizontalLayout_2.addWidget(self.six)
        self.five = QtWidgets.QPushButton(parent=self.centralwidget)
        self.five.setMinimumSize(QtCore.QSize(50, 50))
        self.five.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.five.setFont(font)
        self.five.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(15, 15, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 9px\n"
"}")
        self.five.setAutoExclusive(False)
        self.five.setFlat(False)
        self.five.setObjectName("five")
        self.horizontalLayout_2.addWidget(self.five)
        self.four = QtWidgets.QPushButton(parent=self.centralwidget)
        self.four.setMinimumSize(QtCore.QSize(50, 50))
        self.four.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.four.setFont(font)
        self.four.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(15, 15, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 9px\n"
"}")
        self.four.setAutoExclusive(False)
        self.four.setFlat(False)
        self.four.setObjectName("four")
        self.horizontalLayout_2.addWidget(self.four)
        self.divid = QtWidgets.QPushButton(parent=self.centralwidget)
        self.divid.setMinimumSize(QtCore.QSize(50, 50))
        self.divid.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.divid.setFont(font)
        self.divid.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(15, 15, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 9px\n"
"}")
        self.divid.setAutoExclusive(False)
        self.divid.setFlat(False)
        self.divid.setObjectName("divid")
        self.horizontalLayout_2.addWidget(self.divid)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.three = QtWidgets.QPushButton(parent=self.centralwidget)
        self.three.setMinimumSize(QtCore.QSize(50, 50))
        self.three.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.three.setFont(font)
        self.three.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(15, 15, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 9px\n"
"}")
        self.three.setAutoExclusive(False)
        self.three.setFlat(False)
        self.three.setObjectName("three")
        self.horizontalLayout_3.addWidget(self.three)
        self.two = QtWidgets.QPushButton(parent=self.centralwidget)
        self.two.setMinimumSize(QtCore.QSize(50, 50))
        self.two.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.two.setFont(font)
        self.two.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(15, 15, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 9px\n"
"}")
        self.two.setAutoExclusive(False)
        self.two.setFlat(False)
        self.two.setObjectName("two")
        self.horizontalLayout_3.addWidget(self.two)
        self.one = QtWidgets.QPushButton(parent=self.centralwidget)
        self.one.setMinimumSize(QtCore.QSize(50, 50))
        self.one.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.one.setFont(font)
        self.one.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(15, 15, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 9px\n"
"}")
        self.one.setAutoExclusive(False)
        self.one.setFlat(False)
        self.one.setObjectName("one")
        self.horizontalLayout_3.addWidget(self.one)
        self.plus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.plus.setMinimumSize(QtCore.QSize(50, 50))
        self.plus.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.plus.setFont(font)
        self.plus.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(15, 15, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 9px\n"
"}")
        self.plus.setAutoExclusive(False)
        self.plus.setFlat(False)
        self.plus.setObjectName("plus")
        self.horizontalLayout_3.addWidget(self.plus)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.zero = QtWidgets.QPushButton(parent=self.centralwidget)
        self.zero.setMinimumSize(QtCore.QSize(50, 50))
        self.zero.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.zero.setFont(font)
        self.zero.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(15, 15, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 9px\n"
"}")
        self.zero.setAutoExclusive(False)
        self.zero.setFlat(False)
        self.zero.setObjectName("zero")
        self.horizontalLayout_4.addWidget(self.zero)
        self.dot = QtWidgets.QPushButton(parent=self.centralwidget)
        self.dot.setMinimumSize(QtCore.QSize(50, 50))
        self.dot.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.dot.setFont(font)
        self.dot.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(15, 15, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 9px\n"
"}")
        self.dot.setAutoExclusive(False)
        self.dot.setFlat(False)
        self.dot.setObjectName("minus")
        self.horizontalLayout_4.addWidget(self.dot)
        self.answer = QtWidgets.QPushButton(parent=self.centralwidget)
        self.answer.setMinimumSize(QtCore.QSize(50, 50))
        self.answer.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.answer.setFont(font)
        self.answer.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(15, 15, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 9px\n"
"}")
        self.answer.setAutoExclusive(False)
        self.answer.setFlat(False)
        self.answer.setObjectName("answer")
        self.horizontalLayout_4.addWidget(self.answer)
        self.minus = QtWidgets.QPushButton(parent=self.centralwidget)
        self.minus.setMinimumSize(QtCore.QSize(50, 50))
        self.minus.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        self.minus.setFont(font)
        self.minus.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(15, 15, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(85, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 9px\n"
"}")
        self.minus.setAutoExclusive(False)
        self.minus.setFlat(False)
        self.minus.setObjectName("minus")
        self.horizontalLayout_4.addWidget(self.minus)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Cbtn.setText(_translate("MainWindow", "C"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.mult.setText(_translate("MainWindow", "*"))
        self.six.setText(_translate("MainWindow", "6"))
        self.five.setText(_translate("MainWindow", "5"))
        self.four.setText(_translate("MainWindow", "4"))
        self.divid.setText(_translate("MainWindow", "/"))
        self.three.setText(_translate("MainWindow", "3"))
        self.two.setText(_translate("MainWindow", "2"))
        self.one.setText(_translate("MainWindow", "1"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.dot.setText(_translate("MainWindow", "."))
        self.answer.setText(_translate("MainWindow", "="))
        self.minus.setText(_translate("MainWindow", "-"))



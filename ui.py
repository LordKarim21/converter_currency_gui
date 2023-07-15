# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'curConverter.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):

    def shutprocess(self):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()
            print('Window closed')
        else:
            pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 855)
        MainWindow.setStyleSheet("background-color:")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #22222e;")
        self.centralwidget.setObjectName("centralwidget")

        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(50, 400, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("background-color: #22222e;\n"
                                        "border: 2px solid #f66867;\n"
                                        "border-radius: 30;\n"
                                        "color: white;")
        self.input_amount.setText("")
        self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.output_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.output_amount.setGeometry(QtCore.QRect(50, 560, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.output_amount.setFont(font)
        self.output_amount.setStyleSheet("background-color: #22222e;\n"
                                         ": 2px solid #f66867;\n"
                                         "border-radius: 30;\n"
                                         "color: white;")
        self.output_amount.setText("")
        self.output_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.output_amount.setObjectName("output_amount")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 660, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "\tcolor: white;\n"
                                      "\tbackground-color: #fb5b5d;\n"
                                      "\tborder-radius: 30;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: #fa4244;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")

        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(50, 760, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet("QPushButton {\n"
                                        "\tcolor: white;\n"
                                        "\tbackground-color: #fb5b5d;\n"
                                        "\tborder-radius: 30;\n"
                                        "}")
        self.exitButton.setObjectName("exitButton")
        self.exitButton.clicked.connect(lambda: self.shutprocess())

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 4800, 271))
        self.frame.setStyleSheet("background-color: #fb5b5d")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(140, 80, 191, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("exchanging.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;\n")
        self.label_2.setObjectName("label_2")

        self.input_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.input_currency.setGeometry(QtCore.QRect(50, 320, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_currency.setFont(font)
        self.input_currency.setStyleSheet("background-color: #22222e;\n"
                                          "border: 2px solid #f66867;\n"
                                          "border-radius: 30;\n"
                                          "color: white;")
        self.input_currency.setText("")
        self.input_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.input_currency.setObjectName("input_currency")
        self.output_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.output_currency.setGeometry(QtCore.QRect(50, 480, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.output_currency.setFont(font)
        self.output_currency.setStyleSheet("background-color: #22222e;\n"
                                           "border: 2px solid #f66867;\n"
                                           "border-radius: 30;\n"
                                           "color: white;")
        self.output_currency.setText("")
        self.output_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.output_currency.setObjectName("output_currency")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exitButton.setText(_translate("MainWindow", "EXIT"))
        self.pushButton.setText(_translate("MainWindow", "КОНВЕРТИРУЙ"))
        self.label_2.setText(_translate("MainWindow", "КОНВЕРТЕР ВАЛЮТ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

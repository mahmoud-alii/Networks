from turtle import onclick
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import pickle
import socket
from dataclasses import dataclass
import time
from numpy import array

@dataclass
class question:
    num: int
    Q: str
    a: str
    b: str
    c: str
    d: str
    ans: str

rows, cols = (5, 5)
arr = array([['----------------------------------------------------------------------------------', '----------', '----------', '----------', '----------'], ['----------------------------------------------------------------------------------', '----------', '----------', '----------', '----------'], ['----------------------------------------------------------------------------------', '----------', '----------', '----------', '----------'], ['----------------------------------------------------------------------------------', '----------', '----------', '----------', '----------'], ['----------------------------------------------------------------------------------', '----------', '----------', '----------', '----------']])

s = socket.socket()

port = 12000

s.connect(('127.0.0.1', port))
print(s.recv(1024).decode())

for i in range(5):

    data = s.recv(4096)
    dataVariable = pickle.loads(data)
    k = str('Q' + str(i+1) + '- ' + dataVariable.Q)
    arr[i][0] = k
    print(arr[i][0])
    l = 'a- ' + dataVariable.a
    arr[i][1] = l
    m = 'b- ' + dataVariable.b
    arr[i][2] = m 
    n = 'c- ' + dataVariable.c
    arr[i][3] = n
    o = 'd- ' + dataVariable.d
    arr[i][4] = o
    time.sleep(0.2)

s.close()


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(977, 881)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 50, 471, 31))
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(420, -10, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(212, 82, 255);")
        self.label_6.setObjectName("label_6")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(60, 80, 241, 141))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(30, 20, 281, 31))
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 50, 281, 31))
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 80, 281, 31))
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(30, 110, 281, 31))
        self.radioButton_4.setChecked(False)
        self.radioButton_4.setObjectName("radioButton_4")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(60, 250, 241, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_5.setGeometry(QtCore.QRect(30, 20, 281, 31))
        self.radioButton_5.setChecked(False)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_6.setGeometry(QtCore.QRect(30, 50, 281, 31))
        self.radioButton_6.setChecked(False)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_7.setGeometry(QtCore.QRect(30, 80, 281, 31))
        self.radioButton_7.setChecked(False)
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_8.setGeometry(QtCore.QRect(30, 110, 281, 31))
        self.radioButton_8.setChecked(False)
        self.radioButton_8.setObjectName("radioButton_8")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 220, 471, 31))
        self.label_2.setObjectName("label_2")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(60, 410, 241, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_13 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_13.setGeometry(QtCore.QRect(30, 20, 281, 31))
        self.radioButton_13.setChecked(False)
        self.radioButton_13.setObjectName("radioButton_13")
        self.radioButton_14 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_14.setGeometry(QtCore.QRect(30, 50, 281, 31))
        self.radioButton_14.setChecked(False)
        self.radioButton_14.setObjectName("radioButton_14")
        self.radioButton_15 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_15.setGeometry(QtCore.QRect(30, 80, 281, 31))
        self.radioButton_15.setChecked(False)
        self.radioButton_15.setObjectName("radioButton_15")
        self.radioButton_16 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_16.setGeometry(QtCore.QRect(30, 110, 281, 31))
        self.radioButton_16.setChecked(False)
        self.radioButton_16.setObjectName("radioButton_16")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 380, 471, 31))
        self.label_3.setObjectName("label_3")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(60, 580, 241, 141))
        self.groupBox_4.setObjectName("groupBox_4")
        self.radioButton_17 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_17.setGeometry(QtCore.QRect(30, 20, 281, 31))
        self.radioButton_17.setChecked(False)
        self.radioButton_17.setObjectName("radioButton_17")
        self.radioButton_18 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_18.setGeometry(QtCore.QRect(30, 50, 281, 31))
        self.radioButton_18.setChecked(False)
        self.radioButton_18.setObjectName("radioButton_18")
        self.radioButton_19 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_19.setGeometry(QtCore.QRect(30, 80, 281, 31))
        self.radioButton_19.setChecked(False)
        self.radioButton_19.setObjectName("radioButton_19")
        self.radioButton_20 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_20.setGeometry(QtCore.QRect(30, 110, 281, 31))
        self.radioButton_20.setChecked(False)
        self.radioButton_20.setObjectName("radioButton_20")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 550, 471, 31))
        self.label_4.setObjectName("label_4")
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(60, 740, 241, 141))
        self.groupBox_5.setObjectName("groupBox_5")
        self.radioButton_25 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_25.setGeometry(QtCore.QRect(30, 20, 281, 31))
        self.radioButton_25.setChecked(False)
        self.radioButton_25.setObjectName("radioButton_25")
        self.radioButton_26 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_26.setGeometry(QtCore.QRect(30, 50, 281, 31))
        self.radioButton_26.setChecked(False)
        self.radioButton_26.setObjectName("radioButton_26")
        self.radioButton_27 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_27.setGeometry(QtCore.QRect(30, 80, 281, 31))
        self.radioButton_27.setChecked(False)
        self.radioButton_27.setObjectName("radioButton_27")
        self.radioButton_28 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_28.setGeometry(QtCore.QRect(30, 110, 281, 31))
        self.radioButton_28.setChecked(False)
        self.radioButton_28.setObjectName("radioButton_28")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 710, 471, 31))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(750, 400, 181, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(770, 445, 251, 41))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def on_click(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("Submited Successfully!")
        msgBox.setWindowTitle("Quiz Completed!")
        msgBox.setStandardButtons(QMessageBox.Ok)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            sys.exit(app.exec_())


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Online Quiz"))
        self.label.setText(_translate("Dialog", arr[0][0]))
        self.label_6.setText(_translate("Dialog", "QUIZ"))
        self.groupBox.setTitle(_translate("Dialog", " "))
        self.radioButton.setText(_translate("Dialog", arr[0][1]))
        self.radioButton_2.setText(_translate("Dialog", arr[0][2]))
        self.radioButton_3.setText(_translate("Dialog", arr[0][3]))
        self.radioButton_4.setText(_translate("Dialog", arr[0][4]))
        self.groupBox_2.setTitle(_translate("Dialog", " "))
        self.radioButton_5.setText(_translate("Dialog", arr[1][1]))
        self.radioButton_6.setText(_translate("Dialog", arr[1][2]))
        self.radioButton_7.setText(_translate("Dialog", arr[1][3]))
        self.radioButton_8.setText(_translate("Dialog", arr[1][4]))
        self.label_2.setText(_translate("Dialog", arr[1][0]))
        self.groupBox_3.setTitle(_translate("Dialog", " "))
        self.radioButton_13.setText(_translate("Dialog", arr[2][1]))
        self.radioButton_14.setText(_translate("Dialog", arr[2][2]))
        self.radioButton_15.setText(_translate("Dialog", arr[2][3]))
        self.radioButton_16.setText(_translate("Dialog", arr[2][4]))
        self.label_3.setText(_translate("Dialog", arr[2][0]))
        self.groupBox_4.setTitle(_translate("Dialog", " "))
        self.radioButton_17.setText(_translate("Dialog", arr[3][1]))
        self.radioButton_18.setText(_translate("Dialog", arr[3][2]))
        self.radioButton_19.setText(_translate("Dialog", arr[3][3]))
        self.radioButton_20.setText(_translate("Dialog", arr[3][4]))
        self.label_4.setText(_translate("Dialog", arr[3][0]))
        self.groupBox_5.setTitle(_translate("Dialog", " "))
        self.radioButton_25.setText(_translate("Dialog", arr[4][1]))
        self.radioButton_26.setText(_translate("Dialog", arr[4][2]))
        self.radioButton_27.setText(_translate("Dialog", arr[4][3]))
        self.radioButton_28.setText(_translate("Dialog", arr[4][4]))
        self.label_5.setText(_translate("Dialog", arr[4][0]))
        self.pushButton.setText(_translate("Dialog", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

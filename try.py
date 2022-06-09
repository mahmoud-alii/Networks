from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1077, 943)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 0, 4, 1, 1)
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Answer_btn = QtWidgets.QPushButton(Form)
        self.Answer_btn.setObjectName("Answer_btn")
        self.gridLayout_2.addWidget(self.Answer_btn, 4, 2, 1, 1)
        self.LE_datName = QtWidgets.QLineEdit(Form)
        self.LE_datName.setObjectName("LE_datName")
        self.gridLayout_2.addWidget(self.LE_datName, 7, 1, 1, 1)
        self.label_datName = QtWidgets.QLabel(Form)
        self.label_datName.setObjectName("label_datName")
        self.gridLayout_2.addWidget(self.label_datName, 7, 0, 1, 1)
        self.Question_btn = QtWidgets.QPushButton(Form)
        self.Question_btn.setObjectName("Question_btn")
        self.gridLayout_2.addWidget(self.Question_btn, 1, 2, 1, 1)
        self.LE_TAnswer = QtWidgets.QLineEdit(Form)
        self.LE_TAnswer.setObjectName("LE_TAnswer")
        self.gridLayout_2.addWidget(self.LE_TAnswer, 3, 1, 1, 1)
        self.LE_Answer = QtWidgets.QLineEdit(Form)
        self.LE_Answer.setObjectName("LE_Answer")
        self.gridLayout_2.addWidget(self.LE_Answer, 4, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 8, 0, 1, 4)
        self.label_NQuestion = QtWidgets.QLabel(Form)
        self.label_NQuestion.setObjectName("label_NQuestion")
        self.gridLayout_2.addWidget(self.label_NQuestion, 9, 0, 1, 1)
        self.label_Answer = QtWidgets.QLabel(Form)
        self.label_Answer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_Answer.setTextFormat(QtCore.Qt.AutoText)
        self.label_Answer.setScaledContents(False)
        self.label_Answer.setObjectName("label_Answer")
        self.gridLayout_2.addWidget(self.label_Answer, 4, 0, 1, 1)
        self.LE_NQuestions = QtWidgets.QLineEdit(Form)
        self.LE_NQuestions.setObjectName("LE_NQuestions")
        self.gridLayout_2.addWidget(self.LE_NQuestions, 9, 1, 1, 1)
        self.New_Question_btn = QtWidgets.QPushButton(Form)
        self.New_Question_btn.setObjectName("New_Question_btn")
        self.gridLayout_2.addWidget(self.New_Question_btn, 4, 3, 1, 1)
        self.TAnswer_btn = QtWidgets.QPushButton(Form)
        self.TAnswer_btn.setObjectName("TAnswer_btn")
        self.gridLayout_2.addWidget(self.TAnswer_btn, 3, 2, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 6, 0, 1, 4)
        self.Dat_btn = QtWidgets.QPushButton(Form)
        self.Dat_btn.setObjectName("Dat_btn")
        self.gridLayout_2.addWidget(self.Dat_btn, 7, 2, 1, 1)
        self.label_TAnswer = QtWidgets.QLabel(Form)
        self.label_TAnswer.setObjectName("label_TAnswer")
        self.gridLayout_2.addWidget(self.label_TAnswer, 3, 0, 1, 1)
        self.Generate_btn = QtWidgets.QPushButton(Form)
        self.Generate_btn.setObjectName("Generate_btn")
        self.gridLayout_2.addWidget(self.Generate_btn, 9, 3, 1, 1)
        self.NQuestion_btn = QtWidgets.QPushButton(Form)
        self.NQuestion_btn.setObjectName("NQuestion_btn")
        self.gridLayout_2.addWidget(self.NQuestion_btn, 9, 2, 1, 1)
        self.LE_Question = QtWidgets.QLineEdit(Form)
        self.LE_Question.setToolTipDuration(-1)
        self.LE_Question.setText("")
        self.LE_Question.setObjectName("LE_Question")
        self.gridLayout_2.addWidget(self.LE_Question, 1, 1, 1, 1)
        self.Done_btn = QtWidgets.QPushButton(Form)
        self.Done_btn.setObjectName("Done_btn")
        self.gridLayout_2.addWidget(self.Done_btn, 5, 2, 1, 1)
        self.line_okv2 = QtWidgets.QFrame(Form)
        self.line_okv2.setLineWidth(5)
        self.line_okv2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_okv2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_okv2.setObjectName("line_okv2")
        self.gridLayout_2.addWidget(self.line_okv2, 10, 0, 1, 4)
        self.line_okv1 = QtWidgets.QFrame(Form)
        self.line_okv1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_okv1.setLineWidth(3)
        self.line_okv1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_okv1.setObjectName("line_okv1")
        self.gridLayout_2.addWidget(self.line_okv1, 0, 0, 1, 4)
        self.label_Question = QtWidgets.QLabel(Form)
        self.label_Question.setObjectName("label_Question")
        self.gridLayout_2.addWidget(self.label_Question, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.retranslateUi(Form)
        self.Answer_btn.pressed.connect(self.LE_Answer.clear)
        self.New_Question_btn.clicked.connect(self.LE_Question.clear)
        self.New_Question_btn.clicked.connect(self.LE_TAnswer.clear)
        self.New_Question_btn.clicked.connect(self.LE_Answer.clear)
        self.Generate_btn.clicked.connect(self.LE_NQuestions.clear)
        self.Generate_btn.clicked.connect(self.LE_datName.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kolokvij"))
        self.Answer_btn.setText(_translate("Form", "Enter Answer"))
        self.label_datName.setText(_translate("Form", "Enter the name of the file:"))
        self.Question_btn.setToolTip(_translate("Form", "Pritisnite ovo"))
        self.Question_btn.setText(_translate("Form", "Enter Question"))
        self.label_NQuestion.setText(_translate("Form", "Number of questions in exam:"))
        self.label_Answer.setText(_translate("Form", "Enter all the possible answers:"))
        self.New_Question_btn.setText(_translate("Form", "New Question"))
        self.TAnswer_btn.setText(_translate("Form", "Enter T Answer"))
        self.Dat_btn.setText(_translate("Form", "Enter"))
        self.label_TAnswer.setText(_translate("Form", "Enter the corect answer:"))
        self.Generate_btn.setText(_translate("Form", "Create exam"))
        self.NQuestion_btn.setText(_translate("Form", "Enter"))
        self.LE_Question.setToolTip(_translate("Form", "Unesite pitanje te pritisnite dugme Unesi pitanje"))
        self.Done_btn.setText(_translate("Form", "Done"))
        self.label_Question.setText(_translate("Form", "Enter a question:"))





    def quiz_name(self):
        name = self.LE_datName.text()
        return name

    def question_generator(self):
        question_text = self.LE_Question.text()
        if question_text.lower() == self.New_Question_btn.clicked.connect(self.question_generator):
            return None

        true = self.LE_TAnswer.text()

        answer_dict = []
#        while True:
        answer = self.LE_Answer.text()
#            if answer.lower() == 'stop':
#                break
        answer_dict.append(answer)         
        qapair = (question_text, true, answer_dict) 

        return qapair,print (qapair)

    def question_list_builder(self):
        questions = []
        while True:
            qg_method = self.question_generator()
            if qg_method is None:
                break
            q = (qg_method[0], qg_method[1],qg_method[2]) 
            questions.append(q)
        return questions

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
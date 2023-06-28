
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QFileDialog
import intent_ex as ex
import pandas as pd


class Ui_NLP(object):
    def setupUi(self, NLP):
        NLP.setObjectName("NLP")
        NLP.resize(443, 316)
        NLP.setMinimumSize(QtCore.QSize(443, 316))
        self.verticalLayout = QtWidgets.QVBoxLayout(NLP)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(18, 18, 18, 18)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl = QtWidgets.QLabel(NLP)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbl.setFont(font)
        self.lbl.setObjectName("lbl")
        self.verticalLayout.addWidget(self.lbl)
        self.txt_input = QtWidgets.QLineEdit(NLP)
        self.txt_input.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.txt_input.setFont(font)
        self.txt_input.setObjectName("txt_input")
        self.verticalLayout.addWidget(self.txt_input)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_submit = QtWidgets.QPushButton(NLP)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.btn_submit.setFont(font)
        self.btn_submit.setObjectName("btn_submit")
        self.horizontalLayout.addWidget(self.btn_submit)
        self.btn_csv = QtWidgets.QPushButton(NLP)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_csv.setFont(font)
        self.btn_csv.setObjectName("btn_csv")
        self.horizontalLayout.addWidget(self.btn_csv)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.txt_display = QtWidgets.QTextBrowser(NLP)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_display.setFont(font)
        self.txt_display.setObjectName("txt_display")
        self.verticalLayout.addWidget(self.txt_display)

        self.btn_submit.clicked.connect(self.submit)
        self.btn_csv.clicked.connect(self.open_csv)

        self.retranslateUi(NLP)
        QtCore.QMetaObject.connectSlotsByName(NLP)

    def retranslateUi(self, NLP):
        _translate = QtCore.QCoreApplication.translate
        NLP.setWindowTitle(_translate("NLP", "NLP"))
        self.lbl.setText(_translate("NLP", "Write a Sentence or select a csv file"))
        self.btn_submit.setText(_translate("NLP", "Submit"))
        self.btn_csv.setText(_translate("NLP", "Select CSV File"))


    def submit(self):

        # predit using model
        pos, neg, overall = ex.Start_Extraction(self.txt_input.text(), False).split(":")

        self.txt_display.setText(f"Result:\n\nPositive Keywords: {pos}\nNegative Keywords: {neg}\nOverall Prediction of the Review: {overall}")

    def open_csv(self):

        path = QFileDialog.getOpenFileName(self, 'Open a file', '', 'All Files (*.csv)')

        if path != ('', ''):
            
            file = pd.read_csv(path[0])

            reviews = file.iloc[1:10]["review"]

            for rv in reviews:
                ex.Start_Extraction(rv, True)

            self.txt_display.setText("Output Saved in CSV File")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NLP = QtWidgets.QWidget()
    ui = Ui_NLP()
    ui.setupUi(NLP)
    NLP.show()
    sys.exit(app.exec_())

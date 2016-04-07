# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asd.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)




class Ui_Form(object):

    def delete(self):
        self.secili_indis = self.comboBox.currentIndex()
        self.secili_text = self.comboBox.currentText()
        os.system('apt-get remove '+self.secili_text)


    def list_prog(self):
        os.system('dpkg --get-selections >> proglar.txt')
        proglar = open("proglar.txt", "r")
        self.liste = proglar.readlines()

        for i in range(0, len(self.liste)):
            self.comboBox.addItem(_fromUtf8(""))
        for i in range(0, len(self.liste)):
            self.liste[i] = self.liste[i].replace("\t", "")
        for i in range(0, len(self.liste)):
            self.liste[i] = self.liste[i].replace("install", "")
        for i in range(0, len(self.liste)):
            self.liste[i] = self.liste[i].replace("\n", "")
        for i in range(0, len(self.liste)):
            self.comboBox.setItemText(i, _translate("Form", self.liste[i], None))
        for i in range(0,len(self.liste)):
            item = QtGui.QListWidgetItem()
            self.listWidget.addItem(item)
            item = self.listWidget.item(i)
            item.setText(_translate("Form", self.liste[i], None))
        os.remove('/root/PycharmProjects/untitled/proglar.txt')



    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(550, 355)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(330, 20, 85, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(20, 20, 291, 311))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(340, 60, 191, 33))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(444, 20, 91, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))


        Form.connect(self.pushButton_2, QtCore.SIGNAL("pressed()"), self.list_prog)
        Form.connect(self.pushButton, QtCore.SIGNAL("pressed()"), self.delete)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):

        Form.setWindowTitle(_translate("Form", "Siler Atar v1", None))
        self.pushButton.setText(_translate("Form", "Delete", None))
        self.pushButton_2.setText(_translate("Form", "Run", None))


if __name__ == "__main__":
            app = QtGui.QApplication(sys.argv)
            form = QtGui.QWidget()
            win = Ui_Form()
            win.setupUi(form)
            form.show()
            app.exec_()



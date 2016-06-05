# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deneme4.ui'
#
# Created: Wed Mar 30 13:24:33 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import os
from PyQt4.QtCore import QCoreApplication, Qt
from PyQt4.QtGui import QListWidget, QListWidgetItem, QApplication
import subprocess
from subprocess import call

programListele = subprocess.Popen(['dpkg','--get-selections'], stdout=subprocess.PIPE)
programCikti = programListele.communicate()[0]
listeDuzenle = programCikti.decode("utf-8")
liste=listeDuzenle.split()


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
    def yazdir(self,item):

        self.secildi = str(item.text())
        print(self.secildi)


    def buttonDelete(self,item):

        os.system("gnome-terminal -e 'apt-get remove '"+self.secildi)
        print("Silindi")


    def buttonRefresh(self,item):

        self.listWidget.clear()
        programListele2 = subprocess.Popen(['dpkg','--get-selections'], stdout=subprocess.PIPE)
        programCikti2 = programListele2.communicate()[0]
        listeDuzenle2 = programCikti2.decode("utf-8")
        liste2=listeDuzenle2.split()

        for i in range(0,len(liste2),2):
            self.listWidget.addItem(liste2[i])
        print("Yenilendi")

    def buttonUpdate(self):
        os.system("gnome-terminal -e 'apt-get update '")
        print("Güncellendi")

    def buttonInstall(self,item):
        textYukle = str(self.yukleEdit.text())
        os.system("gnome-terminal -e 'apt-get install '"+textYukle)
        print("Yüklendi")

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(580, 470)
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 401, 401))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.buttonKaldir = QtGui.QPushButton(Form)
        self.buttonKaldir.setGeometry(QtCore.QRect(430, 20, 141, 29))
        self.buttonKaldir.setObjectName(_fromUtf8("buttonKaldir"))
        self.buttonYenile = QtGui.QPushButton(Form)
        self.buttonYenile.setGeometry(QtCore.QRect(430, 100, 141, 29))
        self.buttonYenile.setObjectName(_fromUtf8("buttonYenile"))
        self.buttonGuncelle = QtGui.QPushButton(Form)
        self.buttonGuncelle.setGeometry(QtCore.QRect(430, 200, 141, 29))
        self.buttonGuncelle.setObjectName(_fromUtf8("buttonGuncelle"))
        self.yukleEdit = QtGui.QLineEdit(Form)
        self.yukleEdit.setGeometry(QtCore.QRect(430, 390, 141, 29))
        self.yukleEdit.setObjectName(_fromUtf8("yukleEdit"))
        self.buttonYukle = QtGui.QPushButton(Form)
        self.buttonYukle.setGeometry(QtCore.QRect(430, 350, 141, 29))
        self.buttonYukle.setObjectName(_fromUtf8("buttonGuncelle"))


        for i in range(0,len(liste),2):
            self.listWidget.addItem(liste[i])

        self.listWidget.itemClicked.connect(self.yazdir)

        self.buttonKaldir.clicked.connect(self.buttonDelete)
        self.buttonYenile.clicked.connect(self.buttonRefresh)
        self.buttonGuncelle.clicked.connect(self.buttonUpdate)
        self.buttonYukle.clicked.connect(self.buttonInstall)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Siler Atar v.2", None))
        self.buttonKaldir.setText(_translate("Form", "Delete", None))
        self.buttonYenile.setText(_translate("Form", "Refresh", None))
        self.buttonGuncelle.setText(_translate("Form", "Update", None))
        self.buttonYukle.setText(_translate("Form", "Install", None))
        self.yukleEdit.setText(_translate("Form", "", None))



app = QtGui.QApplication(sys.argv)
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from functools import partial
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(234, 347)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-10, 290, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))

        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 70, 51, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 70, 51, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 70, 51, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 120, 51, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 120, 51, 41))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.pushButton_6 = QtGui.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 120, 51, 41))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

        self.pushButton_7 = QtGui.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 170, 51, 41))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))

        self.pushButton_8 = QtGui.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(90, 170, 51, 41))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))

        self.pushButton_9 = QtGui.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(170, 170, 51, 41))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))

        self.pushButton_10 = QtGui.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(170, 220, 51, 41))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))

        self.pushButton_11 = QtGui.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 220, 51, 41))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))

        self.pushButton_12 = QtGui.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(90, 220, 51, 41))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))

        self.retranslateUi(Dialog)
        # QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(
        #     _fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(
            _fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        okbt = self.buttonBox.button(QtGui.QDialogButtonBox.Ok)
        okbt.clicked.connect(self.ok_function)
        button_list = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5, self.pushButton_6,
                       self.pushButton_7, self.pushButton_8, self.pushButton_9, self.pushButton_10, self.pushButton_11, self.pushButton_12]
        num_list = map(str, range(1, 10)) + ['*', '0', '#']
        for val, bt in zip(num_list, button_list):
            bt.clicked.connect(partial(self.click_action, val))

    def ok_function(self):
        print self.plainTextEdit.toPlainText()

    def click_action(self, x):
        self.plainTextEdit.insertPlainText(x)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialer", None))
        self.pushButton.setText(_translate("Dialog", "1", None))
        self.pushButton_2.setText(_translate("Dialog", "2", None))
        self.pushButton_3.setText(_translate("Dialog", "3", None))
        self.pushButton_4.setText(_translate("Dialog", "5", None))
        self.pushButton_5.setText(_translate("Dialog", "6", None))
        self.pushButton_6.setText(_translate("Dialog", "4", None))
        self.pushButton_7.setText(_translate("Dialog", "7", None))
        self.pushButton_8.setText(_translate("Dialog", "8", None))
        self.pushButton_9.setText(_translate("Dialog", "9", None))
        self.pushButton_10.setText(_translate("Dialog", "#", None))
        self.pushButton_11.setText(_translate("Dialog", "*", None))
        self.pushButton_12.setText(_translate("Dialog", "0", None))

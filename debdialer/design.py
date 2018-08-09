# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designui2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        Dialog.resize(559, 321)
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 60, 541, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.plainTextEdit.setStyleSheet(
            _fromUtf8("background-color: rgb(200, 200, 200); color : rgb(20, 20, 20);"))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 120, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 120, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 170, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 170, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 170, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 220, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(80, 220, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(160, 220, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(160, 270, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_11 = QtGui.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 270, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_12 = QtGui.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(80, 270, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.pushButton_14 = QtGui.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(280, 120, 131, 41))
        self.pushButton_14.setStyleSheet(
            _fromUtf8("background-color: rgb(222, 125, 13); color : black;"))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.pushButton_15 = QtGui.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(280, 170, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(True)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet(
            _fromUtf8("background-color: rgb(46, 166, 60); color : black;"))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.pushButton_16 = QtGui.QPushButton(Dialog)
        self.pushButton_16.setGeometry(QtCore.QRect(420, 120, 131, 41))
        self.pushButton_16.setStyleSheet(
            _fromUtf8("background-color: rgb(222, 125, 13); color : black;"))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 300, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(410, 10, 140, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 300, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_17 = QtGui.QPushButton(Dialog)
        self.pushButton_17.setGeometry(QtCore.QRect(280, 270, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(True)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet(
            _fromUtf8("background-color: rgb(46, 166, 60); color : black;"))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.pushButton_18 = QtGui.QPushButton(Dialog)
        self.pushButton_18.setGeometry(QtCore.QRect(280, 220, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(True)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet(
            _fromUtf8("background-color: rgb(46, 166, 60); color : black;"))
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.pushButton_13 = QtGui.QPushButton(Dialog)
        self.pushButton_13.setGeometry(QtCore.QRect(230, 120, 41, 191))
        self.pushButton_13.setStyleSheet(
            _fromUtf8("background-color: rgb(255, 68, 51); color : black;"))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 10, 41, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialer", None))
        self.plainTextEdit.setPlainText(
            _translate("Dialog", "+91 9988665544", None))
        self.pushButton.setText(_translate("Dialog", "1", None))
        self.pushButton_2.setText(_translate("Dialog", "2 | abc", None))
        self.pushButton_3.setText(_translate("Dialog", "3  | def", None))
        self.pushButton_4.setText(_translate("Dialog", "5  | jkl", None))
        self.pushButton_5.setText(_translate("Dialog", "6 | mno", None))
        self.pushButton_6.setText(_translate("Dialog", "4 | ghi", None))
        self.pushButton_7.setText(_translate("Dialog", "7 | pqrs", None))
        self.pushButton_8.setText(_translate("Dialog", "8 | tuv", None))
        self.pushButton_9.setText(_translate("Dialog", "9 | xyz", None))
        self.pushButton_10.setText(_translate("Dialog", "#", None))
        self.pushButton_11.setText(_translate("Dialog", "*", None))
        self.pushButton_12.setText(_translate("Dialog", "0 | +", None))
        self.pushButton_14.setText(_translate("Dialog",
                                              "Add vcard to Contacts", None))
        self.pushButton_15.setText(_translate("Dialog",
                                              "Open File", None))
        self.pushButton_16.setText(_translate("Dialog",
                                              "Add to Contacts", None))
        self.label.setText(_translate("Dialog", "Location :  NA", None))
        self.label_2.setText(_translate("Dialog", "Carrier : NA", None))
        self.label_3.setText(_translate("Dialog", "Timezone : NA", None))
        self.pushButton_17.setText(_translate(
            "Dialog", "DIAL ON ANDROID PHONE", None))
        self.pushButton_18.setText(_translate(
            "Dialog", "CALL with VoIP/sip", None))
        self.pushButton_13.setText(_translate("Dialog", "DEL", None))
        self.label_4.setText(_translate("Dialog", "  ", None))

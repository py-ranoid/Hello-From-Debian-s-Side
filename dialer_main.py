from PyQt4 import QtGui  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication
from functools import partial
from design2 import Ui_Dialog, _translate
# This file holds our MainWindow and all design related things
# it also keeps events etc that we defined in Qt Designer


class ExampleApp(QtGui.QDialog, Ui_Dialog):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)
        # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined
        self.plainTextEdit.setPlainText(
            _translate("Dialog", "  +91 9119388", None))

        self.btn_list = [self.pushButton_12,  # 0
                         self.pushButton, self.pushButton_2, self.pushButton_3,  # 123
                         self.pushButton_4, self.pushButton_5, self.pushButton_6,  # 456
                         self.pushButton_7, self.pushButton_8, self.pushButton_9,  # 789
                         self.pushButton_11, self.pushButton_10]  # *#
        num_list = map(str, range(0, 10)) + ['*', '#']

        for val, bt in zip(num_list, self.btn_list):
            bt.clicked.connect(partial(self.click_action, val))

        self.object_map = {"NumTextBox": self.plainTextEdit,
                           "NumButtons": self.btn_list,
                           }

    def getDialerNumber(self):
        return self.object_map["NumTextBox"].toPlainText().strip()

    def setDialerNumber(self, x):
        self.object_map["NumTextBox"].setPlainText(x)

    def click_action(self, x):
        self.object_map["NumTextBox"].insertPlainText(x)


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function

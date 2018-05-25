"""
    Middle Layer between the design class and the dialer_main.

    Since the design class is overwritten every time the design changed
    and compiled with QtDesigner, Ui_Dialog_child will inherit the design
    properties and widgets of Ui_Dialog and append functional properties
    to all the elements.
"""

from design2 import Ui_Dialog, _translate


class Ui_Dialog_child(Ui_Dialog):

    def setupUi(self, arg):
        print "Setup"
        # print self.plainTextEdit
        # print super(Ui_Dialog_child, self).plainTextEdit
        super(Ui_Dialog_child, self).setupUi(arg)
        # print super(Ui_Dialog_child, self).plainTextEdit
        self.plainTextEdit.setPlainText(
            _translate("Dialog", "  +91 9119388", None))

        self.object_map = {"NumTextBox": self.plainTextEdit,
                           }
        self.setDialerNumber("HelloWorld")

    def getDialerNumber(self):
        return self.object_map["NumTextBox"].toPlainText().strip()

    def setDialerNumber(self, x):
        self.object_map["NumTextBox"].setPlainText(x)

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

        # okbt = self.buttonBox.button(QtGui.QDialogButtonBox.Ok)
        # okbt.clicked.connect(self.ok_function)
        self.btn_list = [self.pushButton_12,  # 0
                         self.pushButton, self.pushButton_2, self.pushButton_3,  # 123
                         self.pushButton_4, self.pushButton_5, self.pushButton_6,  # 456
                         self.pushButton_7, self.pushButton_8, self.pushButton_9,  # 789
                         self.pushButton_10, , self.pushButton_11]  # *#
        num_list = map(str, range(0, 10)) + ['*', '#']

        for val, bt in zip(num_list, btn_list):
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

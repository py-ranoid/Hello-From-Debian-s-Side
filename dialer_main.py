from PyQt4 import QtGui
import sys
from functools import partial
from design2 import Ui_Dialog, _translate
import argparse
from phonenumbers import parse
from fetch_details import get_timezone, get_carrier, formatNum
from pytz import timezone
from datetime import datetime


class DialerApp(QtGui.QDialog, Ui_Dialog):
    def __init__(self, num):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.objectMapSetup()

        if num is not None:
            self.setDialerNumber(num)

        num_list = map(str, range(0, 10)) + ['*', '#']

        for val, bt in zip(num_list, self.btn_list):
            bt.clicked.connect(partial(self.click_action, val))

        self.object_map["FetchDetails"].clicked.connect(self.setDetails)

    def objectMapSetup(self):
        self.btn_list = [self.pushButton_12,  # 0
                         self.pushButton, self.pushButton_2, self.pushButton_3,  # 123
                         self.pushButton_4, self.pushButton_5, self.pushButton_6,  # 456
                         self.pushButton_7, self.pushButton_8, self.pushButton_9,  # 789
                         self.pushButton_11, self.pushButton_10]  # *#

        self.object_map = {"NumTextBox": self.plainTextEdit,
                           "NumButtons": self.btn_list,
                           "Location": self.label,
                           "Carrier": self.label_2,
                           "Timezone": self.label_3,
                           "FetchDetails": self.pushButton_15
                           }

    def getDialerNumber(self):
        return str(self.object_map["NumTextBox"].toPlainText()).strip()

    def setDialerNumber(self, x):
        self.object_map["NumTextBox"].setPlainText(x)

    def click_action(self, x):
        self.object_map["NumTextBox"].insertPlainText(x)

    def setDetails(self):
        x = parse(self.getDialerNumber())
        self.setTimezone(x)
        self.setCarrier(x)

        formatted = formatNum(x)
        self.setDialerNumber(formatted)

    def setLocation(self, pnum):
        num = self.getDialerNumber()

    def setCarrier(self, pnum):
        carr = get_carrier(pnum)
        self.object_map["Carrier"].setText('Carrier : ' + carr)

    def setTimezone(self, pnum):
        tz = get_timezone(pnum)[0]
        utcdelta = timezone(tz).utcoffset(datetime.now())
        utcoff = str(float(utcdelta.seconds) / 3600)
        self.object_map["Timezone"].setText(
            'Timezone : ' + tz + " | UTC+" + utcoff)


def main(num):
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    # We set the form to be our DialerApp (design)
    form = DialerApp(num)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Arguments for calling dialer_main')
    parser.add_argument("-n", "--num", help="Number", type=str, default=None)
    args = parser.parse_args()
    number = args.num
    main(number)

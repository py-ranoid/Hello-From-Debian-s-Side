from PyQt4 import QtGui
from PyQt4.QtGui import QTextCursor
import sys
from functools import partial
from .design2 import Ui_Dialog
import argparse
from phonenumbers import parse, is_valid_number
from .fetch_details import get_timezone, get_carrier, formatNum, get_country
from pytz import timezone
from datetime import datetime
from pkg_resources import resource_filename


class DialerApp(QtGui.QDialog, Ui_Dialog):
    def __init__(self, num):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.objectMapSetup()

        self.ignore = False
        if num is not None:
            self.setDialerNumber(num)
            self.ignore = False

        self.ignore = False
        num_list = list(map(str, range(0, 10))) + ['*', '#']

        for val, bt in zip(num_list, self.btn_list):
            bt.clicked.connect(partial(self.click_action, val))

        self.object_map["FetchDetails"].clicked.connect(self.setDetails)
        self.object_map["DelButton"].clicked.connect(self.del_action)
        self.object_map['NumTextBox'].textChanged.connect(self.num_changed)
        self.object_map['NumTextBox'].moveCursor(QTextCursor.EndOfLine)
        self.setDetails()

    def num_changed(self):
        if not self.ignore:
            # Critical section
            self.setDetails()
            """
            num = self.getDialerNumber()
            self.setDialerNumber('-' + num)
            """
            self.ignore = False


    # def keyPressEvent(self, event):
    #     print type(event)
    #     if type(event) == QtGui.QKeyEvent:
    #         # here accept the event and do something
    #         print event.key()
    #         event.accept()
    #     else:
    #         event.ignore()

    def objectMapSetup(self):
        self.btn_list = [self.pushButton_12,  # 0
                         self.pushButton, self.pushButton_2, self.pushButton_3,  # 123
                         self.pushButton_6, self.pushButton_4, self.pushButton_5,  # 456
                         self.pushButton_7, self.pushButton_8, self.pushButton_9,  # 789
                         self.pushButton_11, self.pushButton_10]  # *#

        self.object_map = {"NumTextBox": self.plainTextEdit,
                           "NumButtons": self.btn_list,
                           "Location": self.label,
                           "Carrier": self.label_2,
                           "Timezone": self.label_3,
                           "FetchDetails": self.pushButton_15,
                           "DelButton": self.pushButton_13,
                           "Location": self.label,
                           "FlagBox": self.label_4
                           }

    def getDialerNumber(self):
        return str(self.object_map["NumTextBox"].toPlainText()).strip()

    def setDialerNumber(self, x):
        self.ignore = True
        self.object_map["NumTextBox"].setPlainText(x)
        self.object_map['NumTextBox'].moveCursor(QTextCursor.EndOfLine)

    def click_action(self, x):
        self.object_map["NumTextBox"].insertPlainText(x)

    def del_action(self):
        self.setDialerNumber(self.getDialerNumber()[:-1])
        self.ignore = False
        self.num_changed()

    def setCountry(self, pnum, valid):
        default = {"name": "NA", 'code': "NULL"}
        country = get_country(pnum.country_code) if valid else default
        flag_sp = ' ' * 15
        locstring = flag_sp + country['name'] if valid else flag_sp + "NA"
        self.object_map['Location'].setText('Country :' + locstring)
        self.setFlag(country['code'])

    def setFlag(self, code):
        FLAG_PATH = 'resources/flags/' + code + '-32.png'
        FULL_FLAG_PATH = resource_filename(__name__,FLAG_PATH)
        pixmap = QtGui.QPixmap(FULL_FLAG_PATH)
        pixmap = pixmap.scaledToHeight(21)
        self.object_map["FlagBox"].setPixmap(pixmap)

    def setDetails(self):
        number = self.getDialerNumber()
        try:
            x = parse(number)
        except:
            print ("Number Parse error")
            return
        validity = is_valid_number(x)
        self.setTimezone(x, validity)
        self.setCarrier(x, validity)
        self.setCountry(x, validity)
        formatted = formatNum(x)
        self.setDialerNumber(formatted)

    def setLocation(self, pnum):
        num = self.getDialerNumber()

    def setCarrier(self, pnum, valid):
        carr = get_carrier(pnum) if valid else 'NA'
        self.object_map["Carrier"].setText('Carrier : ' + carr)

    def setTimezone(self, pnum, valid):
        if valid:
            tz = get_timezone(pnum)[0] if valid else ''
            utcdelta = timezone(tz).utcoffset(datetime.now())
            utcoff = str(float(utcdelta.seconds) / 3600)
            self.object_map["Timezone"].setText(
                'Timezone : ' + tz + " | UTC+" + utcoff)
        else:
            self.object_map["Timezone"].setText('Timezone : NA')


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
    try:
        main(number)
    except KeyboardInterrupt:
        print ("Interrupt")

from phonenumbers import timezone, carrier, format_number, PhoneNumberFormat
from json import load

import phonenumbers
from pkg_resources import resource_filename

x = phonenumbers.parse("9176119388", "IN")

SOURCE_FILE = 'resources/DialerCodes.json'
SOURCE_FILE_PATH = resource_filename(__name__, SOURCE_FILE)

with open(SOURCE_FILE_PATH) as f:
    CC_dict = load(f)


def get_carrier(x):
    return carrier.name_for_number(x, "en")


def get_timezone(x):
    return timezone.time_zones_for_number(x)


def formatNum(x, national=False):
    if national:
        return format_number(x, PhoneNumberFormat.NATIONAL)
    else:
        return format_number(x, PhoneNumberFormat.INTERNATIONAL)


def get_country(x):
    return CC_dict[str(x)]


"""
formatter = phonenumbers.AsYouTypeFormatter("IN")
formatter.clear()
formatter.input_digit(u'9176119388')


in_number = phonenumbers.parse("9176119388", "IN")
in_number
from phonenumbers import geocoder
geocoder.description_for_number(in_number, "IN")
"""

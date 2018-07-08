from phonenumbers import timezone, carrier, format_number, PhoneNumberFormat, PhoneNumberMatcher
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


def formatNum(x, kind=None):
    if kind:
        if kind == 'national':
            return format_number(x, PhoneNumberFormat.NATIONAL)
        else:
            return format_number(x, PhoneNumberFormat.INTERNATIONAL)
    else:
        return format_number(x, PhoneNumberFormat.E164)


def get_country(x):
    return CC_dict[str(x)]

def parse_file_for_nums(fpath,country_code):
    with open(fpath,'r') as f:
        text = f.read()
    matches = PhoneNumberMatcher(text, country_code)
    return list([formatNum(x.number) for x in matches])

"""
formatter = phonenumbers.AsYouTypeFormatter("IN")
formatter.clear()
formatter.input_digit(u'9176119388')


in_number = phonenumbers.parse("9176119388", "IN")
in_number
from phonenumbers import geocoder
geocoder.description_for_number(in_number, "IN")
"""

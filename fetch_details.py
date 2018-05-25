from phonenumbers import timezone, carrier, format_number, PhoneNumberFormat

import phonenumbers
x = phonenumbers.parse("+919176119388")


def get_carrier(x):
    return carrier.name_for_number(x, "en")


def get_timezone(x):
    return timezone.time_zones_for_number(x)


def formatNum(x):
    return format_number(x, PhoneNumberFormat.INTERNATIONAL)


"""
formatter = phonenumbers.AsYouTypeFormatter("IN")
formatter.clear()
formatter.input_digit(u'9176119388')


in_number = phonenumbers.parse("9176119388", "IN")
in_number
from phonenumbers import geocoder
geocoder.description_for_number(in_number, "IN")
"""

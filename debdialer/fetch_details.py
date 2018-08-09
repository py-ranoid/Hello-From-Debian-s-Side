from phonenumbers import timezone, carrier, format_number, PhoneNumberFormat, PhoneNumberMatcher
from pkg_resources import resource_filename
from datetime import datetime
from json import load
from phonenumbers import parse, is_valid_number
from phonenumbers.phonenumberutil import NumberParseException
from debdialer.utils import get_default_code
from pytz import timezone as pytz_timezone
import sys
loc_setting = None


# Json file mapping dialer codes to countries/
SOURCE_FILE = 'resources/DialerCodes.json'
SOURCE_FILE_PATH = resource_filename(__name__, SOURCE_FILE)
with open(SOURCE_FILE_PATH) as f:
    CC_dict = load(f)


def get_carrier(x):
    """Returns carrier corresponding to given phone number."""
    return carrier.name_for_number(x, "en")


def get_timezone(x):
    return timezone.time_zones_for_number(x)


def formatNum(x, kind=None):
    """Accepts PhoneNumber object and returns formatted number as a string.
    Args:
        kind :  If None, returns number in E164 format'
                else
                    If 'national', return number in NATIONAL format
                    else, return number in INTERNATIONAL format
    """
    if kind:
        if kind == 'national':
            return format_number(x, PhoneNumberFormat.NATIONAL)
        else:
            return format_number(x, PhoneNumberFormat.INTERNATIONAL)
    else:
        return format_number(x, PhoneNumberFormat.E164)


def get_country(x):
    """Returns country details corresponding to given dialer code (x)."""
    return CC_dict[str(x)]


def parse_file_for_nums(fpath, country_code):
    """Accepts a filepath & country_code.
    Returns all valid phonenumbers present in file."""
    with open(fpath, 'r') as f:
        text = f.read()
    print("Parsing", fpath, "for", "numbers. Code :", country_code)
    matches = PhoneNumberMatcher(text, country_code)
    return list([formatNum(x.number) for x in matches])

def getFlagPath(code):
    """Uses a country code to generate flag path. Sets FlagBox to flag."""
    FLAG_PATH = 'resources/flags/' + code + '-32.png'
    FULL_FLAG_PATH = resource_filename(__name__,FLAG_PATH)
    return FULL_FLAG_PATH


def getCountryString(pnum, valid,loc_setting,flag_len=0):
    """Accepts a phone number sets country details.
    If number is invalid, sets country name to NA.
    If country couldn't be determined by prefix, and IP or
    DEBDIALER_COUNTRY variable was used, it mentions the same in brackets.
    Also, sets country flag using country code.

    Args :
        pnum : PhoneNumber object
        valid : bool variable. True when number is valid, else False.
    """
    default = {"name": "NA", 'code': "NULL"}
    country = get_country(pnum.country_code) if valid else default
    flag_sp = ' ' * flag_len
    if valid:
        locstring = flag_sp + country['name']
        if loc_setting:
            locstring += '(' + loc_setting + ')'
    else:
        locstring = flag_sp + "NA"
    flag = getFlagPath(country['code'])
    return ['Country : ' + locstring, flag]


def getDetails(number):
    try:
        x = parse(number)
        loc_setting = None
    except NumberParseException as e:
        if e.error_type == 0:
            ccode, ip = get_default_code()
            if ccode:
                x = parse(number, ccode)
                loc_setting = 'IP' if ip else 'CFG'
            else:
                return
        else:
            print (e.args)
            return
    validity = is_valid_number(x)
    all_parts = []
    all_parts += getTimezoneString(x, validity)
    all_parts += getCarrierString(x, validity)
    all_parts += getCountryString(x, validity)
    all_parts += ['Formatted :'+formatNum(x, 'inter')]
    print ('\n'.join(all_parts))


def getCarrierString(pnum, valid):
    """Get carrier details of number and set in textbox."""
    carr = get_carrier(pnum) if valid else 'NA'
    return ['Carrier : ' + carr]


def getTimezoneString(pnum, valid):
    """If number is valid, display Timezone names and UTC offset.
    Else, set Timezone to NA."""

    if valid:
        tz = get_timezone(pnum)[0] if valid else ''
        utcdelta = pytz_timezone(tz).utcoffset(datetime.now())
        utcoff = (float(utcdelta.seconds) / 3600)+utcdelta.days*24
        utcoff_string = '+'+str(utcoff) if utcoff >=0 else str(utcoff)
        return ['Timezone : ' + tz + " | UTC" + str(utcoff_string)]
    else:
        return ['Timezone : NA']

if __name__ == '__main__':
    optype = sys.argv[1]
    if optype == '-f':
        print ('\n'.join(parse_file_for_nums(sys.argv[2],get_default_code()[0])))
    elif optype == '-p':
        getDetails(sys.argv[2])

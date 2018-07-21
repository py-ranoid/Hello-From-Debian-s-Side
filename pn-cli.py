from phonenumbers import parse, is_valid_number
from phonenumbers.phonenumberutil import NumberParseException
from debdialer.fetch_details import get_timezone, get_carrier, formatNum, get_country, parse_file_for_nums
from debdialer.utils import get_default_code
from debdialer import __path__
from pytz import timezone
from datetime import datetime
import sys
from pkg_resources import resource_filename
loc_setting = None


def getFlagPath(code):
    FLAG_PATH = 'resources/flags/' + code + '-32.png'
    FULL_FLAG_PATH = __path__[0] +'/'+FLAG_PATH
    # FULL_FLAG_PATH = FLAG_PATH
    return 'Flag :' + FULL_FLAG_PATH


def getCountryString(pnum, valid):
    default = {"name": "NA", 'code': "NULL"}
    country = get_country(pnum.country_code) if valid else default
    # flag_sp = ' ' * 20
    flag_sp = ' ' * 0
    if valid:
        locstring = flag_sp + country['name']
        if loc_setting:
            locstring += '(' + loc_setting + ')'
    else:
        locstring = flag_sp + "NA"
    flag = getFlagPath(country['code'])
    return ['Country :' + locstring, flag]


def getDetails(number):
    global loc_setting
    try:
        x = parse(number)
        loc_setting = None
    except NumberParseException as e:
        if e.error_type == 0:
            ccode, ip = get_default_code()
            if ccode:
                x = parse(number, ccode)
                loc_setting = 'IP' if ip else 'ENV'
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
    carr = get_carrier(pnum) if valid else 'NA'
    return ['Carrier : ' + carr]


def getTimezoneString(pnum, valid):
    if valid:
        tz = get_timezone(pnum)[0] if valid else ''
        utcdelta = timezone(tz).utcoffset(datetime.now())
        utcoff = str(float(utcdelta.seconds) / 3600)
        return ['Timezone : ' + tz + " | UTC+" + utcoff]
    else:
        return ['Timezone : NA']

if __name__ == '__main__':
    getDetails(sys.argv[1])

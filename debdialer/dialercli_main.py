from phonenumbers import parse,is_valid_number
from phonenumbers.phonenumberutil import NumberParseException
from .utils import get_default_code
from .fetch_details import getCountryString,getTimezoneString,getCarrierString,formatNum

def dialercli_main(number):
    print ("===")
    getDetails(number)
    print ("===")


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
    all_parts += getCountryString(x, validity,loc_setting)
    all_parts += ['Formatted :'+formatNum(x, 'inter')]
    print (number,"\n================")
    print ('\n'.join(all_parts))

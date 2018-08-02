from phonenumbers import parse,is_valid_number
from phonenumbers.phonenumberutil import NumberParseException
from .utils import get_default_code,parse_vcard
from .fetch_details import getCountryString,getTimezoneString,getCarrierString,formatNum,parse_file_for_nums

LINE = "="*35
def dialercli_num(number):
    getDetails(number)

def dialercli_file(fpath):
    if fpath.strip().endswith('.vcf'):
        name, nums = parse_vcard(fpath)
        print (LINE)
        print ("    ",name,'\n','\t'+'\n\t'.join(nums))
        print (LINE)
    else:
        country_code = get_default_code()
        nums = parse_file_for_nums(fpath,country_code[0])
        print (LINE)
        print ('\t'+'\n\t'.join(nums))
        print (LINE)




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
    country,flag = getCountryString(x, validity,loc_setting)
    all_parts += [country,'Flag\t: '+flag]
    all_parts += ['Formatted : '+formatNum(x, 'inter')]
    print ("================\n",number,"\n================")
    print (('\n'.join(all_parts)).replace(':','\t:'))

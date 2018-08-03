from phonenumbers import parse,is_valid_number
from phonenumbers.phonenumberutil import NumberParseException
from .utils import get_default_code,parse_vcard,sipdial
from .fetch_details import getCountryString,getTimezoneString,getCarrierString,formatNum,parse_file_for_nums
from .kdeconnect_utils import get_devices,check_kdeconnect,dialer_add,dialer_send
from subprocess import check_output,Popen,PIPE

LINE = "="*35
kdeconnect_insalled = check_kdeconnect()
if kdeconnect_insalled:
    devices = get_devices()
    if len(devices) == 0:
        kdeconnect_insalled = False
        devices = None
    else:
        default_device_name = list(devices.keys())[0]

def getDmenu(options=[]):
    dmenu = ['dmenu','-b','-fn','"-xos4-terminus-medium-r-*-*-14-*"']
    echo = ['echo','-e','\n'.join(options)]
    ps = Popen(echo, stdout=PIPE)
    return check_output(dmenu, stdin=ps.stdout).decode().strip()

def dialercli_num(number):
    getDetails(number)
    options = ['exit','dial with sip']
    if kdeconnect_insalled:
        options+=['dial on android','send contact']
    print(LINE)
    if kdeconnect_insalled:
        print ("> Devices :",devices)
    else:
        print ("> No device found / KDE-Connect not installed .",devices)
    print ("> Choose option from dmenu below ")
    choice = getDmenu(options)
    if choice == 'dial on android':
        if kdeconnect_insalled:
            dialer_send(number,devices[default_device_name])
        print ("> Sent notification on Android Device: ",default_device_name)
    elif choice == 'send contact':
        if kdeconnect_insalled:
            print ("> Enter Name for contact : ")
            name = getDmenu()
            dialer_add([number],name,devices[default_device_name])
            print ("> Sent notification on Android Device: ",default_device_name)
    elif choice == 'dial with sip':
        command = sipdial(number,tel=True)
        print ("> Dialing with sip client.("+command+")")
    else:
        print ("> Invalid input : ",choice)

def dialercli_file(fpath):
    if fpath.strip().endswith('.vcf'):
        name, nums = parse_vcard(fpath)
        print (LINE+"\n    "+name+'\n'+'\t'+'\n\t'.join(nums)+'\n'+LINE)
    else:
        country_code = get_default_code()
        nums = parse_file_for_nums(fpath,country_code[0])
        name = None
        print (LINE+'\n\t'+'\n\t'.join(nums)+'\n'+LINE)
    if kdeconnect_insalled:
        options = ['exit','send as contact to android']
        choice = getDmenu(options)
        print ("> Choose option from dmenu below ")
        if choice == 'send as contact to android':
            if name is None:
                print ("> Enter Name for contact : ")
                name = getDmenu()
            dialer_add(nums[:3],name,devices[default_device_name])
            print ("> Sent notification on Android Device: ",default_device_name)

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
    country,flag = getCountryString(x, validity,loc_setting)
    all_parts += [country,'Flag\t: '+flag]
    all_parts += ['Formatted : '+formatNum(x, 'inter')]
    print ("================\n",number,"\n================")
    print (('\n'.join(all_parts)).replace(':','\t:'))

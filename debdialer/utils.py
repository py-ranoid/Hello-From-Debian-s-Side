import os
import json
import vobject
from urllib3 import PoolManager,exceptions

def country_code_mapper(source='./resources/CountryCodes.json', destination='DialerCodes.json'):
    with open(source) as f:
        cclist = json.load(f)
    ccdict = {}
    for d in cclist:
        try:
            ccdict[d['dial_code'].replace(
                '+', '')] = {'code': d['code'], 'name': d['name']}
        except:
            print (d)
    with open(destination, 'w') as f:
        json.dump(ccdict, f)


def check_ip_for_country_code():
    """ Sends a get request to http://ipinfo.io to fetch details about the
    user's country based on Public IP.
    """
    http = PoolManager()
    try :
        r = http.request('GET', 'http://ipinfo.io')
    except exceptions.MaxRetryError:
        return None
    json_resp = json.loads(r.data.decode('utf-8'))
    return json_resp['country']


def get_default_code():
    """Used to fetch default country code if number isn't in E164 format.
    To manually set the default country_code,
        export DEBDIALER_COUNTRY='<2 letter code>'
    For example,
        export DEBDIALER_COUNTRY='US'

    If DEBDIALER_COUNTRY isn't present as an environment variable,
        check user's public IP to predict user's current country.
        (may be misleading if user is using a VPN or
        trying to parse international numbers)

    Returns 2 values:
        result : None, if default country code couldn't be found
        choice : 1, if default country was determined from IP address
                 0, if default country was determined from environment variable.
    """
    default_country = os.environ.get('DEBDIALER_COUNTRY', None)
    if default_country is not None:
        return (default_country,0)
    else:
        ip_result = check_ip_for_country_code()
        if ip_result is not None:
            return (ip_result,1)
    return (None,None)

def parse_vcard(filepath):
    with open(filepath,'r') as vcard_file:
        text = vcard_file.read()
    vcard = vobject.readOne(text)
    name = vcard.getChildValue('fn')
    numbers = [x.value for x in vcard.tel_list]
    return name,numbers

import os
import json
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
    http = PoolManager()
    try :
        r = http.request('GET', 'http://ipinfo.io')
    except exceptions.MaxRetryError:
        return None
    json_resp = json.loads(r.data.decode('utf-8'))
    return json_resp['country']


def get_default_code():
    default_country = os.environ.get('DEBDIALER_COUNTRY', None)
    if default_country is not None:
        return (default_country,0)
    else:
        ip_result = check_ip_for_country_code()
        if ip_result is not None:
            return (ip_result,1)
    return (None,0)

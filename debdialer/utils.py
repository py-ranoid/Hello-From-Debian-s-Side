import json


def country_code_mapper(source='CountryCodes.json', destination='DialerCodes.json'):
    with open(source) as f:
        cclist = json.load(f)
    ccdict = {}
    for d in cclist:
        try:
            ccdict[d['dial_code'].replace(
                '+', '')] = {'code': d['code'], 'name': d['name']}
        except:
            print d
    with open(destination, 'w') as f:
        json.dump(ccdict, f)

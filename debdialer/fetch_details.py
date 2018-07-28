from phonenumbers import timezone, carrier, format_number, PhoneNumberFormat, PhoneNumberMatcher
from pkg_resources import resource_filename
from json import load

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

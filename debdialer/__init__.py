from .dialer_main import main
import argparse

def cli_main():
    """debdialer accepts phone number as optional argument."""
    parser = argparse.ArgumentParser(
        description='Arguments for calling dialer_main')
    parser.add_argument("-n", "--num", dest='num', help="Open Debdialer with phonenumber", type=str, default='9988776655',nargs='?')
    parser.add_argument("-u", "--url", dest='url',help="Open Debdialer with URL", type=str, default='tel:9988776655',nargs='?')
    args = parser.parse_args()
    if args.url:
        url_entered = args.url.strip()
        if url_entered.startswith('tel:'):
            number = url_entered.split(':')[1]
    else:
        number = args.num
    try:
        main(number)
    except KeyboardInterrupt:
        print ("Interrupt")

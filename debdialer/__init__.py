import argparse

def cli_main():
    """debdialer accepts phone number as optional argument."""
    parser = argparse.ArgumentParser(
        description='Arguments for calling dialer_main')
    parser.add_argument("-n", "--num", dest='num', help="Open Debdialer with phonenumber", type=str, default='9988776655',nargs='?')
    parser.add_argument("-u", "--url", dest='url',help="Open Debdialer with URL", type=str, default='tel:9988776655',nargs='?')
    parser.add_argument("-ng", "--no-gui", dest='nogui',help="Open Debdialer with dmenu", action='store_true',default=False)
    args = parser.parse_args()

    if args.url:
        url_entered = args.url.strip()
        if url_entered.startswith('tel:'):
            number = url_entered.split(':')[1]
    else:
        number = args.num
    print ("NO-GUI :",args.nogui)
    if (args.nogui):
        from .dialercli_main import dialercli_main
        dialercli_main(number)
    else:
        from .dialer_main import main
        try:
            main(number)
        except KeyboardInterrupt:
            print ("Interrupt")

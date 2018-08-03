import argparse

def cli_main():
    """debdialer accepts phone number as optional argument."""
    parser = argparse.ArgumentParser(
        description='Arguments for calling dialer_main')
    parser.add_argument("-n", "--num", dest='num', help="Open Debdialer with phonenumber", type=str, default='9988776655')
    parser.add_argument("-u", "--url", dest='url',help="Open Debdialer with URL", type=str, default='tel:9988776655',nargs='?')
    parser.add_argument("-f", "--file", dest='file',help="Parse file for numbers with debdialer", type=str)
    parser.add_argument("-ng", "--no-gui", dest='nogui',help="Open Debdialer with dmenu", action='store_true',default=False)
    args = parser.parse_args()

    if args.file:
        fpath = args.file
        from .dialercli_main import dialercli_file
        dialercli_file(fpath)
        return

    if args.url:
        url_entered = args.url.strip()
        if url_entered.startswith('tel:'):
            number = url_entered.split(':')[1]
        if url_entered.startswith('sip:'):
            from .utils import sipdial
            sipdial(url_entered,sip = True)

    if args.num:
        number = args.num
    if (args.nogui):
        from .dialercli_main import dialercli_num
        dialercli_num(number)
    else:
        try:
            from .dialer_main import main
            main(number)
        except ImportError as e:
            if 'PyQt4' in e.message:
                # If PyQt4, isn't installed, open in no-gui mode
                from .dialercli_main import dialercli_num
                dialercli_num(number)
        except KeyboardInterrupt:
            print ("Interrupt")

from .dialer_main import main
import argparse

def cli_main():
    """debdialer accepts phone number as optional argument."""
    parser = argparse.ArgumentParser(
        description='Arguments for calling dialer_main')
    parser.add_argument("-n", "--num", help="Number", type=str, default=None)
    args = parser.parse_args()
    number = args.num
    try:
        main(number)
    except KeyboardInterrupt:
        print ("Interrupt")

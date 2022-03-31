
import argparse
from sys import exit, stderr
from registrar import app


def main():

    parser = argparse.ArgumentParser(
        description='The registrar application',
        allow_abbrev=False)
    parser.add_argument('port',
                        help='the port at which the server' +
                        ' should listen',
                        type=int)
    args = parser.parse_args()

    try:
        app.run(host='0.0.0.0', port=args.port, debug=True)
    except Exception as ex:
        print(ex, file=stderr)
        exit(1)


if __name__ == '__main__':
    main()

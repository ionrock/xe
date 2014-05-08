import argparse


def get_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('foo')
    return parser.parse_args(args)


def main(args):
    print('HERE')
    args = get_args(args)
    print(args)


if __name__ == '__main__':
    main()

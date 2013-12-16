import argparse
import importlib

from xe.do import run


def get_args():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('action')
    return parser.parse_known_args()


def find_action(name):
    try:
        mod = importlib.import_module('xe.cmds.%s' % name, name)
        return mod.main
    except ImportError:
        return None


def main():
    args, tail = get_args()

    if args.action:
        func = find_action(args.action)
        if func:
            func(tail)
        else:
            tail = ' '.join(tail)
            cmd = '%s %s' % (args.action, tail)
            run(cmd)


if __name__ == '__main__':
    main()

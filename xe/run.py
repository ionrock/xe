import argparse
import importlib

from xe.do import run


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('action')
    return parser.parse_known_args()


def find_action(name):
    try:
        print(name)
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
            cmd = '%s %s' % (args.action, tail or '')
            run(cmd)


if __name__ == '__main__':
    main()

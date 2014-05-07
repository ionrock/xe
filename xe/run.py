import sys
import importlib

from xe.do import run


def find_action(name):
    try:
        mod = importlib.import_module('xe.cmds.%s' % name, name)
        return mod.main
    except ImportError:
        return None


def get_action():
    if len(sys.argv) > 1:
        return sys.argv[1]


def get_tail():
    if len(sys.argv) > 2:
        return sys.argv[2:]
    return []


def main():
    action = get_action()

    if not action:
        sys.exit(0)
        return

    if action:
        func = find_action(action)
        if func:
            func(get_tail())
        else:
            run(sys.argv[1:])


if __name__ == '__main__':
    main()

import argparse
from path import path

from xe import settings
from xe.do import run
from xe.models import Requirements


def get_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clean', action='store_true')
    parser.add_argument('-i', '--index',
                        help='The pypi index to use')
    return parser.parse_args(args)


def main(args):
    args = get_args(args)

    venv = path(settings['VENV'])

    if args.clean and venv.isdir():
        venv.rmtree()

    run(['virtualenv', venv.abspath()])

    # TODO: Allow custom requirement class here
    reqs = Requirements()
    reqs.install(args.index)

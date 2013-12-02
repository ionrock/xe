import argparse
from path import path

from invoke import run
from xe import settings
from xe.models import Requirements


def get_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clean', action='store_true')
    return parser.parse_args(args)


def main(args):
    args = get_args(args)

    venv = path(settings['VENV'])

    if args.clean and venv.isdir():
        venv.rmtree()

    run('virtualenv %s' % venv)

    # TODO: Allow custom requirement class here
    reqs = Requirements()
    reqs.install()

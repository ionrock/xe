from subprocess import call
from path import path

from xe import settings


def env_do(tail):
    return run('%s/bin/%s' % (settings['VENV'], tail))


def run(cmd):
    activate = path(settings['VENV']) / 'bin' / 'activate_this.py'
    execfile(activate, dict(__file__=activate))
    try:
        call(cmd, shell=True)
    except KeyboardInterrupt:
        pass

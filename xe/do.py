from subprocess import call
from path import path

from xe import settings


def env_do(tail):
    return run('%s/bin/%s' % (settings['VENV'], tail))


def run(cmd):
    venv = path(settings['VENV'])
    if venv.exists():
        activate = venv / 'bin' / 'activate_this.py'
        execfile(activate, dict(__file__=activate))

    try:
        call(cmd)
    except KeyboardInterrupt:
        pass

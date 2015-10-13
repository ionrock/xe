from subprocess import call
from path import path, Path
import os

from xe import settings


def bin_dir():
    return 'Scripts' if os.name == 'nt' else 'bin'


def env_do(tail):
    tail[0] = Path('%s/%s/%s' % (settings['VENV'], bin_dir(), tail[0])).normpath()
    return run(tail)


def rdo(cmd):
    # Use rdo for specific commands or ALL commands
    if cmd[0] in settings['RDO_COMMANDS'] or settings['USE_RDO']:
        cmd = ['rdo'] + cmd
    return cmd


def withenv(cmd):
    if settings['WITHENV_DEFAULT']:
        cmd = ['we'] + settings['WITHENV_DEFAULT'].split() + cmd
    return cmd


def run(cmd):
    venv = path(settings['VENV'])
    if venv.exists():
        activate = venv / bin_dir() / 'activate_this.py'
        execfile(activate, dict(__file__=activate))

    cmd = withenv(cmd)
    cmd = rdo(cmd)

    print('Running: %s' % cmd)
    try:
        call(cmd, shell=(os.name == 'nt'))
    except KeyboardInterrupt:
        pass

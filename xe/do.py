from subprocess import call
from path import path

from xe import settings


def env_do(tail):
    tail[0] = '%s/bin/%s' % (settings['VENV'], tail[0])
    return run(tail)


def run(cmd):
    venv = path(settings['VENV'])
    if venv.exists():
        activate = venv / 'bin' / 'activate_this.py'
        execfile(activate, dict(__file__=activate))

    ssh = settings['SSH']

    if ssh:
        cmd = ['ssh'] + ssh.split() + cmd

    if settings['USE_RDO']:
        cmd = ['rdo'] + cmd

    print('Running: %s' % cmd)
    try:
        call(cmd)
    except KeyboardInterrupt:
        pass

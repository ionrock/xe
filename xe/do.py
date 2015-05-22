from subprocess import call
from path import path

from xe import settings


def env_do(tail):
    tail[0] = '%s/bin/%s' % (settings['VENV'], tail[0])
    return run(tail)


def rdo(cmd):
    # Use rdo for specific commands or ALL commands
    if cmd[0] in settings['RDO_COMMANDS'] or settings['USE_RDO']:
        cmd = ['rdo'] + cmd
    return cmd


def run(cmd):
    venv = path(settings['VENV'])
    if venv.exists():
        activate = venv / 'bin' / 'activate_this.py'
        execfile(activate, dict(__file__=activate))

    cmd = rdo(cmd)

    print('Running: %s' % ' '.join(cmd))
    try:
        call(cmd)
    except KeyboardInterrupt:
        pass

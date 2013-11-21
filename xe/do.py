from invoke import run as invoke_run
from path import path

from xe import settings


def env_do(tail, *args, **kw):
    return run('%s/bin/%s' % (settings.VENV, tail), *args, **kw)


def run(*args, **kw):
    activate = path(settings.VENV) / 'bin' / 'activate_this.py'
    execfile(activate, dict(__file__=activate))
    invoke_run(*args, **kw)

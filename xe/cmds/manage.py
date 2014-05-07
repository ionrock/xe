from path import path
from xe import settings
from xe.do import env_do


def main(args):
    manage = path(settings['DJANGO_MANAGE'])
    if not manage.exists():
        print('No manage.py exists in the root directory')
        return

    cmd = ['python', manage]
    cmd.extend(args)
    env_do(cmd)

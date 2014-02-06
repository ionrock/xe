from path import path
from xe import settings
from xe.do import env_do


def main(args):
    manage = path(settings['DJANGO_MANAGE'])
    if not manage.exists():
        print('No manage.py exists in the root directory')
        return

    env_do('python %s %s' % (manage,' '.join(args)))

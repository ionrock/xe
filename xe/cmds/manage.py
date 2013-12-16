from path import path
from xe.do import env_do


def main(args):
    if not path('manage.py').exists():
        print('No manage.py exists in the root directory')
        return

    env_do('python manage.py %s' % ' '.join(args))

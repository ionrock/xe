from xe.do import env_do
from xe import settings


class Requirements(object):
    """A pip install -r capable file"""

    names = [
        'dev_requirements.txt',
        'requirements.txt',
        'setup.py',
    ]

    def install(self):
        filename = self.filename()
        if not filename:
            print('No requirements found!')
            return

        if filename.endswith('setup.py'):
            env_do('pip install -e .')
        else:
            env_do('pip install -r %s' % filename)

    def filename(self):
        for name in self.names:
            result = settings['root'].files(name)
            if result:
                return result[0]
        return None

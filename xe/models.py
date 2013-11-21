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

        if filename == 'setup.py':
            env_do('python setup.py develop')
        else:
            env_do('pip install -r %s' % filename)

    def filename(self):
        for name in self.names:
            result = settings.root().files(name)
            return result[0]

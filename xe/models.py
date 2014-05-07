from xe.do import env_do
from xe import settings


class Requirements(object):
    """A pip install -r capable file"""

    names = [
        'dev_requirements.txt',
        'requirements.txt',
        'setup.py',
    ]

    def install(self, index=None):
        filename = self.filename()
        if not filename:
            print('No requirements found!')
            return

        cmd = ['pip', 'install']

        if index:
            print('Using index: %s' % index)
            cmd.extend(['-i', index])

        if filename.endswith('setup.py'):
            cmd.extend(['-e', '.'])
        else:
            cmd.extend(['-r', filename])

        env_do(cmd)

    def filename(self):
        for name in self.names:
            result = settings['root'].files(name)
            if result:
                return result[0]
        return None

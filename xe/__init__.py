import os
import yaml

from path import path


defaults = dict(
    VENV='venv',
    TEST_RUNNER='py.test',
    DJANGO_MANAGE='manage.py',
    USE_RDO=False,
    RDO_COMMANDS=[],
)


class WorkingDirectory(object):
    ROOT_FILES = [
        '.xerc',
        'setup.py',
        'requirements.txt',
        'dev_requirements.txt',
        'devrequirements.txt',
        'Makefile',
    ]

    ROOT_DIRS = [
        '.hg',
        '.git',
    ]

    def __init__(self):
        self.start = path(os.getcwd())
        self._here = None

    def find_root(self, start=None):

        start = start or self.start

        for f in self.ROOT_FILES:
            if start.files(f):
                return start

        for d in self.ROOT_DIRS:
            if start.dirs(d):
                return start

        if start.parent == '/':
            raise Exception('No project root found')

        return self.find_root(start.parent)

    def settings(self):
        settings = defaults
        settings['root'] = path(self.find_root())

        if settings['root'].files('.xerc'):
            locals = yaml.safe_load(open(settings['root'] / '.xerc'))
            settings.update(locals)

        return settings


settings = WorkingDirectory().settings()

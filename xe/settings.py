import os
from path import path

VENV = 'venv'


ROOT_FILES = [
    'setup.py',
    'requirements.txt',
    'dev_requirements.txt',
    'Makefile',
    '.hg',
    '.git',
]


class CWD(object):
    ROOT_FILES = [
        'setup.py',
        'requirements.txt',
        'dev_requirements.txt',
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

        if start.parent() == '/':
            raise Exception('No project root found')

        return self.find_root(start.parent())

    def __call__(self):
        if not self._here:
            self._here = self.find_root()
        return self._here


root = CWD()

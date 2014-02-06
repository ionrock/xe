from setuptools import setup, find_packages


setup_params = dict(
    name='xe',
    version='0.2',
    author='Eric Larson',
    author_email='eric@ionrock.org',
    url='http://github.com/ionrock/xe',
    packages=find_packages(),
    install_requires=[
        'virtualenv',
        'bumpversion',
        'path.py',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'xe = xe.run:main',
        ]
    },
    description='Reliably manage your python dev environment.',
    long_description=open('README.rst').read(),
)


if __name__ == '__main__':
    setup(**setup_params)

from setuptools import setup, find_packages
from os.path import join, dirname
from pycut import __version__

setup(
    name='pycut',
    version=__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pycut = pycut:pycut',
            ]
        },
    install_requires = [],
)

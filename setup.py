import codecs
import re 
import os 
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

REQUIREMENTS_FILE_NAME = 'requirements.txt'

with open(os.path.join(os.path.dirname(__file__), REQUIREMENTS_FILE_NAME)) as f:
    requirements = [line.strip() for line in f.read().splitlines()]


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

setup(
    name='cepsa-core-libs',
    long_description=README,
    packages=['core_libs'],
    version=find_version("core_libs", "__init__.py"),
    install_requires=requirements,
    author='Cepsa',
    description='',
    license='MIT'
)

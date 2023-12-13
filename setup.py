from glob import glob
from os.path import basename, splitext
from setuptools import find_packages, setup

setup(
    name='auto_ui',
    version='0.1',
    py_modules=[splitext(basename(path))[0] for path in glob('auto_ui/*.py')],   
)
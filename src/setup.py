from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

# get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='rethinking',
    version='0.0.2',
    description='Set of utilities for doing Bayesian data analysis in Python',
    long_description=long_description,
    packages=find_packages(exclude=['tests'])
)

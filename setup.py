#!/usr/bin/env python
from setuptools import setup

requirements = [line for line in open('requirements.txt')]

license = open('LICENSE').read()

setup(name='gl-test',
      author='Luke Campbell',
      author_email='luke.s.campbell+pypi@gmail.com',
      url='https://github.com/lukecampbell/python-gl-test',
      version='0.0.1',
      license=license,
      install_requires=requirements)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst



import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as readme_file:
    readme = readme_file.read()
#
#with open('HISTORY.rst') as history_file:
#    history = history_file.read().replace('.. :changelog:', '')
#
with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()


setup(
    name='mcradar',
    version='0.0',
    description='Radar forward operator for McSnow output (builded on top of PyTmatrix)',
    long_description=readme + '\n\n', #+ history,
    author='Jose Dias Neto',
    author_email='jdias@gmail.com',
    #url='http://',
    packages=['mcradar'],
    package_dir = {'mcradar':
                   'mcradar'},
    license='3-clause BSD',
    install_requires=requirements,
#    classifiers=[
#        'Development Status :: 4 - Beta',
#        'Programming Language :: Python :: 2',
#        'Programming Language :: Python :: 2.7',
#        'Programming Language :: Python :: 3',
#        'Programming Language :: Python :: 3.6',
#        'Programming Language :: Python :: 3.7',
#        'License :: OSI Approved :: BSD License',
#        ],
    keywords='Radar Operator McSnow PyTmatrix',
    include_package_data=True,
    zip_safe=False,
#    extras_require = {
#        'GSW': ["gsw>=3.0.6"],
#        'manualqc': ["matplotlib"],
#        'regional': ["Shapely>=1.6.4"]
#    }
)
#!/usr/bin/env python
import os
from setuptools import setup


on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
# read the docs could not compile numpy and c extensions
if on_rtd:
    setup_requires = []
    install_requires = []
else:
    setup_requires = [
        'nose',
        'coverage',
    ]
    install_requires = [
        'six',
        'bistiming',
        'numpy',
    ]

setup(
    name='serialtime',
    version="0.1.0",
    description=("A Python serialization tool containing many "
                 "serialization shortcuts with timing."),
    long_description=("A Python serialization tool containing many "
                      "serialization shortcuts with timing."),
    author='ianlini',
    url='https://github.com/ianlini/serialtime',
    setup_requires=setup_requires,
    install_requires=install_requires,
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    test_suite='nose.collector',
    packages=[
        'serialtime',
    ],
    package_dir={
        'serialtime': 'serialtime',
    },
)

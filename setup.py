#!/usr/bin/env python
import os
from setuptools import setup


on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
# read the docs could not compile numpy and c extensions
if on_rtd:
    setup_requires = []
    install_requires = []
    tests_require = []
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
    tests_require = [
        'scikit-learn',
        'scipy',
    ]

description = ("A Python serialization tool containing many serialization "
               "and deserialization shortcuts with timing.")

long_description = """\
Please visit  the `GitHub repository <https://github.com/ianlini/serialtime>`_
for more information.\n
"""
with open('README.rst') as fp:
    long_description += fp.read()

setup(
    name='serialtime',
    version="0.1.1",
    description=description,
    long_description=long_description,
    author='ianlini',
    url='https://github.com/ianlini/serialtime',
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
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

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import sys
import os
import re
import io

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    readme = f.read()

with io.open(os.path.join(here, 'HISTORY.rst'), encoding='utf-8') as f:
    history = f.read()

install_requires = ['rebulk>=0.7.1', 'babelfish>=0.5.5', 'python-dateutil<2.5.2']
# python-dateutil 2.5.2 introduced a change with month position in ambiguous day/month dates when year is first.
# https://github.com/dateutil/dateutil/commit/2d42e046d55b9fbbc0a2f41ce83fb8ec5de2d28b#commitcomment-17032106
if sys.version_info < (2, 7):
    install_requires.extend(['argparse', 'ordereddict'])
setup_requires = ['pytest-runner']

native_require = ['regex']

dev_require = ['zest.releaser[recommended]', 'pylint', 'tox', 'sphinx', 'sphinx-autobuild']

tests_require = ['pytest>=2.7.3', 'pytest-benchmark', 'pytest-capturelog', 'PyYAML']

entry_points = {
    'console_scripts': [
        'guessit = guessit.__main__:main'
    ],
}

with io.open('guessit/__version__.py', 'r') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]$', f.read(), re.MULTILINE).group(1)

args = dict(name='guessit',
            version=version,
            description='GuessIt - a library for guessing information from video filenames.',
            long_description=readme + '\n\n' + history,
            # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
            classifiers=['Development Status :: 5 - Production/Stable',
                         'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                         'Operating System :: OS Independent',
                         'Intended Audience :: Developers',
                         'Programming Language :: Python :: 2',
                         'Programming Language :: Python :: 2.6',
                         'Programming Language :: Python :: 2.7',
                         'Programming Language :: Python :: 3',
                         'Programming Language :: Python :: 3.3',
                         'Programming Language :: Python :: 3.4',
                         'Programming Language :: Python :: 3.5',
                         'Topic :: Multimedia',
                         'Topic :: Software Development :: Libraries :: Python Modules'
                         ],
            keywords='python library release parser name filename movies series episodes animes',
            author='Rémi Alvergnat',
            author_email='toilal.dev@gmail.com',
            url='http://guessit.readthedocs.org/',
            download_url='https://pypi.python.org/packages/source/g/guessit/guessit-%s.tar.gz' % version,
            license='LGPLv3',
            packages=find_packages(),
            include_package_data=True,
            install_requires=install_requires,
            setup_requires=setup_requires,
            tests_require=tests_require,
            entry_points=entry_points,
            test_suite='guessit.test',
            zip_safe=True,
            extras_require={
                'test': tests_require,
                'dev': dev_require,
                'native': native_require
            })

setup(**args)

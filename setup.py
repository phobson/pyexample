#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

PACKAGE_DATA = {
    'pyexample.tests.baseline_images.test_viz': ['*png'],
    'pyexample.tests.data': ['*'],
}

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pyexample',
    version='0.1.0',
    description="An Example Python Package",
    long_description=readme + '\n\n' + history,
    author="Paul M. Hobson",
    author_email='phobson@geosyntec.com',
    url='https://github.com/phobson/pyexample',
    packages=[
        'pyexample',
    ],
    package_dir={'pyexample':
                 'pyexample'},
    package_data=PACKAGE_DATA,
    entry_points={
        'console_scripts': [
            'pyexample=pyexample.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='pyexample',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

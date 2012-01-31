#!/usr/bin/env python
"""
sentry-graphite
==================

An extension for Sentry that increments a key in graphite based on the error.

:copyright: (c) 2012 DISQUS.
:license: Apache License 2.0, see LICENSE for more details.
"""

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

install_requires = [
    'sentry>=2.1.0',
]

setup(
    name='sentry-graphite',
    version='0.1.0',
    author='DISQUS',
    author_email='opensource@disqus.com',
    url='http://github.com/disqus/sentry-graphite',
    description='A Sentry extension that counts events in Graphite',
    long_description=__doc__,
    license='Apache License 2.0',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
    keywords='sentry graphite',
)

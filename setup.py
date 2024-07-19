"""
This file is used to install the package and its dependencies.
"""

from setuptools import setup


setup(
    name='REST_API_testing',
    version='0.0.1',
    packages=['REST_API_testing'],
    install_requires=[
        'requests',
        'pytest',
    ],
)


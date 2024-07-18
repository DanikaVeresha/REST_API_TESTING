from setuptools import setup


setup(
    name='REST_API_testing',
    version='0.0.1',
    packages=['REST_API_testing'],
    install_requires=[
        'requests',
        'pytest',
        'pytest-html',
        'pytest-xdist',
        'pytest-rerunfailures',
    ],
)

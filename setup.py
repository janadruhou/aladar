"""Scrum bot's setup"""

from setuptools import setup, find_packages

setup(
    name='aladar',
    description='IRC Scrum bot',
    version='0.0.1',
    author='celestian',
    license='GPLv3',
    url='https://github.com/celestian/aladar',

    packages=find_packages(),

    install_requires=[
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)

#!/usr/bin/env python

from setuptools import setup, find_packages
import blocks

setup(
    name='blocks',
    version=blocks.__version__,
    description='simple n-dimensional array blocks',
    long_description='',
    keywords='blocks n-dimensional arrays',
    author='Adam Luchies',
    url='https://github.com/aluchies/blocks',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
)
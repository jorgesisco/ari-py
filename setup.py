#!/usr/bin/env python

import os

from setuptools import setup

setup(
    name="ari",
    version="0.1",
    license="MIT",
    description="Library for accessing the Asterisk REST Interface",
    author="Jorge Sisco",
    author_email="jorgesisco17@gmail.com",
    url="https://github.com/jorgesisco/ari-py",
    packages=["ari"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    tests_require=["coverage", "httpretty", "nose", "tissue"],
    install_requires=["swaggerpy"],
)

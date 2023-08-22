#!/usr/bin/env python
"""Setup."""

import importlib
import sys

from setuptools import setup, find_packages

# read the contents of the README file
with open("README.md", encoding="utf-8") as f:
    README = f.read()

VERSION = "0.0.1"

print(find_packages)

setup(
    name="dataframe_pointer",
    author="Hugo Dictus",
    author_email="hugo.dictus@epfl.ch",
    version=VERSION,
    description="",
    long_description=README,
    long_description_content_type="text/markdown",
    license="GNU GPL",
    install_requires=[
        'pandas'
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Vision-Analyses",
    ],
)

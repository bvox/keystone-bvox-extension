#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
"""
:py:mod:`setup` --- Setuptools script
=====================================
Provides setuptools needed script in order manage pip install

.. module:: setup
    :synopsis: setuptools script

.. moduleauthor::Rafael Durán Castañeda <rafael@bvox.net>
"""
import os
import bvoxextension
from setuptools import setup, find_packages

GITHUB_URL = 'https://github.com/bvox/keystone-bvox-extension'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="bvoxextension",
    packages=find_packages(),
    install_requires=('keystone',),
    version=bvoxextension.__version__,
    description="BVOX's Keystone extension",
    author="Rafael Durán Castañeda",
    author_email="rafael@bvox.net",
    url=GITHUB_URL,
    download_url="%s/tarball/%s" % (GITHUB_URL, bvoxextension.__version__),
    keywords=["Openstack", "Keystone", "API", "Extension"],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: Public domain",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description = read("README.rst"))

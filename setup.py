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


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "keystone-bvoxextension",
    packages = find_packages(),
    install_requires = ('keystone',),
#    tests_require=['unittest2', 'MySQL-python'],
    version = bvoxextension.__version__,
    description = "BVOX's Keystone extension",
    author = "Rafael Durán Castañeda",
    author_email = "rafael@bvox.net",
    # url = TODO,
    # download_url = TODO,
    keywords = ["Openstack", "Keystone", "API", "Extension"],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        # "License :: TODO,
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
                   ],
    long_description = read("README.rst"))

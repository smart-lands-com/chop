#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 08 30 16:29:20 2018

@project: CHOP
@author : likw
@company: HuMan Inc.
"""


from setuptools import setup, find_packages

setup(
    name = "chop",
    version = "0.1.0",
    keywords = ("pip", "pathtool","timetool", "magetool", "mage"),
    description = "Chinese text segmentation",
    long_description = "Chinese text segmentation from HuMan Inc.",
    license = "MIT Licence",

    url = "https://github.com/smart-lands-com/chop",
    author = "smartlands",
    author_email = "info@smart-lands.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)

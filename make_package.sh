#!/bin/sh
# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Roland Csaszar
#
# Project:  tzolkin-calendar
# File:     make_package.sh
# Date:     21.Mar.2021
################################################################################

# generates a Python PIP package in the current working directory and uploads
# it to Pypi.
# Uses pipenv, you can install that by `python -m pip install pipenv` and
# installing the needed packages from the Buildnis root dir `Buildnis` - where
# the `Pipfile` is located.
# `pipenv install --dev` installs all needed dependencies to develop.


rm -rf -- ./build
rm -rf -- ./dist
rm -rf -- ./tzolkin_calendar.egg-info

pipenv run python -m build

# pipenv run twine upload --repository testpypi dist/* --config-file ~/.pypirc

pipenv run twine upload --repository pypi dist/* --config-file ~/.pypirc

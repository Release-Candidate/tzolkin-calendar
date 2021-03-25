#!/bin/sh
# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Roland Csaszar
#
# Project:  tzolkin-calendar
# File:     run_local_linters.sh
# Date:     16.Mar.2021
################################################################################

# Runs the local linters
isort tzolkin_calendar tests
black tzolkin_calendar tests
pyflakes tzolkin_calendar tests
pycodestyle tzolkin_calendar tests
pydocstyle tzolkin_calendar tests
flake8 tzolkin_calendar tests
bandit -r tzolkin_calendar tests

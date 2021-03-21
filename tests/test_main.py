# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Roland Csaszar
#
# Project:  tzolkin-calendar
# File:     test_main.py
# Date:     21.Mar.2021
###############################################################################
"""Tests the main module."""

from __future__ import annotations

import runpy
import sys
from typing import List
from unittest import mock

import pytest


################################################################################
def runTzolkinCalendar(cmd_line_args: List[str]) -> None:
    """Run the program with the given arguments.

    Returns the output of the command in the tuple `stdout, stderr`. The first element
    of the tuple holds the process' output on `stdout`, the second the output on
    `stderr`.

    Args:
        cmd_line_args (List[str]): The arguments to pass to `tzolkin_calendar`.
    """
    sys_argv_list = [""]
    sys_argv_list.extend(cmd_line_args)
    sys.argv = sys_argv_list

    runpy.run_module("tzolkin_calendar", run_name="__main__")


################################################################################
def test_pythonVersion() -> None:
    """Tests the check of the Python version."""
    with mock.patch.object(sys, "version_info") as mock_vers:
        mock_vers.major = 3
        mock_vers.minor = 6
        with pytest.raises(expected_exception=SystemExit) as excp:
            runpy.run_module("tzolkin_calendar", run_name="__main__")
        assert excp.value.args[0] == 1  # nosec


################################################################################
def test_versionString() -> None:
    """Test the output of a version string."""
    with pytest.raises(expected_exception=SystemExit) as excp:
        runTzolkinCalendar(["--version"])
    assert excp.value.args[0] == 0  # nosec


################################################################################
def test_illegalArg() -> None:
    """Test an illegal argument."""
    with pytest.raises(expected_exception=SystemExit) as excp:
        runTzolkinCalendar(["--HASD"])
    assert excp.value.args[0] == 2  # nosec

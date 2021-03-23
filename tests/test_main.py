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

from tzolkin_calendar import TzolkinDate

# Using https://maya.nmai.si.edu/calendar/maya-calendar-converter
local_reference_dates = {
    "01.01.1800": TzolkinDate(number=10, name=14),
    "12.12.1926": TzolkinDate(number=4, name=19),
    "26.01.1958": TzolkinDate(number=10, name=7),
    "15.03.1967": TzolkinDate(number=4, name=2),
    "01.01.1970": TzolkinDate(number=13, name=5),
    "08.05.1975": TzolkinDate(number=3, name=18),
    "17.02.1978": TzolkinDate(number=5, name=14),
    "25.10.1986": TzolkinDate(number=5, name=6),
    "13.05.1992": TzolkinDate(number=4, name=13),
    "08.11.1997": TzolkinDate(number=7, name=18),
    "01.01.2000": TzolkinDate(number=11, name=2),
    "06.07.2005": TzolkinDate(number=9, name=15),
    "01.10.2017": TzolkinDate(number=7, name=5),
    "20.03.2021": TzolkinDate(number=12, name=11),
}


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
def test_versionString(capsys: pytest.CaptureFixture) -> None:
    """Test the output of a version string."""
    with pytest.raises(expected_exception=SystemExit) as excp:
        runTzolkinCalendar(["--version"])

    assert excp.value.args[0] == 0  # nosec
    captured = capsys.readouterr()
    assert captured.err == ""  # nosec
    assert captured.out.find("tzolkin-calendar") == 0  # nosec


################################################################################
def test_illegalArg() -> None:
    """Test an illegal argument."""
    with pytest.raises(expected_exception=SystemExit) as excp:
        runTzolkinCalendar(["--HASD"])
    assert excp.value.args[0] == 2  # nosec


################################################################################
def test_showHelp(capsys: pytest.CaptureFixture) -> None:
    """Test the output of the help text."""
    with pytest.raises(expected_exception=SystemExit) as excp:
        runTzolkinCalendar(["--help"])

    assert excp.value.args[0] == 0  # nosec
    captured = capsys.readouterr()
    assert captured.err == ""  # nosec
    assert (  # nosec
        captured.out.find("usage: python -m tzolkin_calendar [-h] [--version]") == 0
    )


################################################################################
def test_showYear(capsys: pytest.CaptureFixture) -> None:
    """Test the output of the help text."""
    with pytest.raises(expected_exception=SystemExit) as excp:
        runTzolkinCalendar(["--year"])

    assert excp.value.args[0] == 0  # nosec
    captured = capsys.readouterr()
    assert captured.err == ""  # nosec
    assert captured.out.find(" 1 Imix 2 Ikʼ 3 Akʼbʼal 4 Kʼan 5 Chikchan") == 0  # nosec


################################################################################
@pytest.mark.parametrize(
    "gregorian,tzolkin",
    [
        pytest.param(
            "01.01.1800", local_reference_dates["01.01.1800"], id="01.01.1800"
        ),
        pytest.param(
            "12.12.1926", local_reference_dates["12.12.1926"], id="12.12.1926"
        ),
        pytest.param(
            "26.01.1958", local_reference_dates["26.01.1958"], id="26.01.1958"
        ),
        pytest.param(
            "15.03.1967", local_reference_dates["15.03.1967"], id="15.03.1967"
        ),
        pytest.param(
            "01.01.1970", local_reference_dates["01.01.1970"], id="01.01.1970"
        ),
        pytest.param(
            "08.05.1975", local_reference_dates["08.05.1975"], id="08.05.1975"
        ),
        pytest.param(
            "17.02.1978", local_reference_dates["17.02.1978"], id="17.02.1978"
        ),
        pytest.param(
            "25.10.1986", local_reference_dates["25.10.1986"], id="25.10.1986"
        ),
        pytest.param(
            "13.05.1992", local_reference_dates["13.05.1992"], id="13.05.1992"
        ),
        pytest.param(
            "08.11.1997", local_reference_dates["08.11.1997"], id="08.11.1997"
        ),
        pytest.param(
            "01.01.2000", local_reference_dates["01.01.2000"], id="01.01.2000"
        ),
        pytest.param(
            "06.07.2005", local_reference_dates["06.07.2005"], id="06.07.2005"
        ),
        pytest.param(
            "01.10.2017", local_reference_dates["01.10.2017"], id="01.10.2017"
        ),
        pytest.param(
            "20.03.2021", local_reference_dates["20.03.2021"], id="20.03.2021"
        ),
    ],
)
def test_gregorian2tzolkin(
    capsys: pytest.CaptureFixture, gregorian: str, tzolkin: TzolkinDate
) -> None:
    """Test the conversion to a Tzolkin date."""
    with pytest.raises(expected_exception=SystemExit) as excp:
        runTzolkinCalendar([gregorian])

    assert excp.value.args[0] == 0  # nosec
    captured = capsys.readouterr()
    assert captured.err == ""  # nosec
    assert (  # nosec
        captured.out
        == 'Gregorian "{gregorian}" is "{tzolkin}" as Tzolk’in\n'.format(
            gregorian=gregorian, tzolkin=tzolkin
        )
    )


################################################################################
def test_invalidDate(capsys: pytest.CaptureFixture) -> None:
    """Test  with an invalid gregorian date."""
    with pytest.raises(expected_exception=SystemExit) as excp:
        runTzolkinCalendar(["36.10.2000"])

    assert excp.value.args[0] == 2  # nosec
    captured = capsys.readouterr()
    assert (  # nosec
        captured.err.find("error \"time data '36.10.2000' does not match format") == 0
    )
    assert (  # nosec
        captured.out.find("usage: python -m tzolkin_calendar [-h] [--version]") == 0
    )


################################################################################
@pytest.mark.parametrize(
    "gregorian,tzolkin",
    [
        pytest.param(
            "01.01.1800", local_reference_dates["01.01.1800"], id="01.01.1800"
        ),
        pytest.param(
            "01 01 1800", local_reference_dates["01.01.1800"], id="01 01 1800"
        ),
        pytest.param(
            "01-01-1800", local_reference_dates["01.01.1800"], id="01-01-1800"
        ),
        pytest.param(
            "1800.01.01", local_reference_dates["01.01.1800"], id="1800.01.01"
        ),
        pytest.param(
            "1800-01-01", local_reference_dates["01.01.1800"], id="1800-01-01"
        ),
        pytest.param(
            "1800/01/01", local_reference_dates["01.01.1800"], id="1800/01/01"
        ),
        pytest.param(
            "1800 01 01", local_reference_dates["01.01.1800"], id="1800 01 01"
        ),
        pytest.param(
            "01/01/1800", local_reference_dates["01.01.1800"], id="01/01/1800"
        ),
    ],
)
def test_gregorian2tzolkinVariants(
    capsys: pytest.CaptureFixture, gregorian: str, tzolkin: TzolkinDate
) -> None:
    """Test the conversion to a Tzolkin date."""
    with pytest.raises(expected_exception=SystemExit) as excp:
        runTzolkinCalendar([gregorian])

    assert excp.value.args[0] == 0  # nosec
    captured = capsys.readouterr()
    assert captured.err == ""  # nosec
    assert (  # nosec
        captured.out
        == 'Gregorian "{gregorian}" is "{tzolkin}" as Tzolk’in\n'.format(
            gregorian=gregorian, tzolkin=tzolkin
        )
    )


################################################################################
@pytest.mark.parametrize(
    "tzolkin_str,tzolkin_name",
    [
        pytest.param("12 Bʼen", "12 Bʼen", id="12 Bʼen"),
        pytest.param("12/Bʼen", "12 Bʼen", id="12/Bʼen"),
        pytest.param("12.Bʼen", "12 Bʼen", id="12.Bʼen"),
        pytest.param("12-Bʼen", "12 Bʼen", id="12-Bʼen"),
        pytest.param("12 Ben", "12 Bʼen", id="12 Ben"),
        pytest.param("12/Ben", "12 Bʼen", id="12/Ben"),
        pytest.param("12.Ben", "12 Bʼen", id="12.Ben"),
        pytest.param("12-Ben", "12 Bʼen", id="12-Ben"),
        pytest.param("12 B`en", "12 Bʼen", id="12 B`en"),
        pytest.param("12/B`en", "12 Bʼen", id="12/B`en"),
        pytest.param("12.B`en", "12 Bʼen", id="12.B`en"),
        pytest.param("12-B`en", "12 Bʼen", id="12-B`en"),
        pytest.param("12 B'en", "12 Bʼen", id="12 B'en"),
        pytest.param("12/B'en", "12 Bʼen", id="12/B'en"),
        pytest.param("12.B'en", "12 Bʼen", id="12.B'en"),
        pytest.param("12-B'en", "12 Bʼen", id="12-B'en"),
        pytest.param("12 bEn", "12 Bʼen", id="12 bEn"),
        pytest.param("12/bEn", "12 Bʼen", id="12/bEn"),
        pytest.param("12.bEn", "12 Bʼen", id="12.bEn"),
        pytest.param("12-bEn", "12 Bʼen", id="12-bEn"),
        pytest.param("12 13", "12 Bʼen", id="12 13"),
        pytest.param("12/13", "12 Bʼen", id="12/13"),
        pytest.param("12.13", "12 Bʼen", id="12.13"),
        pytest.param("12-13", "12 Bʼen", id="12-13"),
    ],
)
def test_tzolkin2gregorian(
    capsys: pytest.CaptureFixture, tzolkin_str: str, tzolkin_name: str
) -> None:
    """Test  with an invalid gregorian date."""
    with pytest.raises(expected_exception=SystemExit) as excp:
        runTzolkinCalendar([tzolkin_str])

    assert excp.value.args[0] == 0  # nosec
    captured = capsys.readouterr()
    assert captured.err == ""  # nosec
    assert (  # nosec
        captured.out.find(
            'Tzolk’in date "{tzolkin_name}" next date is "'.format(
                tzolkin_name=tzolkin_name
            )
        )
        == 0
    )


################################################################################
@pytest.mark.parametrize(
    "tzolkin_str,tzolkin_name",
    [
        pytest.param("12 Bʼen", "12 Bʼen", id="12 Bʼen"),
        pytest.param("12/Bʼen", "12 Bʼen", id="12/Bʼen"),
        pytest.param("12.Bʼen", "12 Bʼen", id="12.Bʼen"),
        pytest.param("12-Bʼen", "12 Bʼen", id="12-Bʼen"),
        pytest.param("12 Ben", "12 Bʼen", id="12 Ben"),
        pytest.param("12/Ben", "12 Bʼen", id="12/Ben"),
        pytest.param("12.Ben", "12 Bʼen", id="12.Ben"),
        pytest.param("12-Ben", "12 Bʼen", id="12-Ben"),
        pytest.param("12 B`en", "12 Bʼen", id="12 B`en"),
        pytest.param("12/B`en", "12 Bʼen", id="12/B`en"),
        pytest.param("12.B`en", "12 Bʼen", id="12.B`en"),
        pytest.param("12-B`en", "12 Bʼen", id="12-B`en"),
        pytest.param("12 B'en", "12 Bʼen", id="12 B'en"),
        pytest.param("12/B'en", "12 Bʼen", id="12/B'en"),
        pytest.param("12.B'en", "12 Bʼen", id="12.B'en"),
        pytest.param("12-B'en", "12 Bʼen", id="12-B'en"),
        pytest.param("12 bEn", "12 Bʼen", id="12 bEn"),
        pytest.param("12/bEn", "12 Bʼen", id="12/bEn"),
        pytest.param("12.bEn", "12 Bʼen", id="12.bEn"),
        pytest.param("12-bEn", "12 Bʼen", id="12-bEn"),
        pytest.param("12 13", "12 Bʼen", id="12 13"),
        pytest.param("12/13", "12 Bʼen", id="12/13"),
        pytest.param("12.13", "12 Bʼen", id="12.13"),
        pytest.param("12-13", "12 Bʼen", id="12-13"),
    ],
)
def test_tzolkin2gregorianList(
    capsys: pytest.CaptureFixture, tzolkin_str: str, tzolkin_name: str
) -> None:
    """Test searching for tzolkin dates."""
    with pytest.raises(expected_exception=SystemExit) as excp:
        runTzolkinCalendar(["--list", "4", tzolkin_str])

    assert excp.value.args[0] == 0  # nosec
    captured = capsys.readouterr()
    assert captured.err == ""  # nosec
    assert (  # nosec
        captured.out.find(
            'Tzolk’in date "{tzolkin_name}"\n next dates are '.format(
                tzolkin_name=tzolkin_name
            )
        )
        == 0
    )


################################################################################
@pytest.mark.parametrize(
    "tzolkin_str,tzolkin_name",
    [
        pytest.param("12 Bʼen", "12 Bʼen", id="12 Bʼen"),
        pytest.param("12/Bʼen", "12 Bʼen", id="12/Bʼen"),
        pytest.param("12.Bʼen", "12 Bʼen", id="12.Bʼen"),
        pytest.param("12-Bʼen", "12 Bʼen", id="12-Bʼen"),
        pytest.param("12 Ben", "12 Bʼen", id="12 Ben"),
        pytest.param("12/Ben", "12 Bʼen", id="12/Ben"),
        pytest.param("12.Ben", "12 Bʼen", id="12.Ben"),
        pytest.param("12-Ben", "12 Bʼen", id="12-Ben"),
        pytest.param("12 B`en", "12 Bʼen", id="12 B`en"),
        pytest.param("12/B`en", "12 Bʼen", id="12/B`en"),
        pytest.param("12.B`en", "12 Bʼen", id="12.B`en"),
        pytest.param("12-B`en", "12 Bʼen", id="12-B`en"),
        pytest.param("12 B'en", "12 Bʼen", id="12 B'en"),
        pytest.param("12/B'en", "12 Bʼen", id="12/B'en"),
        pytest.param("12.B'en", "12 Bʼen", id="12.B'en"),
        pytest.param("12-B'en", "12 Bʼen", id="12-B'en"),
        pytest.param("12 bEn", "12 Bʼen", id="12 bEn"),
        pytest.param("12/bEn", "12 Bʼen", id="12/bEn"),
        pytest.param("12.bEn", "12 Bʼen", id="12.bEn"),
        pytest.param("12-bEn", "12 Bʼen", id="12-bEn"),
        pytest.param("12 13", "12 Bʼen", id="12 13"),
        pytest.param("12/13", "12 Bʼen", id="12/13"),
        pytest.param("12.13", "12 Bʼen", id="12.13"),
        pytest.param("12-13", "12 Bʼen", id="12-13"),
    ],
)
def test_tzolkin2gregorianListEmpty(
    capsys: pytest.CaptureFixture, tzolkin_str: str, tzolkin_name: str
) -> None:
    """Test finding a list of length `-1`."""
    with pytest.raises(expected_exception=SystemExit) as excp:
        runTzolkinCalendar(["--list", "-1", tzolkin_str])

    assert excp.value.args[0] == 0  # nosec
    captured = capsys.readouterr()
    assert captured.err == ""  # nosec
    assert (  # nosec
        captured.out.find(
            'Tzolk’in date "{tzolkin_name}"\n next dates are []\n last dates have been []'.format(
                tzolkin_name=tzolkin_name
            )
        )
        == 0
    )


################################################################################
@pytest.mark.parametrize(
    "tzolkin_str,tzolkin_name,next_str,last_str",
    [
        pytest.param("12 Bʼen", "12 Bʼen", "11.05.2000", "25.08.1999", id="12 Bʼen"),
        pytest.param("12/Bʼen", "12 Bʼen", "11.05.2000", "25.08.1999", id="12/Bʼen"),
        pytest.param("12.Bʼen", "12 Bʼen", "11.05.2000", "25.08.1999", id="12.Bʼen"),
        pytest.param("12-Bʼen", "12 Bʼen", "11.05.2000", "25.08.1999", id="12-Bʼen"),
        pytest.param("12 Ben", "12 Bʼen", "11.05.2000", "25.08.1999", id="12 Ben"),
        pytest.param("12/Ben", "12 Bʼen", "11.05.2000", "25.08.1999", id="12/Ben"),
        pytest.param("12.Ben", "12 Bʼen", "11.05.2000", "25.08.1999", id="12.Ben"),
        pytest.param("12-Ben", "12 Bʼen", "11.05.2000", "25.08.1999", id="12-Ben"),
        pytest.param("12 B`en", "12 Bʼen", "11.05.2000", "25.08.1999", id="12 B`en"),
        pytest.param("12/B`en", "12 Bʼen", "11.05.2000", "25.08.1999", id="12/B`en"),
        pytest.param("12.B`en", "12 Bʼen", "11.05.2000", "25.08.1999", id="12.B`en"),
        pytest.param("12-B`en", "12 Bʼen", "11.05.2000", "25.08.1999", id="12-B`en"),
        pytest.param("12 B'en", "12 Bʼen", "11.05.2000", "25.08.1999", id="12 B'en"),
        pytest.param("12/B'en", "12 Bʼen", "11.05.2000", "25.08.1999", id="12/B'en"),
        pytest.param("12.B'en", "12 Bʼen", "11.05.2000", "25.08.1999", id="12.B'en"),
        pytest.param("12-B'en", "12 Bʼen", "11.05.2000", "25.08.1999", id="12-B'en"),
        pytest.param("12 bEn", "12 Bʼen", "11.05.2000", "25.08.1999", id="12 bEn"),
        pytest.param("12/bEn", "12 Bʼen", "11.05.2000", "25.08.1999", id="12/bEn"),
        pytest.param("12.bEn", "12 Bʼen", "11.05.2000", "25.08.1999", id="12.bEn"),
        pytest.param("12-bEn", "12 Bʼen", "11.05.2000", "25.08.1999", id="12-bEn"),
        pytest.param("12 13", "12 Bʼen", "11.05.2000", "25.08.1999", id="12 13"),
        pytest.param("12/13", "12 Bʼen", "11.05.2000", "25.08.1999", id="12/13"),
        pytest.param("12.13", "12 Bʼen", "11.05.2000", "25.08.1999", id="12.13"),
        pytest.param("12-13", "12 Bʼen", "11.05.2000", "25.08.1999", id="12-13"),
    ],
)
def test_tzolkin2gregorianStart(
    capsys: pytest.CaptureFixture,
    tzolkin_str: str,
    tzolkin_name: str,
    next_str: str,
    last_str: str,
) -> None:
    """Test searching for tzolkin dates."""
    with pytest.raises(expected_exception=SystemExit) as excp:
        runTzolkinCalendar([tzolkin_str, "--start", "10.04.2000"])

    assert excp.value.args[0] == 0  # nosec
    captured = capsys.readouterr()
    assert captured.err == ""  # nosec
    assert (  # nosec
        captured.out.find(
            'Tzolk’in date "{tzolkin_name}" next date is "{next}", last date has been "{last}"'.format(
                tzolkin_name=tzolkin_name, next=next_str, last=last_str
            )
        )
        == 0
    )

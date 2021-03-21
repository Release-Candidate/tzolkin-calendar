# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Roland Csaszar
#
# Project:  tzolkin-calendar
# File:     test_tzolkin.py
# Date:     21.Mar.2021
###############################################################################
"""Test tzolkin module."""

from __future__ import annotations

import datetime

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from tzolkin_calendar import USED_DATEFMT, TzolkinDate, TzolkinException, day_names
from tzolkin_calendar.calculate import (
    getTzolkinDay,
    getTzolkinDiff,
    lastTzolkin,
    makeLookUpTable,
    nextTzolkin,
    tzolkin2gregorian,
)
from tzolkin_calendar.tzolkin import Tzolkin

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
def test_TzolkinException1() -> None:
    """Test the constructor of `Tzolkin`, using a invalid day number."""
    with pytest.raises(TzolkinException) as excp:
        Tzolkin(number=17, name_number=7)
    assert excp  # nosec


################################################################################
def test_TzolkinException2() -> None:
    """Test the constructor of `Tzolkin`, using a invalid day name number."""
    with pytest.raises(TzolkinException) as excp:
        Tzolkin(number=6, name_number=27)
    assert excp  # nosec


################################################################################
def test_TzolkinException3() -> None:
    """Test the constructor of `Tzolkin`, using a invalid day name."""
    with pytest.raises(TzolkinException) as excp:
        Tzolkin(number=6, name_str="DOES NOT EXIST")
    assert excp  # nosec


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
def test_fromDate(gregorian: str, tzolkin: TzolkinDate) -> None:
    """Test `Tzolkin.fromDate`."""
    gregorian_date = datetime.datetime.strptime(gregorian, USED_DATEFMT).date()
    to_test = Tzolkin.fromDate(gregorian_date)
    assert to_test.getDayNumber() == tzolkin.number  # nosec
    assert to_test.getDayNameNumber() == tzolkin.name  # nosec


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
def test_fromDateStr(gregorian: str, tzolkin: TzolkinDate) -> None:
    """Test `Tzolkin.fromDateString`."""
    to_test = Tzolkin.fromDateString(date_str=gregorian, fmt=USED_DATEFMT)
    assert to_test.getDayNumber() == tzolkin.number  # nosec
    assert to_test.getDayNameNumber() == tzolkin.name  # nosec


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
def test_fromIsoFormat(gregorian: str, tzolkin: TzolkinDate) -> None:
    """Test `Tzolkin.fromIsoFormat`."""
    gregorian_date = datetime.datetime.strptime(gregorian, USED_DATEFMT).date()
    to_test = Tzolkin.fromIsoFormat(date_str=gregorian_date.isoformat())
    assert to_test.getDayNumber() == tzolkin.number  # nosec
    assert to_test.getDayNameNumber() == tzolkin.name  # nosec


################################################################################
def test_fromToday() -> None:
    """Test `Tzolkin.fromToday`."""
    assert (  # nosec
        Tzolkin.fromToday().getDayName()
        == Tzolkin.fromDate(date=datetime.date.today()).getDayName()
    )
    assert (  # nosec
        Tzolkin.fromToday().getDayNumber()
        == Tzolkin.fromDate(date=datetime.date.today()).getDayNumber()
    )


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
def test_getTzolkinDate(gregorian: str, tzolkin: TzolkinDate) -> None:
    """Test `Tzolkin.getTzolkinDate`."""
    gregorian_date = datetime.datetime.strptime(gregorian, USED_DATEFMT).date()
    to_test = Tzolkin.fromDate(gregorian_date)
    assert to_test.getTzolkinDate().number == tzolkin.number  # nosec
    assert to_test.getTzolkinDate().name == tzolkin.name  # nosec


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
def test_getTzolkinYearDay(gregorian: str, tzolkin: TzolkinDate) -> None:
    """Test `Tzolkin.getTzolkinYearDay`."""
    gregorian_date = datetime.datetime.strptime(gregorian, USED_DATEFMT).date()
    to_test = Tzolkin.fromDate(gregorian_date)
    assert to_test.getTzolkinYearDay() == getTzolkinDay(tzolkin)  # nosec


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
def test_getNextDate(gregorian: str, tzolkin: TzolkinDate) -> None:
    """Test `Tzolkin.getNextDate`."""
    gregorian_date = datetime.datetime.strptime(
        gregorian, USED_DATEFMT
    ).date() - datetime.timedelta(days=1)
    to_test = Tzolkin.fromDateString(date_str=gregorian, fmt=USED_DATEFMT)
    assert to_test.getNextDate(start_date=gregorian_date) == nextTzolkin(  # nosec
        tzolkin=tzolkin, starting=gregorian_date
    )


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
def test_getNextDateToday(gregorian: str, tzolkin: TzolkinDate) -> None:
    """Test `Tzolkin.getNextDate`."""
    to_test = Tzolkin.fromDateString(date_str=gregorian, fmt=USED_DATEFMT)
    assert to_test.getNextDate() == nextTzolkin(  # nosec
        tzolkin=tzolkin, starting=datetime.date.today()
    )


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
def test_getNextDateList(gregorian: str, tzolkin: TzolkinDate) -> None:
    """Test `Tzolkin.getNextDateList`."""
    gregorian_date = datetime.datetime.strptime(
        gregorian, USED_DATEFMT
    ).date() - datetime.timedelta(days=1)
    to_test = Tzolkin.fromDateString(date_str=gregorian, fmt=USED_DATEFMT)
    tz_list = to_test.getNextDateList(start_date=gregorian_date)
    good_list = tzolkin2gregorian(
        tzolkin=tzolkin, start=gregorian_date, num_results=50, forward=True
    )
    assert len(tz_list) == 50  # nosec
    for idx in range(0, len(good_list)):
        assert tz_list[idx] == good_list[idx]  # nosec


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
def test_getLastDate(gregorian: str, tzolkin: TzolkinDate) -> None:
    """Test `Tzolkin.getLastDate`."""
    gregorian_date = datetime.datetime.strptime(
        gregorian, USED_DATEFMT
    ).date() + datetime.timedelta(days=1)
    to_test = Tzolkin.fromDateString(date_str=gregorian, fmt=USED_DATEFMT)
    assert to_test.getLastDate(start_date=gregorian_date) == lastTzolkin(  # nosec
        tzolkin=tzolkin, starting=gregorian_date
    )


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
def test_getLastDateToday(gregorian: str, tzolkin: TzolkinDate) -> None:
    """Test `Tzolkin.getLastDate`."""
    to_test = Tzolkin.fromDateString(date_str=gregorian, fmt=USED_DATEFMT)
    assert to_test.getLastDate() == lastTzolkin(  # nosec
        tzolkin=tzolkin, starting=datetime.date.today()
    )


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
def test_getLastDateList(gregorian: str, tzolkin: TzolkinDate) -> None:
    """Test `Tzolkin.getLastDateList`."""
    gregorian_date = datetime.datetime.strptime(
        gregorian, USED_DATEFMT
    ).date() - datetime.timedelta(days=1)
    to_test = Tzolkin.fromDateString(date_str=gregorian, fmt=USED_DATEFMT)
    tz_list = to_test.getLastDateList(start_date=gregorian_date)
    good_list = tzolkin2gregorian(
        tzolkin=tzolkin, start=gregorian_date, num_results=50, forward=False
    )
    assert len(tz_list) == 50  # nosec
    for idx in range(0, len(good_list)):
        assert tz_list[idx] == good_list[idx]  # nosec


################################################################################
@settings(max_examples=50, deadline=None)
@given(days=st.integers(min_value=1, max_value=260))
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
def test_addDays(gregorian: str, tzolkin: TzolkinDate, days: int) -> None:
    """Test `Tzolkin.addTimedelta`."""
    gregorian_date = datetime.datetime.strptime(gregorian, USED_DATEFMT).date()
    tzolkin_start = Tzolkin.fromDate(date=gregorian_date).getTzolkinDate()
    assert tzolkin_start.number == tzolkin.number  # nosec
    assert tzolkin_start.name == tzolkin.name  # nosec
    tzolkin_add = Tzolkin.fromDate(date=gregorian_date).addDays(days).getTzolkinDate()
    assert getTzolkinDiff(tzolkin_start, tzolkin_add) == days  # nosec


################################################################################
@settings(max_examples=50, deadline=None)
@given(days=st.integers(min_value=1, max_value=260))
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
def test_addTimedelta(gregorian: str, tzolkin: TzolkinDate, days: int) -> None:
    """Test `Tzolkin.addTimedelta`."""
    gregorian_date = datetime.datetime.strptime(gregorian, USED_DATEFMT).date()
    tzolkin_start = Tzolkin.fromDate(date=gregorian_date).getTzolkinDate()
    assert tzolkin_start.number == tzolkin.number  # nosec
    assert tzolkin_start.name == tzolkin.name  # nosec
    tzolkin_add = (
        Tzolkin.fromDate(date=gregorian_date)
        .addTimedelta(datetime.timedelta(days=days))
        .getTzolkinDate()
    )
    assert getTzolkinDiff(tzolkin_start, tzolkin_add) == days  # nosec


################################################################################
@settings(max_examples=50, deadline=None)
@given(days=st.integers(min_value=1, max_value=260))
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
def test_getDayDiff(gregorian: str, tzolkin: TzolkinDate, days: int) -> None:
    """Test `Tzolkin.getDayDiff`."""
    gregorian_date = datetime.datetime.strptime(gregorian, USED_DATEFMT).date()
    tzolkin_start = Tzolkin.fromDate(date=gregorian_date)
    assert tzolkin_start.getTzolkinDate().number == tzolkin.number  # nosec
    assert tzolkin_start.getTzolkinDate().name == tzolkin.name  # nosec
    tzolkin_add = Tzolkin.fromDate(date=gregorian_date).addTimedelta(
        datetime.timedelta(days=days)
    )
    assert tzolkin_start.getDayDiff(other=tzolkin_add) == days  # nosec


################################################################################
@settings(max_examples=50, deadline=None)
@given(days=st.integers(min_value=1, max_value=260))
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
def test_getDayTimedelta(gregorian: str, tzolkin: TzolkinDate, days: int) -> None:
    """Test `Tzolkin.getDayTimedelta`."""
    gregorian_date = datetime.datetime.strptime(gregorian, USED_DATEFMT).date()
    tzolkin_start = Tzolkin.fromDate(date=gregorian_date)
    assert tzolkin_start.getTzolkinDate().number == tzolkin.number  # nosec
    assert tzolkin_start.getTzolkinDate().name == tzolkin.name  # nosec
    tzolkin_add = Tzolkin.fromDate(date=gregorian_date).addTimedelta(
        datetime.timedelta(days=days)
    )
    assert tzolkin_start.getDayTimedelta(other=tzolkin_add).days == days  # nosec


################################################################################
def test_getNameNumberFromName() -> None:
    """Test `Tzolkin.getNameNumberFromName`."""
    for number in day_names:
        assert (  # nosec
            Tzolkin.getNameNumberFromName(name_str=day_names[number]) == number
        )


################################################################################
def test_getTzolkinCalendar() -> None:
    """Test `Tzolkin.getTzolkinCalendar`."""
    calendar = Tzolkin.getTzolkinCalendar()
    tzolkin_dict = makeLookUpTable()
    assert len(calendar) == 260  # nosec
    for key in tzolkin_dict:
        assert calendar[key - 1] == "{number} {name}".format(  # nosec
            number=tzolkin_dict[key].number, name=tzolkin_dict[key].name
        )

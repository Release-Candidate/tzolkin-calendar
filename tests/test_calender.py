# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Roland Csaszar
#
# Project:  tzolkin-calendar
# File:     test_calender.py
# Date:     19.Mar.2021
###############################################################################
"""Test calculate module."""

from __future__ import annotations

import datetime
from typing import List, Optional

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from tzolkin_calendar import USED_DATEFMT, TzolkinDate, day_names, day_numbers
from tzolkin_calendar.calculate import (
    gregorian2tzolkin,
    lastTzolkin,
    nextTzolkin,
    tzolkin2gregorian,
)

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
def test_gregorian2tzolkin(gregorian: str, tzolkin: TzolkinDate) -> None:
    """Test the function gregorian2tzolkin."""
    gregorian_date = datetime.datetime.strptime(gregorian, USED_DATEFMT).date()
    assert gregorian2tzolkin(date=gregorian_date) == tzolkin  # nosec


################################################################################
@pytest.mark.slow
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
def test_tzolkin2gregorian(gregorian: str, tzolkin: TzolkinDate) -> None:
    """Test the function `tzolkin2gregorian`."""
    num_elems = len(day_names) * len(day_numbers)
    last_date_list_b: List[datetime.date] = []
    last_date_list_f: List[datetime.date] = []
    for day_diff in range(0, num_elems):

        given_date = datetime.datetime.strptime(
            gregorian, USED_DATEFMT
        ).date() + datetime.timedelta(days=day_diff)

        date_list_b = tzolkin2gregorian(
            tzolkin=tzolkin, start=given_date, num_results=10, forward=False
        )
        date_list_f = tzolkin2gregorian(
            tzolkin=tzolkin, start=given_date, num_results=10, forward=True
        )

        if last_date_list_b:
            for elem in last_date_list_b:
                assert elem in date_list_b  # nosec

        if last_date_list_f:
            for elem in last_date_list_f:
                assert elem in date_list_f  # nosec

        last_date_f: Optional[datetime.date] = None
        for date in date_list_f:
            if last_date_f is not None:
                day_diffs = date - last_date_f
                assert day_diffs.days == num_elems  # nosec
            last_date_f = date

        last_date_b: Optional[datetime.date] = None
        for date in date_list_b:
            if last_date_b is not None:
                day_diffs = last_date_b - date
                assert day_diffs.days == num_elems  # nosec
            last_date_b = date

        last_date_list_b = date_list_b
        last_date_list_f = date_list_f


################################################################################
@settings(max_examples=500, deadline=None)
@given(day_diff=st.integers(min_value=1, max_value=260))
@pytest.mark.parametrize(
    "tzolkin, gregorian",
    [
        pytest.param(
            local_reference_dates["01.01.1800"], "01.01.1800", id="01.01.1800"
        ),
        pytest.param(
            local_reference_dates["12.12.1926"], "12.12.1926", id="12.12.1926"
        ),
        pytest.param(
            local_reference_dates["26.01.1958"], "26.01.1958", id="26.01.1958"
        ),
        pytest.param(
            local_reference_dates["15.03.1967"], "15.03.1967", id="15.03.1967"
        ),
        pytest.param(
            local_reference_dates["01.01.1970"], "01.01.1970", id="01.01.1970"
        ),
        pytest.param(
            local_reference_dates["08.05.1975"], "08.05.1975", id="08.05.1975"
        ),
        pytest.param(
            local_reference_dates["17.02.1978"], "17.02.1978", id="17.02.1978"
        ),
        pytest.param(
            local_reference_dates["25.10.1986"], "25.10.1986", id="25.10.1986"
        ),
        pytest.param(
            local_reference_dates["13.05.1992"], "13.05.1992", id="13.05.1992"
        ),
        pytest.param(
            local_reference_dates["08.11.1997"], "08.11.1997", id="08.11.1997"
        ),
        pytest.param(
            local_reference_dates["01.01.2000"], "01.01.2000", id="01.01.2000"
        ),
        pytest.param(
            local_reference_dates["06.07.2005"], "06.07.2005", id="06.07.2005"
        ),
        pytest.param(
            local_reference_dates["01.10.2017"], "01.10.2017", id="01.10.2017"
        ),
        pytest.param(
            local_reference_dates["20.03.2021"], "20.03.2021", id="20.03.2021"
        ),
    ],
)
def test_nextTzolkin(tzolkin: TzolkinDate, gregorian: str, day_diff: int) -> None:
    """Test the function `nextTzolkin`."""
    given_date = datetime.datetime.strptime(gregorian, USED_DATEFMT).date()
    start_date = given_date - datetime.timedelta(days=day_diff)
    assert nextTzolkin(tzolkin=tzolkin, starting=start_date) == given_date  # nosec


################################################################################
@settings(max_examples=500, deadline=None)
@given(day_diff=st.integers(min_value=1, max_value=260))
@pytest.mark.parametrize(
    "tzolkin, gregorian",
    [
        pytest.param(
            local_reference_dates["01.01.1800"], "01.01.1800", id="01.01.1800"
        ),
        pytest.param(
            local_reference_dates["12.12.1926"], "12.12.1926", id="12.12.1926"
        ),
        pytest.param(
            local_reference_dates["26.01.1958"], "26.01.1958", id="26.01.1958"
        ),
        pytest.param(
            local_reference_dates["15.03.1967"], "15.03.1967", id="15.03.1967"
        ),
        pytest.param(
            local_reference_dates["01.01.1970"], "01.01.1970", id="01.01.1970"
        ),
        pytest.param(
            local_reference_dates["08.05.1975"], "08.05.1975", id="08.05.1975"
        ),
        pytest.param(
            local_reference_dates["17.02.1978"], "17.02.1978", id="17.02.1978"
        ),
        pytest.param(
            local_reference_dates["25.10.1986"], "25.10.1986", id="25.10.1986"
        ),
        pytest.param(
            local_reference_dates["13.05.1992"], "13.05.1992", id="13.05.1992"
        ),
        pytest.param(
            local_reference_dates["08.11.1997"], "08.11.1997", id="08.11.1997"
        ),
        pytest.param(
            local_reference_dates["01.01.2000"], "01.01.2000", id="01.01.2000"
        ),
        pytest.param(
            local_reference_dates["06.07.2005"], "06.07.2005", id="06.07.2005"
        ),
        pytest.param(
            local_reference_dates["01.10.2017"], "01.10.2017", id="01.10.2017"
        ),
        pytest.param(
            local_reference_dates["20.03.2021"], "20.03.2021", id="20.03.2021"
        ),
    ],
)
def test_lastTzolkin(tzolkin: TzolkinDate, gregorian: str, day_diff: int) -> None:
    """Test the function `lastTzolkin`."""
    given_date = datetime.datetime.strptime(gregorian, USED_DATEFMT).date()
    start_date = given_date + datetime.timedelta(days=day_diff)
    assert lastTzolkin(tzolkin=tzolkin, starting=start_date) == given_date  # nosec

# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Roland Csaszar
#
# Project:  tzolkin-calendar
# File:     test_tzolkin.py
# Date:     21.Mar.2021
###############################################################################
"""Test tzolkin module."""

from __future__ import annotations

import pytest

from tzolkin_calendar import TzolkinDate, TzolkinException
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

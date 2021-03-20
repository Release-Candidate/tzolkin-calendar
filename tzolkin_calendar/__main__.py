# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Roland Csaszar
#
# Project:  tzolkin-calendar
# File:     __main__.py
# Date:     19.Mar.2021
###############################################################################
"""The main entry point of the program, does nothing but call the 'real' main function `main`."""

from __future__ import annotations

import tzolkin_calendar
from tzolkin_calendar.calculate import getTzolkinDiff
from tzolkin_calendar.tzolkin import Tzolkin


################################################################################
def main() -> None:
    """Main function of the program."""
    print(tzolkin_calendar.DayGlyphs)
    print(tzolkin_calendar.TzolkinDate(number=4, name=6))
    print(
        getTzolkinDiff(
            start=tzolkin_calendar.TzolkinDate(number=4, name=7),
            end=tzolkin_calendar.TzolkinDate(number=3, name=19),
        )
    )
    print(
        getTzolkinDiff(
            start=tzolkin_calendar.TzolkinDate(number=8, name=11),
            end=tzolkin_calendar.TzolkinDate(number=11, name=1),
        )
    )
    print(Tzolkin(number=4, name_number=7))
    print(Tzolkin(number=4, name_str="Ebʼ"))
    try:
        print(Tzolkin(number=4, name_str="BLA"))
    except tzolkin_calendar.TzolkinException as excp:
        print(excp)
    try:
        print(Tzolkin(number=4, name_number=87))
    except tzolkin_calendar.TzolkinException as excp:
        print(excp)

    try:
        print(Tzolkin(number=14, name_number=6))
    except tzolkin_calendar.TzolkinException as excp:
        print(excp)


if __name__ == "__main__":
    main()

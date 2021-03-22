# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Roland Csaszar
#
# Project:  tzolkin-calendar
# File:     main.py
# Date:     21.Mar.2021
###############################################################################
"""The main entry point of the program if tzolkin_calender is not imported, but called
as a script.
"""

from __future__ import annotations

import argparse
import datetime
import re
import sys
from typing import Optional

from tzolkin_calendar import USED_DATEFMT, VERSION

from .tzolkin import Tzolkin

__description = """A Tzolk’in date converter and calculator.

Examples:

To get the Tzolk’in date of today:

 python -m tzolkin_calendar

To get the next and last gregorian dates with a Tzolk’in date of '8 Chuwen' you can use either:

 python -m tzolkin_calendar 8 Chuwen
 python -m tzolkin_calendar 8/Chuwen
 python -m tzolkin_calendar 8.Chuwen
 python -m tzolkin_calendar 8-Chuwen
 python -m tzolkin_calendar 8 11
 python -m tzolkin_calendar 8/11
 python -m tzolkin_calendar 8.11
 python -m tzolkin_calendar 8-11

To get the Tzolk’in date of the 16th april 2016, use one of these date formats:

    python -m tzolkin_calendar 16.04.2016
    python -m tzolkin_calendar 16/04/2016
    python -m tzolkin_calendar 16-04-2016
    python -m tzolkin_calendar 16 04 2016
    python -m tzolkin_calendar 2016.04.16
    python -m tzolkin_calendar 2016-04-16
    python -m tzolkin_calendar 2016/04/16
    python -m tzolkin_calendar 2016 04 16
    python -m tzolkin_calendar 04/16/2016
    python -m tzolkin_calendar 04.16.2016
    python -m tzolkin_calendar 04-16-2016
    python -m tzolkin_calendar 04 16 2016

"""
__gregorian_regex1 = re.compile(
    r"^([0-3]?[0-9])[\t .-/]([0-1]?[0-9])[\t .-/]([0-9][0-9][0-9][0-9])",
)
__gregorian_regex2 = re.compile(
    r"^([0-9][0-9][0-9][0-9])[\t .-/]([0-1]?[0-9])[\t .-/]([0-3]?[0-9])"
)
__gregorian_regex3 = re.compile(
    r"^([0-1]?[0-9])[\t .-/]([0-3]?[0-9])[\t .-/]([0-9][0-9][0-9][0-9])"
)
__tzolkin_regex1 = re.compile(r"([0-1]?[0-9])[\t .-/]([0-2]?[0-9])")
__tzolkin_regex2 = re.compile(r"([0-1]?[0-9])[\t .-/](\s+)")


################################################################################
def main() -> None:
    """Main function, called if this is called as a script and not imported."""
    cmd_line_parser = argparse.ArgumentParser(
        prog="python -m tzolkin_calendar",
        formatter_class=argparse.RawTextHelpFormatter,
        description=__description,
        epilog="See website https://github.com/Release-Candidate/tzolkin_calendar for a detailed description.",
    )

    cmd_line_parser.add_argument(
        "--version",
        action="version",
        version="Buildnis {version}".format(version=VERSION),
    )

    cmd_line_parser.add_argument(
        "date",
        metavar="DATE",
        nargs="*",
        help="The date to parse and convert. Either a Tzolk’in date or a gregorian date can be given. The default is the date of today.",
        default=datetime.date.today().strftime("%d.%m.%Y"),
    )

    cmdline_args = cmd_line_parser.parse_args()

    date_str = ""
    if isinstance(cmdline_args.date, list):
        date_str = " ".join(cmdline_args.date)
    else:
        date_str = cmdline_args.date

    print("Parsing date {date}".format(date=date_str))

    parsed_date = __parseGregorian(date_str)

    if parsed_date is not None:
        print(Tzolkin.fromDateString(date_str=parsed_date, fmt="%d.%m.%Y"))
        sys.exit(0)

    tzolkin_number = 0
    tzolkin_day_number = 0

    result = __tzolkin_regex1.search(date_str)
    if result:
        tzolkin_number = int(result.group(1))
        tzolkin_day_number = int(result.group(2))

    result = __tzolkin_regex1.search(date_str)
    if result:
        tzolkin_number = int(result.group(1))
        tzolkin_day_name = result.group(2)
        print(tzolkin_day_name)

    if tzolkin_number * tzolkin_day_number != 0:
        print(Tzolkin(number=tzolkin_number, name_number=tzolkin_day_number))
        print(
            Tzolkin(number=tzolkin_number, name_number=tzolkin_day_number)
            .getLastDate()
            .strftime(USED_DATEFMT)
        )
        print(
            Tzolkin(number=tzolkin_number, name_number=tzolkin_day_number)
            .getNextDate()
            .strftime(USED_DATEFMT)
        )


################################################################################
def __parseGregorian(date_str: str) -> Optional[str]:
    """Tries to parse the given string as a gregorian date.
    Return the string 'DD.MM.YYYY' on success, `None`else.

    Args:
        date_str (str): The string to parse

    Returns:
        Optional[str]: The string 'DD.MM.YYYY' on success, `None`else.
    """
    day = ""
    month = ""
    year = ""
    result = __gregorian_regex1.search(date_str)
    if result:
        day = result.group(1)
        month = result.group(2)
        year = result.group(3)
        return ".".join([day, month, year])

    result = __gregorian_regex2.search(date_str)
    if result:
        day = result.group(3)
        month = result.group(2)
        year = result.group(1)
        return ".".join([day, month, year])

    result = __gregorian_regex3.search(date_str)
    if result:
        day = result.group(2)
        month = result.group(1)
        year = result.group(3)
        return ".".join([day, month, year])

    return None

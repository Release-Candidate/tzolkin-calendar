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
from typing import Dict, Optional, Tuple

from tzolkin_calendar import USED_DATEFMT, TzolkinDate, TzolkinException
from tzolkin_calendar.calculate import makeLookUpTable, parseTzolkinName
from tzolkin_calendar.commandline import parseCommandline

from .tzolkin import Tzolkin

# Regexes to parse date strings, gregorian and Tzolkin dates.
__gregorian_regex1 = re.compile(
    r"^([0-3]?[0-9])[\t .\-/]([0-1]?[0-9])[\t .\-/]([0-9][0-9][0-9][0-9])",
)
__gregorian_regex2 = re.compile(
    r"^([0-9][0-9][0-9][0-9])[\t .\-/]([0-1]?[0-9])[\t .\-/]([0-3]?[0-9])"
)
__gregorian_regex3 = re.compile(r"^([0-1]?[0-9])/([0-3]?[0-9])/([0-9][0-9][0-9][0-9])")
__tzolkin_regex1 = re.compile(r"([0-1]?[0-9])[\t .\-/]([0-2]?[0-9])")
__tzolkin_regex2 = re.compile(r"([0-1]?[0-9])[\t .\-/](\S+)")


################################################################################
def main() -> None:
    """Main function, called if this is called as a script and not imported."""
    cmd_line_parser, cmdline_args = parseCommandline()

    date_str = ""
    if isinstance(cmdline_args.date, list):
        date_str = " ".join(cmdline_args.date)
    else:
        date_str = cmdline_args.date

    __displayYear(cmdline_args)

    __date2gregorian(cmd_line_parser, date_str)

    tzolkin_number, tzolkin_day_number = __date2Tzolkin(
        cmd_line_parser, cmdline_args, date_str
    )

    __nothingFound(
        cmd_line_parser=cmd_line_parser,
        date_str=date_str,
        tzolkin_number=tzolkin_number,
        tzolkin_day_number=tzolkin_day_number,
    )


################################################################################
def __date2Tzolkin(
    cmd_line_parser: argparse.ArgumentParser,
    cmdline_args: argparse.Namespace,
    date_str: str,
) -> Tuple[int, int]:
    """Try to parse the given date string as a Tzolkin date and display the next and
    last gregorian dates with the same Tzolkin date.

    Args:
        cmd_line_parser (argparse.ArgumentParser): The command line parser object.
        cmdline_args (argparse.Namespace): The object holding all command line arguments.
        date_str (str): The Tzolkin date string to parse.

    Returns:
        Tuple[int, int]: The Tzolkin day number and day name number on success, the
        tuple (0, 0) if no Tzolkin date could be parsed.
    """
    tzolkin_number, tzolkin_day_number = __parseTzolkin(date_str=date_str)
    if tzolkin_number * tzolkin_day_number != 0:
        __searchTzolkinDates(
            cmd_line_parser, cmdline_args, date_str, tzolkin_number, tzolkin_day_number
        )

    return tzolkin_number, tzolkin_day_number


################################################################################
def __searchTzolkinDates(
    cmd_line_parser: argparse.ArgumentParser,
    cmdline_args: argparse.Namespace,
    date_str: str,
    tzolkin_number: int,
    tzolkin_day_number: int,
) -> None:
    """[summary]

    Args:
        cmd_line_parser (argparse.ArgumentParser): [description]
        cmdline_args (argparse.Namespace): [description]
        date_str (str): [description]
        tzolkin_number (int): [description]
        tzolkin_day_number (int): [description]
    """
    try:
        if cmdline_args.start_date is not None:
            start_date = datetime.datetime.strptime(
                __parseGregorian(cmdline_args.start_date), USED_DATEFMT
            ).date()
        else:
            start_date = datetime.date.today()
        tzolkin = Tzolkin(number=tzolkin_number, name_number=tzolkin_day_number)
        if cmdline_args.list_size is None:
            __printTzolkin(start_date=start_date, tzolkin=tzolkin)
        else:
            __printTzolkinList(
                cmdline_args=cmdline_args,
                start_date=start_date,
                tzolkin=tzolkin,
            )
    except TzolkinException as excp:
        __errorParsingTzolkin(cmd_line_parser, date_str, excp)


################################################################################
def __date2gregorian(cmd_line_parser: argparse.ArgumentParser, date_str: str) -> None:
    """Try to parse the given date as a gregorian date and convert it to a Tzolkin date.

    Args:
        cmd_line_parser (argparse.ArgumentParser): The command line parser object.
        date_str (str): The string to try to parse as a gregorian date.
    """
    parsed_date = __parseGregorian(date_str=date_str)
    try:
        if parsed_date is not None:
            __printTzolkinSingle(date_str, parsed_date)
    except Exception as excp:
        __errorParsingDate(cmd_line_parser, parsed_date, excp)


################################################################################
def __errorParsingDate(
    cmd_line_parser: argparse.ArgumentParser, parsed_date: str, excp: TzolkinException
) -> None:
    """Print the error message of `TzolkinException` and exit.

    Args:
        cmd_line_parser (argparse.ArgumentParser): The command line parser object.
        parsed_date (str): The string that failed to be parsed.
        excp (TzolkinException): The raised exception.
    """
    print(
        'error "{error}" parsing date "{date}". Exiting'.format(
            error=excp, date=parsed_date
        ),
        file=sys.stderr,
    )
    cmd_line_parser.print_help()
    sys.exit(2)


################################################################################
def __errorParsingTzolkin(
    cmd_line_parser: argparse.ArgumentParser, date_str: str, excp: TzolkinException
) -> None:
    """Display the error message of the TzolkinException and exit.

    Args:
        cmd_line_parser (argparse.ArgumentParser): The command line parser object.
        date_str (str): The string that failed to be parsed.
        excp (TzolkinException): The raised exception.
    """
    print(
        'error "{error}" parsing Tzolkin date "{date}"'.format(
            error=excp,
            date=date_str,
        ),
        file=sys.stderr,
    )
    cmd_line_parser.print_help()
    sys.exit(2)


################################################################################
def __printTzolkinSingle(date_str: str, parsed_date: str) -> None:
    """Print the converted gregorian date as Tzolkin date and exit.

    Args:
        date_str (str): The given gregorian string.
        parsed_date (str): The parsed result of the given gregorian string.
    """
    print(
        'Gregorian "{greg}" is "{tzolk}" as Tzolkin'.format(
            greg=date_str,
            tzolk=Tzolkin.fromDateString(date_str=parsed_date, fmt="%d.%m.%Y"),
        )
    )
    sys.exit(0)


################################################################################
def __parseTzolkin(date_str: str) -> Tuple[int, int]:
    """Parse the given string to find a Tzolkin date string.

    Args:
        date_str (str): The string to parse for a Tzolkin day string of the form
                        'NUMBER DAY_NAME'
    Returns:
        Tuple[int, int]: Returns the Tzolkin day number and Tzolkin day name number as a
                        Tuple.
    """
    tzolkin_number = 0
    tzolkin_day_number = 0
    result = __tzolkin_regex1.search(date_str)

    if result:
        tzolkin_number = int(result.group(1))
        tzolkin_day_number = int(result.group(2))

    result = __tzolkin_regex2.search(date_str)
    if result:
        tzolkin_number = int(result.group(1))
        tzolkin_day_name = result.group(2)
        tzolkin_day_number = parseTzolkinName(tzolkin_day_name)

    return tzolkin_number, tzolkin_day_number


################################################################################
def __printTzolkin(
    start_date: datetime.date,
    tzolkin: Tzolkin,
) -> None:
    """Print the next and last dates with the same tzolkin date as the given one.

    Args:
        tzolkin_number (int): [description]
        tzolkin_day_number (int): [description]
        start_date (datetime.date): [description]
        tzolkin (Tzolkin): [description]
    """
    last_date = tzolkin.getLastDate(start_date=start_date).strftime(USED_DATEFMT)
    next_date = tzolkin.getNextDate(start_date=start_date).strftime(USED_DATEFMT)
    print(
        'Tzolkin date "{tzolk}" next date is "{next}", last date has been "{last}"'.format(
            tzolk=tzolkin, next=next_date, last=last_date
        )
    )
    sys.exit(0)


################################################################################
def __printTzolkinList(
    cmdline_args: argparse.Namespace,
    start_date: datetime.date,
    tzolkin: Tzolkin,
) -> None:
    """Print the list of dates with the same Tzolkin date as the given one.

    Args:
        cmdline_args (argparse.Namespace): The command line arguments in a `Namespace` object.
        tzolkin_number (int): The number of the Tzolkin day to search.
        tzolkin_day_number (int): The day name number of the tzolkin day to search.
        start_date (datetime.date): The gregorian date to start the search on.
        tzolkin (Tzolkin): [description]
    """
    last_date_list = tzolkin.getLastDateList(
        start_date=start_date, list_size=cmdline_args.list_size
    )
    next_date_list = tzolkin.getNextDateList(
        start_date=start_date, list_size=cmdline_args.list_size
    )
    print(
        'Tzolkin date "{tzolk}"\n next dates are {next}\n last dates have been {last}'.format(
            tzolk=tzolkin,
            next=[a.strftime(USED_DATEFMT) for a in next_date_list],
            last=[a.strftime(USED_DATEFMT) for a in last_date_list],
        )
    )
    sys.exit(0)


################################################################################
def __nothingFound(
    cmd_line_parser: argparse.ArgumentParser,
    date_str: str,
    tzolkin_number: int,
    tzolkin_day_number: int,
) -> None:
    """Exit with an error if no date has been found.

    Args:
        cmd_line_parser (argparse.ArgumentParser): The command line parser instance.
        date_str (str): The date string to parse.
        tzolkin_number (int): The Tzolkin day number.
        tzolkin_day_number (int): The number of the Tzolkin day name.
    """
    if tzolkin_number * tzolkin_day_number == 0:
        print('Error parsing date "{date}"'.format(date=date_str), file=sys.stderr)
        cmd_line_parser.print_help()
        sys.exit(2)


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


################################################################################
def __displayYear(cmdline_args: argparse.Namespace) -> None:
    """If the argument 'show year' has been given, display all days of a Tzolkin year.

    Args:
        cmdline_args (argparse.Namespace): The object holding all command line
                            arguments.
    """
    if cmdline_args.display_year:
        year_dict = makeLookUpTable()

        __displayYearList(year_dict)


################################################################################
def __displayYearList(year_dict: Dict[int, TzolkinDate]) -> None:
    """Display the list of Tzolkin days in a Tzolkin year.

    Args:
        year_dict (Dict[int, TzolkinDate]): The dictionary of days in a Tzolkin year.
    """
    key_string = ""
    for key in year_dict:
        key_string = " ".join([key_string, year_dict[key].__repr__()])
        if key % 13 == 0:
            print(key_string)
            key_string = ""

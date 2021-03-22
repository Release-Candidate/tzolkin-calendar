# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Roland Csaszar
#
# Project:  tzolkin-calendar
# File:     commandline.py
# Date:     22.Mar.2021
###############################################################################
"""All  functions to parse the command line arguments of the program."""


from __future__ import annotations

import argparse
import datetime
from typing import Tuple

from tzolkin_calendar import VERSION

__description = """A Tzolkin date converter and calculator.

Examples:

To get the Tzolkin date of today:

 python -m tzolkin_calendar

To get the next and last gregorian dates with a Tzolkin date of '8 Chuwen' you can use either:

 python -m tzolkin_calendar 8 Chuwen
 python -m tzolkin_calendar 8/Chuwen
 python -m tzolkin_calendar 8.Chuwen
 python -m tzolkin_calendar 8-Chuwen
 python -m tzolkin_calendar 8 11
 python -m tzolkin_calendar 8/11
 python -m tzolkin_calendar 8.11
 python -m tzolkin_calendar 8-11

To get the Tzolkin date of the 16th april 2016, use one of these date formats:

    python -m tzolkin_calendar 16.04.2016
    python -m tzolkin_calendar 16-04-2016
    python -m tzolkin_calendar 16 04 2016
    python -m tzolkin_calendar 2016.04.16
    python -m tzolkin_calendar 2016-04-16
    python -m tzolkin_calendar 2016/04/16
    python -m tzolkin_calendar 2016 04 16
    python -m tzolkin_calendar 04/16/2016

"""


################################################################################
def parseCommandline() -> Tuple[argparse.ArgumentParser, argparse.Namespace]:
    """Parse the command line the program has been called with.

    Returns:
        Tuple[argparse.ArgumentParser, argparse.Namespace]: The command line parser
                instance and an object holding the parsed command line arguments.
    """
    cmd_line_parser = argparse.ArgumentParser(
        prog="python -m tzolkin_calendar",
        formatter_class=argparse.RawTextHelpFormatter,
        description=__description,
        epilog="See website https://github.com/Release-Candidate/tzolkin_calendar for a detailed description.",
    )
    cmd_line_parser.add_argument(
        "--version",
        action="version",
        version="tzolkin-calendar {version}".format(version=VERSION),
    )
    cmd_line_parser.add_argument(
        "-l",
        "--list",
        metavar="LIST_LENGTH",
        help="Display a list of dates with the given Tzolkin date instead of a single one. The length of the list is LIST_LENGTH.",
        dest="list_size",
        type=int,
        default=None,
    )
    cmd_line_parser.add_argument(
        "-s",
        "--start",
        metavar="START_DATE",
        help="The start date to begin the search for the dates with the same Tzolkin date. The same formatting rules apply as for the main argument DATE.",
        dest="start_date",
        type=str,
        default=None,
    )
    cmd_line_parser.add_argument(
        "date",
        metavar="DATE",
        nargs="*",
        help="The date to parse and convert. Either a Tzolkin date or a gregorian date can be given. The default is the date of today.",
        default=datetime.date.today().strftime("%d.%m.%Y"),
    )

    cmdline_args = cmd_line_parser.parse_args()

    return cmd_line_parser, cmdline_args

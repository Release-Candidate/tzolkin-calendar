# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Roland Csaszar
#
# Project:  tzolkin-calendar
# File:     __init__.py
# Date:     19.Mar.2021
###############################################################################

from __future__ import annotations

from typing import Dict, Literal, NamedTuple

__all__ = ["calculate", "tzolkin"]

VERSION: str = "0.8.0"


################################################################################
class TzolkinException(Exception):
    """This excpetion is raised when an error occurred.
    Mostly this is because of an invalid Tzolkin day number (not in 1 to 13) or day
    name or day name number (not in 1 to 20).
    """


TzolkinName = Literal[
    "Imix",
    "Ikʼ",
    "Akʼbʼal",
    "Kʼan",
    "Chikchan",
    "Kimi",
    "Manikʼ",
    "Lamat",
    "Muluk",
    "Ok",
    "Chuwen",
    "Ebʼ",
    "Bʼen",
    "Ix",
    "Men",
    "Kʼibʼ",
    "Kabʼan",
    "Etzʼnabʼ",
    "Kawak",
    "Ajaw",
]

TzolkinNumber = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
TzolkinNameNumber = Literal[
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
]


################################################################################
class TzolkinDate(NamedTuple):
    """Tuple that holds the Tzolkin day number and day name in `number` and `name`."""

    number: int
    name: int

    def __repr__(self) -> str:
        """Return the Tzolkin date as day number and day name including the Unicode
        glyph for the name.

        Returns:
            str: The Tzolkin date as day number and day name and the day name
                 Unicode glyph..
        """
        # TODO if Unicode adds the Tzolkin day name glyphs, add them here!
        # return "{number} {name} ({glyph})".format(
        #     number=day_numbers[self.number],
        #     name=day_names[self.name],
        #     glyph=day_glyphs[self.name],
        # )
        return "{number} {name}".format(
            number=day_numbers[self.number],
            name=day_names[self.name],
        )


# some reference days in Tzolkin, actually used is "01.01.1970"
REFERENCE_DATES = {
    "01.01.1970": TzolkinDate(number=13, name=5),
    "01.01.1800": TzolkinDate(number=10, name=14),
    "01.01.2000": TzolkinDate(number=11, name=2),
}

# The default date format string to use when outputing.
USED_DATEFMT = "%d.%m.%Y"

# The numbers of a Tzolkin day, from 1 to 13 (including 1 and 13)
DayNumbers = Dict[TzolkinNumber, str]
day_numbers = {
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "11",
    12: "12",
    13: "13",
}

# The 20 names of a Tzolkin day, from Imix to Ajaw (including Imix and Ajaw)
DayNames = Dict[TzolkinNameNumber, str]
day_names = {
    1: "Imix",
    2: "Ikʼ",
    3: "Akʼbʼal",
    4: "Kʼan",
    5: "Chikchan",
    6: "Kimi",
    7: "Manikʼ",
    8: "Lamat",
    9: "Muluk",
    10: "Ok",
    11: "Chuwen",
    12: "Ebʼ",
    13: "Bʼen",
    14: "Ix",
    15: "Men",
    16: "Kʼibʼ",
    17: "Kabʼan",
    18: "Etzʼnabʼ",
    19: "Kawak",
    20: "Ajaw",
}

# The 20 glyphs for the Tzolkin day names, from Imix to Ajaw (including Imix and Ajaw).
#
DayGlyphs = Dict[TzolkinNameNumber, str]
day_glyphs = {
    1: "\U000153E2",
    2: "\U000153E7",
    3: "\U000153E9",
    4: "\U000153EC",
    5: "\U000153EF",
    6: "\U000153F2",
    7: "\U000153F5",
    8: "\U000153F7",
    9: "\U000153FB",
    10: "\U000153FF",
    11: "\U00015403",
    12: "\U00015406",
    13: "\U0001540A",
    14: "\U0001540C",
    15: "\U0001540F",
    16: "\U00015412",
    17: "\U00015416",
    18: "\U0001541A",
    19: "\U0001541D",
    20: "\U0001541F",
}

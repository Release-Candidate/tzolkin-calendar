# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Roland Csaszar
#
# Project:  tzolkin-calendar
# File:     calculate.py
# Date:     19.Mar.2021
###############################################################################
"""This modules holds functions needed to calculate with Tzolkin calendar dates and
convert them to and from gregorian dates.

Example:
>>> import datetime
>>> import tzolkin_calendar.calculate
>>> tzolkin_calendar.calculate.gregorian2tzolkin(datetime.datetime.strptime("23.05.2014", "%d.%m.%Y"))
2 Etzʼnabʼ (𕐚)

>>> import datetime
>>> import tzolkin_calendar.calculate
>>> tzolkin_calendar.calculate.nextTzolkin(tzolkin_calendar.TzolkinDate(name=3, number=5))
datetime.date(2021, 4, 21)

>>> import datetime
>>> import tzolkin_calendar.calculate
>>> tzolkin_calendar.calculate.lastTzolkin(tzolkin_calendar.TzolkinDate(name=17, number=3))
datetime.date(2021, 1, 5)

>>> import datetime
>>> import tzolkin_calendar.calculate
>>> tzolkin_calendar.calculate.tzolkin2gregorian(tzolkin_calendar.TzolkinDate(name="2", number="7"),start=datetime.date.today())
[datetime.date(2021, 10, 15), datetime.date(2022, 7, 2), datetime.date(2023, 3, 19), datetime.date(2023, 12, 4),

>>> import datetime
>>> import tzolkin_calendar.calculate
>>> tzolkin_calendar.calculate.tzolkin2gregorian(tzolkin_calendar.TzolkinDate(name="2", number="7"), forward=False, start=datetime.date.today())
[datetime.date(2021, 10, 15), datetime.date(2021, 1, 28), datetime.date(2020, 5, 13), datetime.date(2019, 8, 27),

Functions:
    gregorian2tzolkin(date: datetime.date) -> TzolkinDate
    tzolkin2gregorian(tzolkin: TzolkinDate, start: datetime.date,
                num_results: int = 100, forward: bool = True) -> List[datetime.date]
    nextTzolkin(tzolkin: TzolkinDate, starting: datetime.date) -> datetime.date
    lastTzolkin(tzolkin: TzolkinDate, starting: datetime.date) -> datetime.date
    getTzolkinDiff(start: TzolkinDate, end: TzolkinDate) -> int
    getTzolkinDay(tzolkin: TzolkinDate) -> int
    parseTzolkinName(name_str: str) -> int
    calculateTzolkinName(start_name: int, to_add: int) -> int
    calculateTzolkinNumber(start_number: int, to_add: int) -> int
    makeLookUpTable() -> Dict[int, TzolkinDate]
"""

from __future__ import annotations

import datetime
from typing import Dict, List, Tuple

from tzolkin_calendar import (
    REFERENCE_DATES,
    USED_DATEFMT,
    TzolkinDate,
    day_names,
    day_numbers,
)


################################################################################
def makeLookUpTable() -> Dict[int, TzolkinDate]:
    """Return a dictionary holding all `TzolkinDate` instances of a tzolkin year.
    The tzolkin year consists of all combinations of `day_names` and `ay_numbers`,
    `day_numbers` are the numbers from 1 to 13 and `day_names` the names from
    'Imix' to 'Ajaw'. So a Tzolkin year is: 1 Imix, 2 Ik', 3 Ak'b'al, ... and
    finishes at 12 Kawak and finally 13 Ajaw.

    Returns:
        Dict[int, TzolkinDate]: The dictionary of all tzolkin date combinations in a
                                tzolkin year (of 260 days).
    """
    ret_val: Dict[int, TzolkinDate] = {}
    num_elems = len(day_names) * len(day_numbers)
    for day in range(0, num_elems):
        tz_name = calculateTzolkinName(start_name=1, to_add=day)
        tz_number = calculateTzolkinNumber(start_number=1, to_add=day)
        ret_val[day + 1] = TzolkinDate(name=tz_name, number=tz_number)

    return ret_val


################################################################################
def getTzolkinDiff(start: TzolkinDate, end: TzolkinDate) -> int:
    """Return the difference in days between the two given Tzolkin dates.
    No negative differences are returned, but the number of days to reach the `end` date
    if starting from `start`. If `start` is earlier than `end` the difference is
    `start` - `end`. If `end` is before `start`, 260 - `start` + `end`
    (same as 260 - (`end` - `start`)) is returned.

    Example:
        getTzolkinDiff returns 12 for `start` = 4 Manikʼ and `end` = 3 Kawak
                                (`end` - `start`)
        ```
        getTzolkinDiff(
            start=tzolkin_calendar.TzolkinDate(number=4, name=7),
            end=tzolkin_calendar.TzolkinDate(number=3, name=19),
        ) == 12
        ```

        getTzolkinDiff returns 250 for `start` = 8 Chuwen and `end` = 11 Imix
        ```
        getTzolkinDiff(
            start=tzolkin_calendar.TzolkinDate(number=8, name=11),
            end=tzolkin_calendar.TzolkinDate(number=11, name=1),
        ) == 250
        ```

    Args:
        start (TzolkinDate): The Tzolkin date to start the calculation from.
        end (TzolkinDate): The Tzolkin date to calculate the time difference in days to.

    Returns:
        int: The number of days between the two given dates. Never negative (0 if
        `start` and `end` are the same day).
    """
    ret_val = 0

    table = makeLookUpTable()

    day1, day2 = __getDays(start, end, table)

    num_elems = len(day_names) * len(day_numbers)
    if day2 > day1:
        ret_val = day2 - day1
    else:
        ret_val = num_elems - day1 + day2

    return ret_val


################################################################################
def __getDays(
    start: TzolkinDate, end: TzolkinDate, table: Dict[int, TzolkinDate]
) -> Tuple[int, int]:
    """Return the day indices of each day in the Tzolkin year.

    Args:
        start (TzolkinDate): The first Tzolkin date to get the day index of.
        end (TzolkinDate): The second Tzolkin date to get the day index of.
        table (Dict[int, TzolkinDate]): The dictionary containing all 260 Tzolkin days
                                     of a Tzolkin year.

    Returns:
        Tuple[int, int]: the indices of the days `start` in the first element and
                            `end` in the second.
    """
    day1 = 0
    day2 = 0
    for day in table:
        ret_val = __getDayIdx(start, table, day)
        if ret_val:
            day1 = ret_val
        ret_val = __getDayIdx(end, table, day)
        if ret_val:
            day2 = ret_val

    return day1, day2


################################################################################
def __getDayIdx(tzolkin: TzolkinDate, table: Dict[int, TzolkinDate], day: int) -> int:
    """Return the day's number in the Tzolkin year if the given day is the same as
    the Tzolkin date.

    Args:
        tzolkin (TzolkinDate): The Tzolkin date to search for in the Tzolkin year.
        table (Dict[int, TzolkinDate]): The dictionary of Tzolkin dates in a Tzolkin year.
        day (int): The current key in the Tzolkin year dict to check.

    Returns:
        int: The index of the current date in the Tzolkin year if it is the same as
                `tzolkin`, 0 else.
    """
    ret_val: int = 0
    if table[day].name == tzolkin.name and table[day].number == tzolkin.number:
        ret_val = day

    return ret_val


################################################################################
def getTzolkinDay(tzolkin: TzolkinDate) -> int:
    """Return the day number in the Tzolkin year, in the interval [1,260] (including
    both 1 and 260).
    That is, the index of the given Tzolkin date in the 260 day Tzolkin year.
    `1 Imix` yields 1 (the first day of the year), `13 Ajaw` yields 260, the last day
    of the Tzolkin year. If the given date `tzolkin` does not exist, `0` is returned.

    Args:
        tzolkin (TzolkinDate): The Tzolkin date to get the day in the year of.

    Returns:
        int: The day of the given date in the Tzolkin year, a positive integer between
            and including 1 and 260.
            If the given date does not exist, `0` is returned.
    """
    ret_val = 0

    table = makeLookUpTable()

    for day in table:
        if table[day].name == tzolkin.name and table[day].number == tzolkin.number:
            ret_val = day

    return ret_val


################################################################################
def gregorian2tzolkin(date: datetime.date) -> TzolkinDate:
    """Return the Tzolkin date of the given gregorian date.

    Args:
        date (datetime.date): The gregorian date to convert to Tzolkin.

    Returns:
        TzolkinDate: The Tzolkin date of the given day `date`.
    """
    ref_date_str = "01.01.1970"
    reference_date = datetime.datetime.strptime(ref_date_str, USED_DATEFMT)
    date_diff = date - reference_date.date()

    diff_days = date_diff.days + getTzolkinDay(REFERENCE_DATES[ref_date_str])

    num_elems = len(day_names) * len(day_numbers)
    tzolkin_date = diff_days % num_elems

    tzolkin_name = tzolkin_date % len(day_names)
    if tzolkin_name == 0:
        tzolkin_name = len(day_names)
    tzolkin_number = tzolkin_date % len(day_numbers)
    if tzolkin_number == 0:
        tzolkin_number = len(day_numbers)

    return TzolkinDate(number=tzolkin_number, name=tzolkin_name)


################################################################################
def tzolkin2gregorian(
    tzolkin: TzolkinDate,
    start: datetime.date,
    num_results: int = 100,
    forward: bool = True,
) -> List[datetime.date]:
    """Return a list of dates having the same Tzolkin date as the given date `tzolkin`.

    If `num_results` is smaller than 1, an empty list is returned.

    Args:
        tzolkin (TzolkinDate): The Tzolkin date to search for.
        start (datetime.date): The gregorian date to start the search from.
        num_results (int, optional): The number of results to return. If this is < 1,
                                    an empty list is returned. Defaults to 100.
        forward (bool, optional): The direction in time to search. Either forward (if
        `forward` is `True`) or backwards (if `forward` is `False`). Defaults to True.

    Returns:
        List[datetime.date]: The list of gregorian dates having the same Tzolkin date as
                            `tzolkin`. The number of elements of this list is
                            `num_results`.
    """
    ret_val: List[datetime.date] = []
    if num_results < 1:
        return ret_val
    if forward:
        ret_val = [nextTzolkin(tzolkin=tzolkin, starting=start)]
        __forward(tzolkin, num_results, ret_val)
    else:
        ret_val = [lastTzolkin(tzolkin=tzolkin, starting=start)]
        __backward(tzolkin, num_results, ret_val)

    return ret_val


################################################################################
def __backward(
    tzolkin: TzolkinDate, num_results: int, ret_val: List[datetime.date]
) -> None:
    """Search forward in time for Tzolkin date `tzolkin` and append to the list.

    Args:
        tzolkin (TzolkinDate): The Tzolkin date to search for.
        num_results (int): The number of dates to search.
        ret_val (List[datetime.date]): The list of found dates with the same Tzolkin date.
    """
    results = 0
    while results < num_results - 1:
        ret_val.append(lastTzolkin(tzolkin=tzolkin, starting=ret_val[-1]))
        results += 1


################################################################################
def __forward(
    tzolkin: TzolkinDate, num_results: int, ret_val: List[datetime.date]
) -> None:
    """Search backwards in time for Tzolkin date `tzolkin` and append to the list.

    Args:
        tzolkin (TzolkinDate): The Tzolkin date to search for.
        num_results (int): The number of dates to search.
        ret_val (List[datetime.date]): The list of found dates with the same Tzolkin date.
    """
    results = 0
    while results < num_results - 1:
        ret_val.append(nextTzolkin(tzolkin=tzolkin, starting=ret_val[-1]))
        results += 1


################################################################################
def calculateTzolkinName(start_name: int, to_add: int) -> int:
    """Return the Tzolkin name `to_add` days after `start_name`.
    Add or subtracts the given integer to the index of the Tzolkin name and return
    the index of the new name. Adds `to_add` to the name index `start_name` and takes
    the value modulo 20. If the result would be 0, return 20 instead.

    Args:
        start_name (int): The index of the name to add days to.
        to_add (int): The number of days to add to the Tzolkin name.

    Returns:
        int: The index of the resulting Tzolkin name, `to_add` days after `start_name`.
    """
    ret_val = (start_name + to_add) % len(day_names)
    if ret_val == 0:
        ret_val = len(day_names)

    return ret_val


################################################################################
def calculateTzolkinNumber(start_number: int, to_add: int) -> int:
    """Return the Tzolkin number `to_add` days after `start_number`.
    Add or subtracts the given integer to the Tzolkin number and return the new number.
    Adds `to_add` to the number `start_name` and takes the value modulo 13. If the
    result would be 0, return 13 instead.

    Args:
        start_number (int): The number to add the days to.
        to_add (int): The number of days to add to the Tzolkin number.

    Returns:
        int: The resulting number `to_add` days after `start_number`.
    """
    ret_val = (start_number + to_add) % len(day_numbers)
    if ret_val == 0:
        ret_val = len(day_numbers)

    return ret_val


################################################################################
def parseTzolkinName(name_str: str) -> int:
    """Parse the given string to get a Tzolkin day name.
    Ignores lower- and uppercase, ignores all non-alphanumberic characters.

    Returns 0 if no name has been found

    Args:
        name_str (str): The string to parse to get a Tzolkin day name.

    Returns:
        int: The number of the found Tzolkin day name. 0 on errors.
    """
    ret_val = 0

    for num, name in day_names.items():
        if "".join(
            [a for a in name_str.upper() if a.isascii() and a.isalpha()]
        ) == "".join([a for a in name.upper() if a.isascii() and a.isalpha()]):
            ret_val: int = num

    return ret_val


################################################################################
def nextTzolkin(
    tzolkin: TzolkinDate, starting: datetime.date = datetime.date.today()
) -> datetime.date:
    """Return the next gregorian date after `starting`, that has a Tzolkin date of
    `tzolkin`.
    Search forward in time for a day with Tzolkin date `tzolkin`.

    Args:
        tzolkin (TzolkinDate): The Tzolkin date to search for.
        starting (datetime.date, optional): The date to start the search. Defaults to
                                            `datetime.date.today()`.

    Returns:
        datetime.date: The next gregorian date with the given Tzolkin date `tzolkin`
                        after `starting`.
    """
    tzolkin_start_date = gregorian2tzolkin(starting)

    days_diff = getTzolkinDiff(start=tzolkin_start_date, end=tzolkin)

    if days_diff == 0:
        num_elems = len(day_names) * len(day_numbers)
        days_diff = num_elems

    day_diff_delta = datetime.timedelta(days=days_diff)

    return starting + day_diff_delta


################################################################################
def lastTzolkin(
    tzolkin: TzolkinDate, starting: datetime.date = datetime.date.today()
) -> datetime.date:
    """Return the last gregorian date before `starting`, that has a Tzolkin date of
    `tzolkin`.
    Search backwards in time for a day with the  Tzolkin date `tzolkin`.

    Args:
        tzolkin (TzolkinDate): The Tzolkin date to search for.
        starting (datetime.date, optional): The date to start the search. Defaults to
                                            `datetime.date.today()`.

    Returns:
        datetime.date: The last gregorian date with the given Tzolkin date `tzolkin`
                        before `starting`.
    """
    tzolkin_start_date = gregorian2tzolkin(starting)

    days_diff = getTzolkinDiff(start=tzolkin, end=tzolkin_start_date)

    day_diff_delta = datetime.timedelta(days=(-1) * days_diff)

    return starting + day_diff_delta

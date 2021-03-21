# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Roland Csaszar
#
# Project:  tzolkin-calendar
# File:     tzolkin.py
# Date:     20.Mar.2021
###############################################################################
"""Main Tzolkin class."""

from __future__ import annotations

import datetime
from typing import List, Optional

from tzolkin_calendar.calculate import (
    calculateTzolkinName,
    calculateTzolkinNumber,
    getTzolkinDay,
    getTzolkinDiff,
    gregorian2tzolkin,
    lastTzolkin,
    makeLookUpTable,
    nextTzolkin,
    tzolkin2gregorian,
)

from . import TzolkinDate, TzolkinException, TzolkinName, day_names, day_numbers


class Tzolkin:
    """A representation of a Tzolkin date.
    Use to do calculations and conversions from and to gregorian dates to Tzolkin dates
    and search for days.

    Attributes:
        `fromDate`: Convert a gregorian date to a Tzolkin date.
        `fromDateString`: Convert a gregorian date to a Tzolkin date.
        `fromIsoFormat`: Convert a gregorian date to a Tzolkin date.
        `fromToday`: The Tzolkin date of today, the current day.
        `getTzolkinDate`: Return a `TzolkinDate`instance to use with
                                    `tzolkin_calendar.calculate` functions.
        `getDayNumber`: Return the Tzolkin day number, between 1 and 13.
        `getDayName`: Return the Tzolkin day name.
        `getDayNameNumber`: Return the Tzolkin day name as a number between 1 and 20.
        `getTzolkinYearDay`: Return the number of the dy in the Tzolkin year.
        `getNextDate`: Return the next day with the same Tzolkin date.
        `getNextDateList`: Return a list of days with the same Tzolkin date.
                            Search forward in time.
        `getLastDate`: Return the last day with the same Tzolkin date.
        `getLastDateList`: Return a list of days with the same Tzolkin date.
                            Search backwards in time.
        `addDays`: Add a number of days to the Tzolkin date.
        `addTimedelta`: Add a number of days to the Tzolkin date.
        `getDayDiff`: Return the difference in days until the given Tzolkin date.
        `getDayTimedelta`:Return the difference in days until the given Tzolkin date.
        `getNameNumberFromName`: Return the number of the given Tzolkin day name, between 1 and 20.
        `getTzolkinCalendar`: Return a list of all (260) Tzolkin dates.
    """

    ############################################################################
    def __init__(
        self,
        number: int,
        name_str: Optional[str] = None,
        name_number: Optional[int] = None,
    ) -> None:
        """Generate a Tzolkin date, from the tzolkin day number `number` and the
        Tzolkin day name `name_str` or `name_number`.
        The valid day names for `name_str` are: "Imix", "Ikʼ", "Akʼbʼal", "Kʼan",
        "Chikchan", "Kimi", "Manikʼ", "Lamat", "Muluk", "Ok", "Chuwen", "Ebʼ", "Bʼen",
        "Ix", "Men", "Kʼibʼ", "Kabʼan", "Etzʼnabʼ", "Kawak" and "Ajaw".

        You can also set the Tzolkin day name using the argument `name_number`, which
        takes an integer between 1 and 20 (including 1 and 20).

        If you set both `name_number` and `name_str` to something else than `None`,
        `name_str` takes precedence.

        Raises:
            TzolkinException: if one of the parameters isn't valid.
                                That means, if `number` is not in [1,13], `name_number`
                                is not in [1, 20] or `name_str` is not a valid Tzolkin
                                day name.

        Args:
            number (TzolkinNumber): [description]
            name_str (Optional[TzolkinName], optional): [description]. Defaults to None.
            name_number (Optional[TzolkinNameNumber], optional): [description]. Defaults to None.
        """
        name_num: int = 1
        num_num = number
        if name_str is not None:
            self.__checkNameString(name_str)

            name_num = self.getNameNumberFromName(name_str)

        elif name_number is not None:
            self.__checkNameNumber(name_number)
            name_num = name_number

        self.__checkDayNumber(number)

        self.__tzolkin_date = TzolkinDate(number=num_num, name=name_num)

    ############################################################################
    @classmethod
    def fromDate(cls, date: datetime.date) -> Tzolkin:
        """Create a `Tzolkin` instance from the given gregorian date.

        Args:
            date (datetime.date): The date to convert to a Tzolkin date.

        Returns:
            Tzolkin: The gregorion date `date` converted to a Tzolkin date.
        """
        tzolkin = gregorian2tzolkin(date)

        ret_val = cls(number=tzolkin.number, name_number=tzolkin.name)

        return ret_val

    ############################################################################
    @classmethod
    def fromDateString(cls, date_str: str, fmt: str) -> Tzolkin:
        """Create a `Tzolkin` instance from the given gregorian date string.
        See https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        for a detailed description of date format strings.

        Args:
            date_str (str): The date to convert to a Tzolkin date.
            fmt (str): The format string to parse the given date string. See
            `datetime.datetime.strptime` for a description of date format strings.

        Returns:
            Tzolkin: The gregorion date `date_str` converted to a Tzolkin date.
        """
        date = datetime.datetime.strptime(date_str, fmt).date()
        tzolkin = gregorian2tzolkin(date)

        ret_val = cls(number=tzolkin.number, name_number=tzolkin.name)

        return ret_val

    ############################################################################
    @classmethod
    def fromIsoFormat(cls, date_str: str) -> Tzolkin:
        """Create a `Tzolkin` instance from the given gregorian date string in ISO
        format.
        ISO format means a date in the form 'YYYY-MM-DD', like '2019-03-21'.
        See https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisoformat

        Args:
            date_str (str): See also `datetime.date.fromisoformat`

        Returns:
            Tzolkin: The gregorion date `date_str` converted to a Tzolkin date.
        """
        date = datetime.date.fromisoformat(date_str)
        tzolkin = gregorian2tzolkin(date)

        ret_val = cls(number=tzolkin.number, name_number=tzolkin.name)

        return ret_val

    ############################################################################
    @classmethod
    def fromToday(cls) -> Tzolkin:
        """Return the current date (today) as a Tzolkin date.

        Returns:
            Tzolkin: The current day (today) as a Tzolkin date.
        """
        return cls.fromDate(datetime.date.today())

    ############################################################################
    def getTzolkinDate(self) -> TzolkinDate:
        """Return the Tzolkin date as a `TzolkinDate` instance to use with the
        `tzolkin_calendar.calculate` functions.

        Returns:
            TzolkinDate: The `TzolkinDate` instance of this Tzolkin date.
        """
        return self.__tzolkin_date

    ############################################################################
    def getDayNumber(self) -> int:
        """Return the day number of the Tzolkin date of this class instance.

        Returns:
            int: The day number of this Tzolkin date.
        """
        return self.__tzolkin_date.number

    ############################################################################
    def getDayName(self) -> str:
        """Return the day name of the Tzolkin date of this class instance.

        Returns:
            str: The day name of this Tzolkin date.
        """
        return day_names[self.__tzolkin_date.name]

    ############################################################################
    def getDayNameNumber(self) -> int:
        """Return the number of the Tzolkin day name of this class instance.

        Returns:
            int: The number of the Tzolkin day name of this Tzolkin date.
        """
        return self.__tzolkin_date.name

    ############################################################################
    def getTzolkinYearDay(self) -> int:
        """Return the day of the Tzolkin year of this Tzolkin date.
         1 Imix, the first day in the Tzolkin year, yields 1, 13 Ajaw, the last day of
         the Tzolkin year, yields 260 and so on.

        Returns:
             int: The day of this Tzolkin date in the Tzolkin year, an integer between
                 1 and 260 (including 1 and 260).
        """
        return getTzolkinDay(self.__tzolkin_date)

    ############################################################################
    def getNextDate(
        self, start_date: datetime.date = datetime.date.today()
    ) -> datetime.date:
        """Return the next gregorian date with the Tzolkin date of this Tzolkin instance.
        Next means the first gregorian date with the same Tzolkin date as this `Tzolkin`
        instance after (forward in time) `start_date`.

        Args:
            start_date (datetime.date, optional): The date to start searching for a day
                        with the same Tzolkin date. Defaults to `datetime.date.today()`.

        Returns:
            datetime.date: The gregorian date of the day with the same Tzolkin date as
                            this `Tzolkin` instance after `start_date`.
        """
        return nextTzolkin(tzolkin=self.__tzolkin_date, starting=start_date)

    ############################################################################
    def getNextDateList(
        self, start_date: datetime.date = datetime.date.today(), list_size: int = 50
    ) -> List[datetime.date]:
        """Return a list of dates with the same Tzolkin date as this `Tzolkin` instance
        after `start_date`.
        Searches forwards in time, starting with `start_date`.
        The number of elements in this returned list is set with `list_size`, that is
        the number of dates to search and return.

        Args:
            start_date (datetime.date, optional): The date to start searching for a day
                            with the same Tzolkin date. Defaults to datetime.date.today().
            list_size (int, optional): The number of elements in the returned list of
                                        dates. Defaults to 50.

        Returns:
            List[datetime.date]: The list with `list_size` elements of days with the
                            same Tzolkin date as this instance after `start_date`.
        """
        return tzolkin2gregorian(
            tzolkin=self.__tzolkin_date,
            start=start_date,
            num_results=list_size,
            forward=True,
        )

    ############################################################################
    def getLastDate(
        self, start_date: datetime.date = datetime.date.today()
    ) -> datetime.date:
        """Return the last gregorian date with the Tzolkin date of this Tzolkin instance.
        Last means the first gregorian date with the same Tzolkin date as this `Tzolkin`
        instance before (backwards in time) `start_date`.

        Args:
            start_date (datetime.date, optional):  The date to start searching for a day
                          with the same Tzolkin date. Defaults to datetime.date.today().

        Returns:
            datetime.date: The gregorian date of the day with the same Tzolkin date as
                            this `Tzolkin` instance before `start_date`.
        """
        return lastTzolkin(tzolkin=self.__tzolkin_date, starting=start_date)

    ############################################################################
    def getLastDateList(
        self, start_date: datetime.date = datetime.date.today(), list_size: int = 50
    ) -> List[datetime.date]:
        """Return a list of dates with the same Tzolkin date as this `Tzolkin` instance
        before`start_date`.
        Searches backwards in time, starting with `start_date`.
        The number of elements in this returned list is set with `list_size`, that is
        the number of dates to search and return.

        Args:
            start_date (datetime.date, optional): The date to start searching for a day
                            with the same Tzolkin date. Defaults to datetime.date.today().
            list_size (int, optional): The number of elements in the returned list of
                                        dates. Defaults to 50.

        Returns:
            List[datetime.date]: The list with `list_size` elements of days with the
                            same Tzolkin date as this instance before `start_date`.
        """
        return tzolkin2gregorian(
            tzolkin=self.__tzolkin_date,
            start=start_date,
            num_results=list_size,
            forward=False,
        )

    ############################################################################
    def addDays(self, days: int) -> Tzolkin:
        """Add the number of days to this Tzolkin date and return this instance too.

        Args:
            days (int): The number of days to add (or subtract, if < 0) to this
                        `Tzolkin` instance.

        Returns:
            Tzolkin: This instance with the number of days added (or subtracted) to it.
        """
        added_name = calculateTzolkinName(
            start_name=self.__tzolkin_date.name, to_add=days
        )
        added_number = calculateTzolkinNumber(
            start_number=self.__tzolkin_date.number, to_add=days
        )
        self.__tzolkin_date = TzolkinDate(number=added_number, name=added_name)
        return self

    ############################################################################
    def addTimedelta(self, delta: datetime.timedelta) -> Tzolkin:
        """Add the number of days given in the `datetime.timedelta` object to this
        Tzolkin date.
        Returns this `Tzolkin` instance with the days added to or subtracted from.

        Args:
            delta (datetime.timedelta): The number of days to add (or subtrace, if < 0).

        Returns:
            Tzolkin: This instance with the number of days added or subtracted.
        """
        return self.addDays(days=delta.days)

    ############################################################################
    def getDayDiff(self, other: Tzolkin) -> int:
        """Return the number of days between the two Tzolkin dates.
        No negative differences are returned, but the number of days to reach the
        `other` date if starting from this Tzolkin date.
        If this date is earlier than `other` the difference is
        `this` - `other`. If `other` is before `this`, 260 - `this` + `other`
        (same as 260 - (`other` - `this`)) is returned.

        Args:
            other (Tzolkin): The Tzolkin date to calculate the time difference to.

        Returns:
            int: The number of days between the Tzolkin date of this `Tzolkin` instance
                and the Tzolkin date `other`.
        """
        return getTzolkinDiff(start=self.__tzolkin_date, end=other.__tzolkin_date)

    ############################################################################
    def getDayTimedelta(self, other: Tzolkin) -> datetime.timedelta:
        """Return the number of days between the two Tzolkin dates as a
        `datetime.timedelta` object.
        No negative differences are returned, but the number of days to reach the
        `other` date if starting from this Tzolkin date.
        If this date is earlier than `other` the difference is
        `this` - `other`. If `other` is before `this`, 260 - `this` + `other`
        (same as 260 - (`other` - `this`)) is returned.

        Args:
            other (Tzolkin): The Tzolkin date to calculate the time difference to.

        Returns:
            datetime.timedelta: The number of days between the Tzolkin date of this `Tzolkin` instance
                and the Tzolkin date `other` as a `datetime.timedelta` object.
        """
        days = getTzolkinDiff(start=self.__tzolkin_date, end=other.__tzolkin_date)
        return datetime.timedelta(days=days)

    ############################################################################
    @staticmethod
    def getNameNumberFromName(name_str: str) -> int:
        """Return the day name's number (between 1 and 20) of the Tzolkin day name.
        Imix yields the number 1, Ikʼ 2, ... , Ajaw yields 20.

        Args:
            name_str (TzolkinName): The day name to convert to a number.

        Raises:
            TzolkinException: Raised, if `name_str` is not a valid `TzolkinName`, that
            is, one of "Imix", "Ikʼ", "Akʼbʼal", "Kʼan", "Chikchan", "Kimi", "Manikʼ",
            "Lamat", "Muluk", "Ok", "Chuwen", "Ebʼ", "Bʼen", "Ix", "Men", "Kʼibʼ",
            "Kabʼan", "Etzʼnabʼ", "Kawak" and "Ajaw".

        Returns:
            int: The number of the Tzolkin day name, between 1 and 20 (including 1 and
                20).
        """
        for num, name in day_names.items():
            if name == name_str:
                return num

        raise TzolkinException(
            'string "{name}" is not a valid Tzolkin day name, one of {list}'.format(
                name=name_str, list=day_names.values()
            )
        )

    ############################################################################
    @staticmethod
    def getTzolkinCalendar() -> List[str]:
        """Return all days in a Tzolkin year as a List of strings.
        The returned List looks like: ["1 Imix", "2 Ikʼ", ... , "13 Ajaw"]

        Returns:
            List[str]: All days with day number and name in a list of strings.
        """
        ret_val: List[str] = []
        tzolkin_list = makeLookUpTable()
        for tzolkin_date in tzolkin_list.values():
            ret_val.append(
                "{number} {name}".format(
                    number=tzolkin_date.number, name=tzolkin_date.name
                )
            )

        return ret_val

    ############################################################################
    @staticmethod
    def __checkDayNumber(number: int) -> None:
        """Check, if the given number is a valid Tzolkin day number, that is, between 1
        and 13 (including 1 and 13).

        Args:
            number (TzolkinNumber): The integer to check.

        Raises:
            TzolkinException: If `number` is not in [1, 13] (including 1 and 13)
        """
        if number not in day_numbers.keys():
            raise TzolkinException(
                "number {num} is not a valid Tzolkin day number, not between 1 and 13 (including 1 and 13)".format(
                    num=number
                )
            )

    ############################################################################
    @staticmethod
    def __checkNameNumber(name_number: int) -> None:
        """Check, if the given integer is a valid day name number, that is, between 1
        and 20, including 1 and 20.

        Args:
            name_number (TzolkinNameNumber): The number to check.

        Raises:
            TzolkinException: If `number` is not in [1, 20] (including 1 and 20).
        """
        if name_number not in day_names:
            raise TzolkinException(
                "{number} is not a valid Tzolkin day name number, it must be between 1 and 20 (including 1 and 20)".format(
                    number=name_number
                )
            )

    ############################################################################
    @staticmethod
    def __checkNameString(name_str: TzolkinName) -> None:
        """Check, if the given string is a valid Tzolkin day name.
         The valid day names for `name_str` are: "Imix", "Ikʼ", "Akʼbʼal", "Kʼan",
        "Chikchan", "Kimi", "Manikʼ", "Lamat", "Muluk", "Ok", "Chuwen", "Ebʼ", "Bʼen",
        "Ix", "Men", "Kʼibʼ", "Kabʼan", "Etzʼnabʼ", "Kawak" and "Ajaw".

        Args:
            name_str (TzolkinName): The string to check.

        Raises:
            TzolkinException: If `name_str` is not a valid Tzolkin day name.
        """
        if name_str not in day_names.values():
            raise TzolkinException(
                'string "{name}" is not a valid Tzolkin day name, one of: {list}'.format(
                    name=name_str, list=day_names.values()
                )
            )

    ############################################################################
    def __repr__(self) -> str:
        """Return the string representation of a Tzolkin date.
        Return a string containing day number, day name and the day name'S glyph in
        Unicode - that works as soon as the Maya glyphs are added to the standard.

        Returns:
            str: The string representation of a Tzolkin date.
        """
        return self.__tzolkin_date.__repr__()

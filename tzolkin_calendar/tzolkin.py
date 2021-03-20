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
    getTzolkinDiff,
    gregorian2tzolkin,
    lastTzolkin,
    nextTzolkin,
    tzolkin2gregorian,
)

from . import TzolkinDate, TzolkinException, TzolkinName, day_names, day_numbers


class Tzolkin:
    """[summary]"""

    ############################################################################
    def __init__(
        self,
        number: int,
        name_str: Optional[TzolkinName] = None,
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

            name_num = self.getDayNumber(name_str)

        elif name_number is not None:
            self.__checkNameNumber(name_number)
            name_num = name_number

        self.__checkDayNumber(number)

        self.__tzolkin_date = TzolkinDate(number=num_num, name=name_num)

    ############################################################################
    @classmethod
    def fromDate(cls, date: datetime.date) -> Tzolkin:
        """[summary]

        Args:
            date (datetime.date): [description]

        Returns:
            Tzolkin: [description]
        """
        tzolkin = gregorian2tzolkin(date)

        ret_val = cls(number=tzolkin.number, name_number=tzolkin.name)

        return ret_val

    ############################################################################
    @classmethod
    def fromDateString(cls, date_str: str, fmt: str) -> Tzolkin:
        """[summary]

        Args:
            date_str (str): [description]
            fmt (str): [description]

        Returns:
            Tzolkin: [description]
        """
        date = datetime.datetime.strptime(date_string=date_str, format=fmt).date()
        tzolkin = gregorian2tzolkin(date)

        ret_val = cls(number=tzolkin.number, name_number=tzolkin.name)

        return ret_val

    ############################################################################
    @classmethod
    def fromIsoFormat(cls, date_str: str) -> Tzolkin:
        """[summary]

        Args:
            date_str (str): [description]

        Returns:
            Tzolkin: [description]
        """
        date = datetime.date.fromisoformat(date_str)
        tzolkin = gregorian2tzolkin(date)

        ret_val = cls(number=tzolkin.number, name_number=tzolkin.name)

        return ret_val

    ############################################################################
    def getNextDate(
        self, start_date: datetime.date = datetime.date.today()
    ) -> datetime.date:
        """[summary]

        Args:
            start_date (datetime.date, optional): [description]. Defaults to datetime.date.today().

        Returns:
            datetime.date: [description]
        """
        return nextTzolkin(tzolkin=self.__tzolkin_date, starting=start_date)

    ############################################################################
    def getNextDateList(
        self, start_date: datetime.date = datetime.date.today(), list_size: int = 50
    ) -> List[datetime.date]:
        """[summary]

        Args:
            start_date (datetime.date, optional): [description]. Defaults to datetime.date.today().
            list_size (int, optional): [description]. Defaults to 50.

        Returns:
            List[datetime.date]: [description]
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
        """[summary]

        Args:
            start_date (datetime.date, optional): [description]. Defaults to datetime.date.today().

        Returns:
            datetime.date: [description]
        """
        return lastTzolkin(tzolkin=self.__tzolkin_date, starting=start_date)

    ############################################################################
    def getLastDateList(
        self, start_date: datetime.date = datetime.date.today(), list_size: int = 50
    ) -> List[datetime.date]:
        """[summary]

        Args:
            start_date (datetime.date, optional): [description]. Defaults to datetime.date.today().
            list_size (int, optional): [description]. Defaults to 50.

        Returns:
            List[datetime.date]: [description]
        """
        return tzolkin2gregorian(
            tzolkin=self.__tzolkin_date,
            start=start_date,
            num_results=list_size,
            forward=False,
        )

    ############################################################################
    def addDays(self, days: int) -> Tzolkin:
        """[summary]

        Args:
            days (int): [description]

        Returns:
            Tzolkin: [description]
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
        """[summary]

        Args:
            delta (datetime.timedelta): [description]

        Returns:
            Tzolkin: [description]
        """
        return self.addDays(days=delta.days)

    ############################################################################
    def getDayDiff(self, other: Tzolkin) -> int:
        """[summary]

        Args:
            other (Tzolkin): [description]

        Returns:
            int: [description]
        """
        return getTzolkinDiff(start=self.__tzolkin_date, end=other.__tzolkin_date)

    ############################################################################
    def getDayTimedelta(self, other: Tzolkin) -> datetime.timedelta:
        """[summary]

        Args:
            other (Tzolkin): [description]

        Returns:
            datetime.timedelta: [description]
        """
        days = getTzolkinDiff(start=self.__tzolkin_date, end=other.__tzolkin_date)
        return datetime.timedelta(days=days)

    ############################################################################
    @staticmethod
    def getDayNumber(name_str: TzolkinName) -> int:
        """[summary]

        Args:
            name_str (TzolkinName): [description]

        Raises:
            TzolkinException: [description]

        Returns:
            int: [description]
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
    def __checkDayNumber(number: int) -> None:
        """[summary]

        Args:
            number (TzolkinNumber): [description]

        Raises:
            TzolkinException: [description]
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
        """[summary]

        Args:
            name_number (TzolkinNameNumber): [description]

        Raises:
            TzolkinException: [description]
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
        """[summary]

        Args:
            name_str (TzolkinName): [description]

        Raises:
            TzolkinException: [description]
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

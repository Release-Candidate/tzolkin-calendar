Tzolk’in Command Line Client
============================

You can try the command line client in an interactive Jupyter Notebook at MyBinder:
`tzolkin_calendar Command Line Client <https://mybinder.org/v2/gh/Release-Candidate/tzolkin-calendar/main?filepath=Tzolk%E2%80%99in%20Command%20Line.ipynb>`_

We start the command line client of ``tzolkin-calendar`` using
``python -m``: beware of the underscore (``_``)

.. code:: shell

    % python -m tzolkin_calendar


.. parsed-literal::

    Gregorian "24.03.2021" is "3 Men" as Tzolk’in


As default, if no argument is given, the Tzolk’in date of the current
day (‘today’ ins the 24th of March, 2021) is printed.

To get the version of ``tzolkin_calendar``, use the argument
``--version``

.. code:: shell

    % python -m tzolkin_calendar --version


.. parsed-literal::

    tzolkin-calendar 0.9.3


The argument ``--help`` displays a short usage text, we go through all
options in the follwing parts.

.. code:: shell

    % python -m tzolkin_calendar --help


.. parsed-literal::

    usage: python -m tzolkin_calendar [-h] [--version] [-l LIST_LENGTH]
                                      [-s START_DATE] [-y]
                                      [DATE ...]
    
    A Tzolk’in date converter and calculator.
    
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
        python -m tzolkin_calendar 16-04-2016
        python -m tzolkin_calendar 16 04 2016
        python -m tzolkin_calendar 2016.04.16
        python -m tzolkin_calendar 2016-04-16
        python -m tzolkin_calendar 2016/04/16
        python -m tzolkin_calendar 2016 04 16
        python -m tzolkin_calendar 04/16/2016
    
    positional arguments:
      DATE                  The date to parse and convert. Either a Tzolk’in date or a gregorian date can be given. The default is the date of today.
    
    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      -l LIST_LENGTH, --list LIST_LENGTH
                            Display a list of dates with the given Tzolk’in date instead of a single one. The length of the list is LIST_LENGTH.
      -s START_DATE, --start START_DATE
                            The start date to begin the search for the dates with the same Tzolk’in date. The same formatting rules apply as for the main argument DATE.
      -y, --year            Print all dates of a Tzolk’in year.
    
    See website https://github.com/Release-Candidate/tzolkin_calendar for a detailed description.


Converting Gregorian Dates to Tzolk’in Dates
--------------------------------------------

To get the Tzolk’in date of a Gregorian date use the Gregorian date as
the main argument to ``tzolkin_calendar``.

E.g. to get the Tzolk’in date of the 18th of May, 1974, which is “12
Akʼbʼal”

.. code:: shell

    % python -m tzolkin_calendar 18.05.1974


.. parsed-literal::

    Gregorian "18.05.1974" is "12 Akʼbʼal" as Tzolk’in


| Many date format conventions are supported, any of these work (and
  result in the 18th of May, 1974):
| DD.MM.YYYY - 18.05.1974
| DD-MM-YYYY - 18-05-1974
| DD MM YYYY - 18 05 1974
| YYYY.MM.DD - 1974.05.18
| YYYY-MM-DD - 1974-05-18
| YYYY/MM/DD - 1974/05/18
| YYYY MM DD - 1974 05 18
| MM/DD/YYYY - 05/18/1974

.. code:: shell

    % python -m tzolkin_calendar 05/18/1974


.. parsed-literal::

    Gregorian "05/18/1974" is "12 Akʼbʼal" as Tzolk’in


Searching Tzolk’in Dates
------------------------

To search for Gregorian Dates to a given Tzolk’in date, input the
Tzolk’in date to search for.

As default the search is started today (the 24th of March, 2021). So, we
search for “13 Lamat”

.. code:: shell

    % python -m tzolkin_calendar 13 Lamat


.. parsed-literal::

    Tzolk’in date "13 Lamat" next date is "24.08.2021", last date has been "07.12.2020"


The next gregorian date with a Tzolk’in date of “12 Lamat” after today
(the 24th of March 2021) is the 24th od August, 2021, the last gregorian
date before today has been the 7th of December 2020.

| We again can use many formats to pass as Tzolk’in dates: DD NNNN - 13
  Lamat
| DD/NNNN - 13/Lamat
| DD.NNNN - 13.Lamat
| DD-NNNN - 13-Lamat

Instead of the name, we can also use the number of the day name (between
1 and 20), so instead of “Lamat” we could use the number 8. The valid
formats are again (with or without leading zeroes). DD NN - 13 8 DD/NN -
13/8 DD.NN - 13.8 DD-NN - 13-8

We can also search starting at other days than today, so lets start the
search at the 18th of May 1974, this is the argument to ``--start``

.. code:: shell

    % python -m tzolkin_calendar 13 Lamat --start 18.05.1974


.. parsed-literal::

    Tzolk’in date "13 Lamat" next date is "31.08.1974", last date has been "14.12.1973"


Now the search returned the 31th of August, 1974 as the next and the
14th of December 1974 as the last Gregorian date with the same Tzolk’in
date.

We can also search for more than one date in the future and the past, by
using the argument ``--list``, which is the number of Gregorian dates to
return. Lets search for 5 Gregorian dates with a Tzolk’in date of “13
Lamat”, starting at the 18th of May, 1974.

.. code:: shell

    % python -m tzolkin_calendar 13 Lamat --start 18.05.1974 --list 5


.. parsed-literal::

    Tzolk’in date "13 Lamat"
     next dates are ['31.08.1974', '18.05.1975', '02.02.1976', '19.10.1976', '06.07.1977']
     last dates have been ['14.12.1973', '29.03.1973', '12.07.1972', '26.10.1971', '08.02.1971']


So we’re getting 5 Gregorian dates after and before the 18th of May,
1974.

Without an ``--start`` argument, we start the search today (the 24th of
March, 2021).

.. code:: shell

    % python -m tzolkin_calendar 13 Lamat --list 5


.. parsed-literal::

    Tzolk’in date "13 Lamat"
     next dates are ['24.08.2021', '11.05.2022', '26.01.2023', '13.10.2023', '29.06.2024']
     last dates have been ['07.12.2020', '22.03.2020', '06.07.2019', '19.10.2018', '01.02.2018']


We can make the list as long as we want, but if the list would be too
long, we ran out of the valid calendar days.

.. code:: shell

    % python -m tzolkin_calendar 13 Lamat --list 10000


.. parsed-literal::

    Traceback (most recent call last):
     ...
      File "./tzolkin_calendar/calculate.py", line 432, in lastTzolkin
        return starting + day_diff_delta
    OverflowError: date value out of range


Print all Tzolk’in Dates in a Tzolk’in Year
-------------------------------------------

To get a list of all 260 Tzolk’in dates in a Tzolk’in year, we use the
argument ``--year``:

.. code:: shell

    % python -m tzolkin_calendar --year


.. parsed-literal::

     1 Imix 2 Ikʼ 3 Akʼbʼal 4 Kʼan 5 Chikchan 6 Kimi 7 Manikʼ 8 Lamat 9 Muluk 10 Ok 11 Chuwen 12 Ebʼ 13 Bʼen
     1 Ix 2 Men 3 Kʼibʼ 4 Kabʼan 5 Etzʼnabʼ 6 Kawak 7 Ajaw 8 Imix 9 Ikʼ 10 Akʼbʼal 11 Kʼan 12 Chikchan 13 Kimi
     1 Manikʼ 2 Lamat 3 Muluk 4 Ok 5 Chuwen 6 Ebʼ 7 Bʼen 8 Ix 9 Men 10 Kʼibʼ 11 Kabʼan 12 Etzʼnabʼ 13 Kawak
     1 Ajaw 2 Imix 3 Ikʼ 4 Akʼbʼal 5 Kʼan 6 Chikchan 7 Kimi 8 Manikʼ 9 Lamat 10 Muluk 11 Ok 12 Chuwen 13 Ebʼ
     1 Bʼen 2 Ix 3 Men 4 Kʼibʼ 5 Kabʼan 6 Etzʼnabʼ 7 Kawak 8 Ajaw 9 Imix 10 Ikʼ 11 Akʼbʼal 12 Kʼan 13 Chikchan
     1 Kimi 2 Manikʼ 3 Lamat 4 Muluk 5 Ok 6 Chuwen 7 Ebʼ 8 Bʼen 9 Ix 10 Men 11 Kʼibʼ 12 Kabʼan 13 Etzʼnabʼ
     1 Kawak 2 Ajaw 3 Imix 4 Ikʼ 5 Akʼbʼal 6 Kʼan 7 Chikchan 8 Kimi 9 Manikʼ 10 Lamat 11 Muluk 12 Ok 13 Chuwen
     1 Ebʼ 2 Bʼen 3 Ix 4 Men 5 Kʼibʼ 6 Kabʼan 7 Etzʼnabʼ 8 Kawak 9 Ajaw 10 Imix 11 Ikʼ 12 Akʼbʼal 13 Kʼan
     1 Chikchan 2 Kimi 3 Manikʼ 4 Lamat 5 Muluk 6 Ok 7 Chuwen 8 Ebʼ 9 Bʼen 10 Ix 11 Men 12 Kʼibʼ 13 Kabʼan
     1 Etzʼnabʼ 2 Kawak 3 Ajaw 4 Imix 5 Ikʼ 6 Akʼbʼal 7 Kʼan 8 Chikchan 9 Kimi 10 Manikʼ 11 Lamat 12 Muluk 13 Ok
     1 Chuwen 2 Ebʼ 3 Bʼen 4 Ix 5 Men 6 Kʼibʼ 7 Kabʼan 8 Etzʼnabʼ 9 Kawak 10 Ajaw 11 Imix 12 Ikʼ 13 Akʼbʼal
     1 Kʼan 2 Chikchan 3 Kimi 4 Manikʼ 5 Lamat 6 Muluk 7 Ok 8 Chuwen 9 Ebʼ 10 Bʼen 11 Ix 12 Men 13 Kʼibʼ
     1 Kabʼan 2 Etzʼnabʼ 3 Kawak 4 Ajaw 5 Imix 6 Ikʼ 7 Akʼbʼal 8 Kʼan 9 Chikchan 10 Kimi 11 Manikʼ 12 Lamat 13 Muluk
     1 Ok 2 Chuwen 3 Ebʼ 4 Bʼen 5 Ix 6 Men 7 Kʼibʼ 8 Kabʼan 9 Etzʼnabʼ 10 Kawak 11 Ajaw 12 Imix 13 Ikʼ
     1 Akʼbʼal 2 Kʼan 3 Chikchan 4 Kimi 5 Manikʼ 6 Lamat 7 Muluk 8 Ok 9 Chuwen 10 Ebʼ 11 Bʼen 12 Ix 13 Men
     1 Kʼibʼ 2 Kabʼan 3 Etzʼnabʼ 4 Kawak 5 Ajaw 6 Imix 7 Ikʼ 8 Akʼbʼal 9 Kʼan 10 Chikchan 11 Kimi 12 Manikʼ 13 Lamat
     1 Muluk 2 Ok 3 Chuwen 4 Ebʼ 5 Bʼen 6 Ix 7 Men 8 Kʼibʼ 9 Kabʼan 10 Etzʼnabʼ 11 Kawak 12 Ajaw 13 Imix
     1 Ikʼ 2 Akʼbʼal 3 Kʼan 4 Chikchan 5 Kimi 6 Manikʼ 7 Lamat 8 Muluk 9 Ok 10 Chuwen 11 Ebʼ 12 Bʼen 13 Ix
     1 Men 2 Kʼibʼ 3 Kabʼan 4 Etzʼnabʼ 5 Kawak 6 Ajaw 7 Imix 8 Ikʼ 9 Akʼbʼal 10 Kʼan 11 Chikchan 12 Kimi 13 Manikʼ
     1 Lamat 2 Muluk 3 Ok 4 Chuwen 5 Ebʼ 6 Bʼen 7 Ix 8 Men 9 Kʼibʼ 10 Kabʼan 11 Etzʼnabʼ 12 Kawak 13 Ajaw
    Gregorian "24.03.2021" is "3 Men" as Tzolk’in

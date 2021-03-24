Usage of tzolkin-calendar in Your Python Code
=============================================

You can try the tzolkin_calendar package interactively using the online Jupyter Notebook at MyBinder:
`tzolkin_calendar module <https://mybinder.org/v2/gh/Release-Candidate/tzolkin-calendar/main?filepath=Tzolk%E2%80%99in%20Calender%20Python%20Module.ipynb>`_


Import the Module
-----------------

To use the Tzolk’in date package, import ``tzolkin_calender`` (with an
underscore ``_``).

A short check to see if it is working, is to print the version of
``tzolkin-calendar``, that’s the constant ``tzolkin_calendar.VERSION``.

.. code:: python

    # Import the package.
    import tzolkin_calendar
    
    # Check, if it is working.
    tzolkin_calendar.VERSION




.. parsed-literal::

    '0.9.3'



The Tzolk’in Date Class ``Tzolkin``
-----------------------------------

The Tzolk’in date class resides in the module
``tzolkin_calendar.tzolkin``, and is named ``Tzolkin``.

So, import that module:

.. code:: python

    # Import the module tzolkin that contains `Tzolkin`.
    from tzolkin_calendar import tzolkin

Convert Gregorian Dates to Tzolk’in Dates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get the Tzolk’in date of today, call the static method ``fromToday``.
This returns a ``Tzolkin`` instance holding the Tzolk’in date of today
(‘today’ is the 22nd of March, 2021, with a Tzolk’in date of ‘1 Bʼen’)

.. code:: python

    tzolkin.Tzolkin.fromToday()




.. parsed-literal::

    '3 Men'



You can generate a ``Tzolkin`` instance from any gregorian date using
the ``datetime.date`` class or a date string.

So, first import the datetime module:

.. code:: python

    import datetime

And then use the 3 possibilities to set the Tzolk’in date from a
gregorian date. Or, in other words, to convert a gregorian date to a
Tzolk’in date.

1. from a datetime.date instance using ``Tzolkin.fromDate``. We use the
   method ``fromisoformat`` to set the gregorian date to the 22nd of
   March 2021 with the date string ‘2021-03-22’. The Tzolk’in date of
   the 22nd of March 2021 is ‘1 Bʼen’.

.. code:: python

    gregorian_date = datetime.date.fromisoformat("2021-03-22")
    
    tzolkin.Tzolkin.fromDate(gregorian_date)




.. parsed-literal::

    '1 Bʼen'



2. from an ISO date string using ``Tzolkin.fromIsoFormat``. We set the
   Tzolk’in date to the 22nd of March 2021 with the ISO date string
   ‘2021-03-22’. The Tzolk’in date of the 22nd of March 2021 is ‘1
   Bʼen’.

.. code:: python

    tzolkin.Tzolkin.fromIsoFormat("2021-03-22")




.. parsed-literal::

    '1 Bʼen'



3. from an arbitrary date string using ``Tzolkin.fromDateString``. We
   set the Tzolk’in date to the 22nd of March 2021 with the date string
   ‘22=03*2021’ and the format string ``fmt`` ’%d=%m*%Y’. The Tzolk’in
   date of the 22nd of March 2021 is ‘1 Bʼen’.

.. code:: python

    tzolkin.Tzolkin.fromDateString("22=03*2021", fmt="%d=%m*%Y")




.. parsed-literal::

    '1 Bʼen'



Set Tzolk’in Dates
~~~~~~~~~~~~~~~~~~

You can set the ``Tzolkin`` instance to a Tzolk’in Date using it’s
constructor. The constructor takes the Tzolk’in day number (between 1
and 13 including 1 and 13) and either a Tzolk’in day name or the number
of the Tzolk’in day name (between 1 and 20 , including 1 and 20).

To get a dictionary of Tzolk’in day names and numbers, look at
``tzolkin.day_names``.

.. code:: python

    tzolkin.day_names




.. parsed-literal::

    {1: 'Imix', 2: 'Ikʼ', 3: 'Akʼbʼal', 4: 'Kʼan', 5: 'Chikchan', 6: 'Kimi', 7: 'Manikʼ',
     8: 'Lamat', 9: 'Muluk', 10: 'Ok', 11: 'Chuwen', 12: 'Ebʼ', 13: 'Bʼen', 14: 'Ix',
     15: 'Men', 16: 'Kʼibʼ', 17: 'Kabʼan', 18: 'Etzʼnabʼ', 19: 'Kawak', 20: 'Ajaw'}



If we want to set a Tzolk’in day of ‘8 Kabʼan’, we can either pass the
day number 8 and day name Kabʼan to the constructor, or the day number 8
and the day name number 17.

.. code:: python

    tzolkin.Tzolkin(number=8, name_str="Kabʼan")




.. parsed-literal::

    '8 Kabʼan'



.. code:: python

    tzolkin.Tzolkin(number=8, name_number=17)




.. parsed-literal::

    '8 Kabʼan'



If we pass an invalid number (not in [1, 13]) or name to the
constructor, we get a ``TzolkinException``.

.. code:: python

   tzolkin.Tzolkin(number=53, name_number=17)

       TzolkinException: number 53 is not a valid Tzolkin day number, not between 1 and 13 (including 1 and 13)

   tzolkin.Tzolkin(number=3, name_str="Hugo")

       TzolkinException: string "Hugo" is not a valid Tzolkin day name, one of: dict_values(['Imix', 'Ikʼ', 'Akʼbʼal', 'Kʼan', 'Chikchan', 'Kimi', 'Manikʼ', 'Lamat', 'Muluk', 'Ok', 'Chuwen', 'Ebʼ', 'Bʼen', 'Ix', 'Men', 'Kʼibʼ', 'Kabʼan', 'Etzʼnabʼ', 'Kawak', 'Ajaw'])
             
   tzolkin.Tzolkin(number=3, name_number=-5)

       TzolkinException: -5 is not a valid Tzolkin day name number, it must be between 1 and 20 (including 1 and 20)

These Tzolk’in day numbers and names can be accessed using the methods
``getDayNumber``, ``getDayName`` and ``getDayNameNumber``.

.. code:: python

    # Set the Tzolk’in date to '12 Kimi'.
    tzolkin_date = tzolkin.Tzolkin(number=12, name_str="Kimi")
    
    tzolkin_date.getDayNumber()




.. parsed-literal::

    12



.. code:: python

    tzolkin_date.getDayName()




.. parsed-literal::

    'Kimi'



.. code:: python

    tzolkin_date.getDayNameNumber()




.. parsed-literal::

    6



To get the number of Tzolk’in day in the Tzolk’in year of 260 days,
there is ``getTzolkinYearDay``. For example ‘12 Kimi’ is the 246. day
(of 260 days) of the Tzolk’in year

.. code:: python

    tzolkin_date.getTzolkinYearDay()




.. parsed-literal::

    246



To parse a Tzolk’in day name that isn't exactly like the ones in ``tzolkin.day_names``
there is the method ``Tzolkin.parseTzolkinName``, that ignores upper- and lowercase and
all non-alphanumeric and non-ascii characters.

.. code:: python

    day_number = tzolkin.Tzolkin.parseTzolkinName("EtZ`nAB")
    if day_number != 0:
        tzolkin_name = tzolkin_calendar.day_names[day_number]
    tzolkin_name




.. parsed-literal::

    'Etzʼnabʼ'



All 260 Tzolk’in days of a Tzolk’in year we can get as a list of strings
from the static method ``getTzolkinCalendar``.

.. code:: python

    tzolkin.Tzolkin.getTzolkinCalendar()




.. parsed-literal::

    ['1 Imix', '2 Ikʼ', '3 Akʼbʼal', '4 Kʼan', '5 Chikchan', '6 Kimi', '7 Manikʼ', '8 Lamat', '9 Muluk', '10 Ok', '11 Chuwen', '12 Ebʼ', '13 Bʼen',
     '1 Ix', '2 Men', '3 Kʼibʼ', '4 Kabʼan', '5 Etzʼnabʼ', '6 Kawak', '7 Ajaw', '8 Imix', '9 Ikʼ', '10 Akʼbʼal', '11 Kʼan', '12 Chikchan', '13 Kimi',
     '1 Manikʼ', '2 Lamat', '3 Muluk', '4 Ok', '5 Chuwen', '6 Ebʼ', '7 Bʼen', '8 Ix', '9 Men', '10 Kʼibʼ', '11 Kabʼan', '12 Etzʼnabʼ', '13 Kawak',
     '1 Ajaw', '2 Imix', '3 Ikʼ', '4 Akʼbʼal', '5 Kʼan', '6 Chikchan', '7 Kimi', '8 Manikʼ', '9 Lamat', '10 Muluk', '11 Ok', '12 Chuwen', '13 Ebʼ',
     '1 Bʼen', '2 Ix', '3 Men', '4 Kʼibʼ', '5 Kabʼan', '6 Etzʼnabʼ', '7 Kawak', '8 Ajaw', '9 Imix', '10 Ikʼ', '11 Akʼbʼal', '12 Kʼan', '13 Chikchan',
     '1 Kimi', '2 Manikʼ', '3 Lamat', '4 Muluk', '5 Ok', '6 Chuwen', '7 Ebʼ', '8 Bʼen', '9 Ix', '10 Men', '11 Kʼibʼ', '12 Kabʼan', '13 Etzʼnabʼ',
     '1 Kawak', '2 Ajaw', '3 Imix', '4 Ikʼ', '5 Akʼbʼal', '6 Kʼan', '7 Chikchan', '8 Kimi', '9 Manikʼ', '10 Lamat', '11 Muluk', '12 Ok', '13 Chuwen',
     '1 Ebʼ', '2 Bʼen', '3 Ix', '4 Men', '5 Kʼibʼ', '6 Kabʼan', '7 Etzʼnabʼ', '8 Kawak', '9 Ajaw', '10 Imix', '11 Ikʼ', '12 Akʼbʼal', '13 Kʼan',
     '1 Chikchan', '2 Kimi', '3 Manikʼ', '4 Lamat', '5 Muluk', '6 Ok', '7 Chuwen', '8 Ebʼ', '9 Bʼen', '10 Ix', '11 Men', '12 Kʼibʼ', '13 Kabʼan',
     '1 Etzʼnabʼ', '2 Kawak', '3 Ajaw', '4 Imix', '5 Ikʼ', '6 Akʼbʼal', '7 Kʼan', '8 Chikchan', '9 Kimi', '10 Manikʼ', '11 Lamat', '12 Muluk', '13 Ok',
     '1 Chuwen', '2 Ebʼ', '3 Bʼen', '4 Ix', '5 Men', '6 Kʼibʼ', '7 Kabʼan', '8 Etzʼnabʼ', '9 Kawak', '10 Ajaw', '11 Imix', '12 Ikʼ', '13 Akʼbʼal',
     '1 Kʼan', '2 Chikchan', '3 Kimi', '4 Manikʼ', '5 Lamat', '6 Muluk', '7 Ok', '8 Chuwen', '9 Ebʼ', '10 Bʼen', '11 Ix', '12 Men', '13 Kʼibʼ',
     '1 Kabʼan', '2 Etzʼnabʼ', '3 Kawak', '4 Ajaw', '5 Imix', '6 Ikʼ', '7 Akʼbʼal', '8 Kʼan', '9 Chikchan', '10 Kimi', '11 Manikʼ', '12 Lamat', '13 Muluk',
     '1 Ok', '2 Chuwen', '3 Ebʼ', '4 Bʼen', '5 Ix', '6 Men', '7 Kʼibʼ', '8 Kabʼan', '9 Etzʼnabʼ', '10 Kawak', '11 Ajaw', '12 Imix', '13 Ikʼ',
     '1 Akʼbʼal', '2 Kʼan', '3 Chikchan', '4 Kimi', '5 Manikʼ', '6 Lamat', '7 Muluk', '8 Ok', '9 Chuwen', '10 Ebʼ', '11 Bʼen', '12 Ix', '13 Men',
     '1 Kʼibʼ', '2 Kabʼan', '3 Etzʼnabʼ', '4 Kawak', '5 Ajaw', '6 Imix', '7 Ikʼ', '8 Akʼbʼal', '9 Kʼan', '10 Chikchan', '11 Kimi', '12 Manikʼ', '13 Lamat',
     '1 Muluk', '2 Ok', '3 Chuwen', '4 Ebʼ', '5 Bʼen', '6 Ix', '7 Men', '8 Kʼibʼ', '9 Kabʼan', '10 Etzʼnabʼ', '11 Kawak', '12 Ajaw', '13 Imix',
     '1 Ikʼ', '2 Akʼbʼal', '3 Kʼan', '4 Chikchan', '5 Kimi', '6 Manikʼ', '7 Lamat', '8 Muluk', '9 Ok', '10 Chuwen', '11 Ebʼ', '12 Bʼen', '13 Ix',
     '1 Men', '2 Kʼibʼ', '3 Kabʼan', '4 Etzʼnabʼ', '5 Kawak', '6 Ajaw', '7 Imix', '8 Ikʼ', '9 Akʼbʼal', '10 Kʼan', '11 Chikchan', '12 Kimi', '13 Manikʼ',
     '1 Lamat', '2 Muluk', '3 Ok', '4 Chuwen', '5 Ebʼ', '6 Bʼen', '7 Ix', '8 Men', '9 Kʼibʼ', '10 Kabʼan', '11 Etzʼnabʼ', '12 Kawak', '13 Ajaw']


Search Gregorian Dates to a given Tzolk’in Date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can search for the next (forward in time) or last (backwards in time)
day with the same Tzolk’in date using the methods ``getNextDate`` and
``getLastDate``. Both methods return a ``datetime.date`` object.

When searching for the next gregorian date that has the Tzolk’in date ‘7
Kawak’, we get the 28th of March, 2021 - because we started searching
‘today’, which is the 22nd of March 2021.

.. code:: python

    # Set the Tzolk’in date to search for to '7 Kawak'.
    tzolkin_date = tzolkin.Tzolkin(number=7, name_str="Kawak")
    
    tzolkin_date.getNextDate()




.. parsed-literal::

    datetime.date(2021, 3, 28)



When searching for the last gregorian date that has the Tzolk’in date ‘7
Kawak’, we get the 11th of July, 2020 - because we started searching
‘today’, which is the 22nd of March 2021.

.. code:: python

    tzolkin_date.getLastDate()




.. parsed-literal::

    datetime.date(2020, 7, 11)



Both methods, ``getNextDate`` and ``getLastDate`` take an optional
argument ``start_date``, which is the gregorian date to start the
search. If no ``start_date`` is given, ‘today’ is used as the start
date.

So now we search again for ‘7 Kawak’ in both directions, but this time
we start at the 10th of July, 2020.

.. code:: python

    # Set the Tzolk’in date to search for to '7 Kawak'.
    tzolkin_date = tzolkin.Tzolkin(number=7, name_str="Kawak")
    
    # Set the start date of the search to the 10th of July, 2020.
    start_search = datetime.date.fromisoformat("2020-07-10")
    
    start_search.isoformat()




.. parsed-literal::

    '2020-07-10'



For the next day with a Tzolk’in date of ‘7 Kawak’ we now get the 11th
of July, 2020.

.. code:: python

    tzolkin_date.getNextDate(start_date=start_search)




.. parsed-literal::

    datetime.date(2020, 7, 11)



For the last day before our start date with a Tzolk’in date of ‘7 Kawak’
we now get the 25th of October, 2019.

.. code:: python

    tzolkin_date.getLastDate(start_date=start_search)




.. parsed-literal::

    datetime.date(2019, 10, 25)



To get a list of ``datetime.date`` dates with the same Tzolk’in date, we
can use the methods ``getNextDateList`` and ``getLastDateList``.

Again, we can set the argument ``start_date`` to a gregorian date to
start the search or not set it to start the search today. The number of
elements in the returned list is set using the parameter ``list_size``,
which defaults to 50.

.. code:: python

    # Set the Tzolk’in date to search for to '7 Kawak'.
    tzolkin_date = tzolkin.Tzolkin(number=7, name_str="Kawak")

Let’s start the search for dates with a Tzolk’in date of ’ 7 Kawak’
today, the 22nd of March 2021, and set the list size to 9 elements:

.. code:: python

    tzolkin_date.getNextDateList(list_size=9)




.. parsed-literal::

    [datetime.date(2021, 3, 28),
     datetime.date(2021, 12, 13),
     datetime.date(2022, 8, 30),
     datetime.date(2023, 5, 17),
     datetime.date(2024, 2, 1),
     datetime.date(2024, 10, 18),
     datetime.date(2025, 7, 5),
     datetime.date(2026, 3, 22),
     datetime.date(2026, 12, 7)]



Now start searching for ‘7 Kawak’ on the 29th of March, 2021 and set the
returned list size to 5.

.. code:: python

    # Set the start date of the search to the 29th of March, 2021.
    start_search = datetime.date.fromisoformat("2021-03-29")
    
    tzolkin_date.getLastDateList(start_date=start_search, list_size=5)




.. parsed-literal::

    [datetime.date(2021, 3, 28),
     datetime.date(2020, 7, 11),
     datetime.date(2019, 10, 25),
     datetime.date(2019, 2, 7),
     datetime.date(2018, 5, 23)]



Calculations using Tzolk’in Dates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are 4 methods to get the difference in days between two Tzolk’in
dates and to add (or subtract) days from a Tzolk’in date: ``addDays``,
``addTimedelta``, ``getDayDiff`` and ``getDayTimedelta``.

Lets start with a Tzolk’in date of ‘6 Muluk’.

.. code:: python

    tzolkin.Tzolkin(number=6, name_str="Muluk")




.. parsed-literal::

    '6 Muluk'



Add 6 days to it, and we get a Tzolk’in date of ‘12 Men’.

.. code:: python

    tzolkin.Tzolkin(number=6, name_str="Muluk").addDays(6)




.. parsed-literal::

    '12 Men'



Instead of using ints, we can also add and subtract
``datetime.timedelta`` objects. Now subtract 6 days from ‘12 Men’ - we
get ‘6 Muluk’.

.. code:: python

    to_subtract = datetime.timedelta(days=-6)
    
    tzolkin.Tzolkin(number=12, name_str="Men").addTimedelta(to_subtract)




.. parsed-literal::

    '6 Muluk'



To get the difference between two Tzolk’in dates there exist the Methods
``getDayDiff`` and ``getDayTimedelta``.

Lets calculate the difference in days between ‘6 Muluk’ and ‘12 Men’.

.. code:: python

    # Set start_tzolkin to '6 Muluk'.
    start_tzolkin = tzolkin.Tzolkin(number=6, name_str="Muluk")
    
    # Set end_tzolkin to '12 Men'.
    end_tzolkin = tzolkin.Tzolkin(number=12, name_str="Men")
    
    start_tzolkin.getDayDiff(end_tzolkin)




.. parsed-literal::

    6



And using ``getDayTimedelta``, which returns a ``datetime.timedelta``
object.

.. code:: python

    start_tzolkin.getDayTimedelta(end_tzolkin)




.. parsed-literal::

    datetime.timedelta(days=6)



What happens, if we calculate the difference between ‘12 Men’ and ‘6
Muluk’?

.. code:: python

    end_tzolkin.getDayDiff(start_tzolkin)




.. parsed-literal::

    254



We get 254 days, not -6. That’s because the difference is always
calculated forward in time. If you want to get negative days or the
shortest possible time difference, subtract 260 from the the result (the
number of days in a Tzolk’in year). As soon as the difference in days is
greater than 130, to minimum time distance in days ‘is negative’.

.. code:: python

    day_diff = end_tzolkin.getDayDiff(start_tzolkin)
    
    if day_diff > 130:
        day_diff = 260 - day_diff
    day_diff




.. parsed-literal::

    6



Or you can use the minimum of ``result`` and ``|result - 260|`` that is
``abs(result - 260)``.

.. code:: python

    day_diff = end_tzolkin.getDayDiff(start_tzolkin)
    shortest_diff = min(day_diff, abs(day_diff - 260))
    shortest_diff




.. parsed-literal::

    6

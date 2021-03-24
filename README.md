# tzolkin-calendar - Converter for Maya Tzolk’in Dates

This program converts mayan Tzolk’in dates to gregorian dates and vice versa.
If you want to know more about the maya calendar systems, see [Links](#links).

Information about the installation and usage you find at [Installation and Usage](#installation-and-usage)

More detailed Documentation can be found at [Read the Docs](https://tzolkin-calendar.readthedocs.io/en/latest/)

[![Binder tzolkin-calendar Notebook](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Release-Candidate/tzolkin-calendar/main?filepath=Tzolk%E2%80%99in%20Calendar.ipynb)
[![MIT license badge](https://img.shields.io/github/license/Release-Candidate/tzolkin-calendar)](https://github.com/Release-Candidate/tzolkin-calendar/blob/main/LICENSE)
[![Python version badge](https://img.shields.io/pypi/pyversions/buildnis)](https://www.python.org/downloads/)
[![PIP version badge](https://img.shields.io/pypi/v/tzolkin-calendar)](https://pypi.org/project/tzolkin-calendar/)
[![ReadTheDocs badge](https://readthedocs.org/projects/tzolkin-calendar/badge/?version=latest)](https://tzolkin-calendar.readthedocs.io/en/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[more badges](#badges)

## Table of Contents <!-- omit in toc -->

- [tzolkin-calendar - Converter for Maya Tzolk’in Dates](#tzolkin-calendar---converter-for-maya-tzolkin-dates)
  - [Links](#links)
  - [Installation and Usage](#installation-and-usage)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
      - [Using the Command-Line Client](#using-the-command-line-client)
        - [Converting Gregorian Dates to Tzolk’in Dates](#converting-gregorian-dates-to-tzolkin-dates)
        - [Searching Tzolk’in Dates](#searching-tzolkin-dates)
        - [Print all Tzolk’in Dates in a Tzolk’in Year](#print-all-tzolkin-dates-in-a-tzolkin-year)
      - [Using the Jupyter Notebook](#using-the-jupyter-notebook)
      - [Using the Python Module in Your Programs](#using-the-python-module-in-your-programs)
        - [Import the Module](#import-the-module)
        - [The Tzolk’in Date Class `Tzolkin`](#the-tzolkin-date-class-tzolkin)
        - [Convert Gregorian Dates to Tzolk’in Dates](#convert-gregorian-dates-to-tzolkin-dates)
        - [Set Tzolk’in Dates](#set-tzolkin-dates)
        - [Search Gregorian Dates to a given Tzolk’in Date](#search-gregorian-dates-to-a-given-tzolkin-date)
        - [Calculations using  Tzolk’in Dates](#calculations-using--tzolkin-dates)
    - [More information](#more-information)
  - [Contributing](#contributing)
    - [Report Issues (Bugs and Feature Requests)](#report-issues-bugs-and-feature-requests)
    - [Changing the Documentation and Source Code](#changing-the-documentation-and-source-code)
    - [Github Documentation on Collaborating with Issues and Pull Requests](#github-documentation-on-collaborating-with-issues-and-pull-requests)
  - [License](#license)
  - [Badges](#badges)
    - [External Checks](#external-checks)
    - [Static Code Checks](#static-code-checks)
    - [Tests](#tests)

## Links

Smithsonian Museo Nacional del Indígena Americano: [Viviendo El Tiempo Maya](https://maya.nmai.si.edu/es)

Website of the Smithsonian National Museum of the American Indian on Mayas [Living Maya Time](https://maya.nmai.si.edu/).

Online general Maya (not only Tzolk’in) calendar converter: [Maya Converter of the Smithsonian NMAI](https://maya.nmai.si.edu/calendar/maya-calendar-converter)

[Convertidor Al Calendario Maya Smithsonian NMIA](https://maya.nmai.si.edu/es/calendario/convertidor-de-calendario-maya)

Mayan Glyphs and Unicode: [Roadmap to the SMP](https://www.unicode.org/roadmaps/smp/) and the PDF [Updated List of Characters for Mayan Codices](https://www.unicode.org/L2/L2020/20248-mayan-update.pdf)

## Installation and Usage

There are 3 Jupyter Notebooks online at [Binder](https://mybinder.org/):

Interactive Tzolk’in converter:
[![Binder tzolkin-calendar Notebook](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Release-Candidate/tzolkin-calendar/main?filepath=Tzolk%E2%80%99in%20Calendar.ipynb)

Command line program:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Release-Candidate/tzolkin-calendar/main?filepath=Tzolk%E2%80%99in%20Command%20Line.ipynb)

The usage of the module tzolkin-calendar in your code:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Release-Candidate/tzolkin-calendar/main?filepath=Tzolk%E2%80%99in%20Calender%20Python%20Module.ipynb)

### Prerequisites

You need Python, at least version 3.9 to be able to use tzolkin-calendar. You can
download it from [python.org](https://www.python.org/downloads/).

To install the package, you need pip, see [Installing pip](https://pip.pypa.io/en/stable/installing/).

### Installation

Install the package using pip on a shell or command prompt:

```shell
python -m pip install tzolkin-calendar
```

More information about using pip you get at [pip Quickstart](https://pip.pypa.io/en/stable/quickstart/)

### Usage

#### Using the Command-Line Client

There is an online interactive Jupyter version: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Release-Candidate/tzolkin-calendar/main?filepath=Tzolk%E2%80%99in%20Command%20Line.ipynb)

We start the command line client of `tzolkin-calendar` using `python -m`: beware of the underscore (`_`)

```python
! python -m tzolkin_calendar
```

``` text
    Gregorian "24.03.2021" is "3 Men" as Tzolk’in
```

As default, if no argument is given, the Tzolk’in date of the current day ('today' ins the 24th of March, 2021) is printed.

To get the version of `tzolkin_calendar`, use the argument `--version`

```python
! python -m tzolkin_calendar --version
```

``` text
    tzolkin-calendar 0.9.3
```

The argument `--help` displays a short usage text, we go through all options in the follwing parts.

```python
! python -m tzolkin_calendar --help
```

``` text
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
```

##### Converting Gregorian Dates to Tzolk’in Dates

To get the Tzolk’in date of a Gregorian date use the Gregorian date as the main argument to `tzolkin_calendar`.

E.g. to get the Tzolk’in date of the 18th of May, 1974, which is "12 Akʼbʼal"

```python
! python -m tzolkin_calendar 18.05.1974
```

``` text
    Gregorian "18.05.1974" is "12 Akʼbʼal" as Tzolk’in
```

Many date format conventions are supported, any of these work (and result in the 18th of May, 1974):  
DD.MM.YYYY - 18.05.1974  
DD-MM-YYYY - 18-05-1974  
DD MM YYYY - 18 05 1974  
YYYY.MM.DD - 1974.05.18  
YYYY-MM-DD - 1974-05-18  
YYYY/MM/DD - 1974/05/18  
YYYY MM DD - 1974 05 18  
MM/DD/YYYY - 05/18/1974

```python
! python -m tzolkin_calendar 05/18/1974
```

``` text
    Gregorian "05/18/1974" is "12 Akʼbʼal" as Tzolk’in
```

##### Searching Tzolk’in Dates

To search for Gregorian Dates to a given Tzolk’in date, input the Tzolk’in date to search for.

As default the search is started today (the 24th of March, 2021). So, we search for "13 Lamat"

```python
! python -m tzolkin_calendar 13 Lamat
```

``` text
    Tzolk’in date "13 Lamat" next date is "24.08.2021", last date has been "07.12.2020"
```

The next gregorian date with a Tzolk’in date of "12 Lamat" after today (the 24th of March 2021) is the 24th od August, 2021, the last gregorian date before today has been the 7th of December 2020.

We again can use many formats to pass as Tzolk’in dates:  
DD NNNN - 13 Lamat  
DD/NNNN - 13/Lamat  
DD.NNNN - 13.Lamat  
DD-NNNN - 13-Lamat  

Instead of the name, we can also use the number of the day name (between 1 and 20), so instead of "Lamat" we could use the number 8. The valid formats are again (with or without leading zeroes).  
DD NN - 13 8  
DD/NN - 13/8  
DD.NN - 13.8  
DD-NN - 13-8  

We can also search starting at other days than today, so lets start the search at the 18th of May 1974, this is the argument to `--start`

```python
! python -m tzolkin_calendar 13 Lamat --start 18.05.1974
```

``` text
    Tzolk’in date "13 Lamat" next date is "31.08.1974", last date has been "14.12.1973"
```

Now the search returned the 31th of August, 1974 as the next and the 14th of December 1974 as the last Gregorian date with
the same Tzolk’in date.

We can also search for more than one date in the future and the past, by using the argument `--list`, which is the number of Gregorian dates to return. Lets search for 5 Gregorian dates with a Tzolk’in date of "13 Lamat", starting at the 18th of May, 1974.

```python
! python -m tzolkin_calendar 13 Lamat --start 18.05.1974 --list 5
```

``` text
    Tzolk’in date "13 Lamat"
     next dates are ['31.08.1974', '18.05.1975', '02.02.1976', '19.10.1976', '06.07.1977']
     last dates have been ['14.12.1973', '29.03.1973', '12.07.1972', '26.10.1971', '08.02.1971']
```

So we're getting 5 Gregorian dates after and before the 18th of May, 1974.

Without an `--start` argument, we start the search today (the 24th of March, 2021).

```python
! python -m tzolkin_calendar 13 Lamat --list 5
```

``` text
    Tzolk’in date "13 Lamat"
     next dates are ['24.08.2021', '11.05.2022', '26.01.2023', '13.10.2023', '29.06.2024']
     last dates have been ['07.12.2020', '22.03.2020', '06.07.2019', '19.10.2018', '01.02.2018']
```

We can make the list as long as we want, but if the list would be too long, we ran out of the valid calendar days.

```python
! python -m tzolkin_calendar 13 Lamat --list 10000
```

```python
    Traceback (most recent call last):
      ...
      File "./tzolkin_calendar/calculate.py", line 432, in lastTzolkin
        return starting + day_diff_delta
    OverflowError: date value out of range
```

##### Print all Tzolk’in Dates in a Tzolk’in Year

To get a list of all 260 Tzolk’in dates in a Tzolk’in year, we use the argument `--year`:

```python
! python -m tzolkin_calendar --year
```

```text
     1 Imix 2 Ikʼ 3 Akʼbʼal 4 Kʼan 5 Chikchan 6 Kimi 7 Manikʼ 8 Lamat 9 Muluk 10 Ok 11 Chuwen 12 Ebʼ 13 Bʼen
     1 Ix
     ...
                                                                                                  13 Manikʼ
     1 Lamat 2 Muluk 3 Ok 4 Chuwen 5 Ebʼ 6 Bʼen 7 Ix 8 Men 9 Kʼibʼ 10 Kabʼan 11 Etzʼnabʼ 12 Kawak 13 Ajaw
    Gregorian "24.03.2021" is "3 Men" as Tzolk’in
```

#### Using the Jupyter Notebook

You can test it online at [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Release-Candidate/tzolkin-calendar/main?filepath=Tzolk%E2%80%99in%20Calendar.ipynb). You need to restart the kernel first
by going to the menu and selecting **Kernel**->**Restart & Run All** to get the interactive
sliders and input fields.

You can get Information about Jupyter Notebooks at the [official site](https://jupyter-notebook.readthedocs.io/en/stable/)

Install Jupyter Notebook and ipywidgets

```shell
python -m pip install notebook ipywidgets
```

If you want to be able to open the Jupyter notebook files directly, install `nbopen`.

```shell
python -m pip install nbopen
```

and add the extension to the list of extensions of your OS, so that you can double click
the `.ipynb` files and Jupyter opens it.

On Linux:

```shell
python -m nbopen.install_xdg
```

On Windows:

```shell
python -m nbopen.install_win
```

For OS X, the installation is a bit more advanced, see [nbopen](https://github.com/takluyver/nbopen)

Download the Tzolk’in calendar notebook at [Tzolk’in Calendar.ipynb](https://raw.githubusercontent.com/Release-Candidate/tzolkin-calendar/main/Tzolk%E2%80%99in%20Calendar.ipynb)

Open it in Jupyter Notebook and run all cells, by going to the menu and using **Kernel**->**Restart & Run All** .

You should now see something like:

![Interactive view of Tzolk’in Calendar](https://raw.githubusercontent.com/Release-Candidate/tzolkin-calendar/main/tzolkin_calendar/doc/images/tzolkin_jupyter_page.png))

#### Using the Python Module in Your Programs

See the second Jupyter Notebook about how to use the tzolkin-calendar module: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Release-Candidate/tzolkin-calendar/main?filepath=Tzolk%E2%80%99in%20Calender%20Python%20Module.ipynb)

##### Import the Module

To use the Tzolk’in date package, import `tzolkin_calender` (with an underscore `_`).

A short check to see if it is working is to print the version of `tzolkin-calendar`, that's the constant `tzolkin_calendar.VERSION`.

```python
# Import the package.
import tzolkin_calendar

# Check, if it is working.
tzolkin_calendar.VERSION
```

```text
    '0.9.3'
```

##### The Tzolk’in Date Class `Tzolkin`

The Tzolk’in date class resides in the module `tzolkin_calendar.tzolkin`, and is named `Tzolkin`.

So, import that module:

```python
# Import the module tzolkin that contains `Tzolkin`.
from tzolkin_calendar import tzolkin
```

##### Convert Gregorian Dates to Tzolk’in Dates

To get the Tzolk’in date of today, call the static method `fromToday`. This returns a `Tzolkin` instance holding the
Tzolk’in date of today ('today' is the 24th of March, 2021, with a Tzolk’in date of '3 Men')

```python
tzolkin.Tzolkin.fromToday()
```

```text
    3 Men
```

You can generate a `Tzolkin` instance from any gregorian date using the `datetime.date` class or a date string.

So, first import the datetime module:

```python
import datetime
```

And then use the 3 possibilities to set the Tzolk’in date from a gregorian date. Or, in other words, to convert a gregorian date to a Tzolk’in date.

1. from a datetime.date instance using `Tzolkin.fromDate`. We use the method `fromisoformat` to set the gregorian date to the
24th of March 2021 with the date string '2021-03-24'. The Tzolk’in date of the 24th of March 2021 is '3 Men'.

```python
gregorian_date = datetime.date.fromisoformat("2021-03-24")

tzolkin.Tzolkin.fromDate(gregorian_date)
```

```text
    3 Men
```

2. from an ISO date string using `Tzolkin.fromIsoFormat`. We set the Tzolk’in date to the 24th of March 2021 with the ISO date
string '2021-03-24'. The Tzolk’in date of the 24th of March 2021 is '3 Men'.

```python
tzolkin.Tzolkin.fromIsoFormat("2021-03-24")
```

```text
    3 Men
```

3. from an arbitrary date string using `Tzolkin.fromDateString`. We set the Tzolk’in date to the 24th of March 2021 with the date string '24=03\*2021' and the format string `fmt` '%d=%m*%Y'. The Tzolk’in date of the 24th of March 2021 is '3 Men'.

```python
tzolkin.Tzolkin.fromDateString("24=03*2021", fmt="%d=%m*%Y")
```

```text
    3 Men
```

##### Set Tzolk’in Dates

You can set the `Tzolkin` instance to a Tzolk’in Date using it's constructor. The construcotr takes the Tzolk’in day number (between 1 and 13 including 1 and 13) and either a Tzolk’in day name or the number of the Tzolk’in day name (between 1 and 20 , including 1 and 20).

To get a dictionary of Tzolk’in day names and numbers, look at `tzolkin.day_names`.

```python
tzolkin.day_names
```

```text
    {1: 'Imix', 2: 'Ikʼ', 3: 'Akʼbʼal', 4: 'Kʼan', 5: 'Chikchan', 6: 'Kimi',
     7: 'Manikʼ', 8: 'Lamat', 9: 'Muluk', 10: 'Ok', 11: 'Chuwen', 12: 'Ebʼ',
     13: 'Bʼen', 14: 'Ix', 15: 'Men', 16: 'Kʼibʼ', 17: 'Kabʼan', 18: 'Etzʼnabʼ',
     19: 'Kawak', 20: 'Ajaw'}
```

If we want to set a Tzolk’in day of '8 Kabʼan', we can either pass the day number 8 and day name Kabʼan to the constructor, or
the day number 8 and the day name number 17.

```python
tzolkin.Tzolkin(number=8, name_str="Kabʼan")
```

```text
    8 Kabʼan
```

```python
tzolkin.Tzolkin(number=8, name_number=17)
```

```text
    8 Kabʼan
```

If we pass an invalid number (not in [1, 13]) or name to the constructor, we get a `TzolkinException`.

```python
tzolkin.Tzolkin(number=53, name_number=17)

    TzolkinException: number 53 is not a valid Tzolkin day number, not between 1 and 13 (including 1 and 13)

tzolkin.Tzolkin(number=3, name_str="Hugo")

    TzolkinException: string "Hugo" is not a valid Tzolkin day name, one of: dict_values(['Imix', 'Ikʼ', 'Akʼbʼal', 'Kʼan', 'Chikchan', 'Kimi', 'Manikʼ', 'Lamat', 'Muluk', 'Ok', 'Chuwen', 'Ebʼ', 'Bʼen', 'Ix', 'Men', 'Kʼibʼ', 'Kabʼan', 'Etzʼnabʼ', 'Kawak', 'Ajaw'])

tzolkin.Tzolkin(number=3, name_number=-5)

    TzolkinException: -5 is not a valid Tzolkin day name number, it must be between 1 and 20 (including 1 and 20)
```

These Tzolk’in day numbers and names can be accessed using the mthods `getDayNumber`, `getDayName` and `getDayNameNumber`.

```python
# Set the Tzolk’in date to '12 Kimi'.
tzolkin_date = tzolkin.Tzolkin(number=12, name_str="Kimi")

tzolkin_date.getDayNumber()
```

```text
    12
```

```python
tzolkin_date.getDayName()
```

```text
    'Kimi'
```

```python
tzolkin_date.getDayNameNumber()
```

```text
    6
```

 To get the number of Tzolk’in day in the Tzolk’in year of 260 days, there is `getTzolkinYearDay`. For example '12 Kimi' is the 246. day (of 260 days)  of the Tzolk’in year

```python
tzolkin_date.getTzolkinYearDay()
```

```text
    246
```

To parse a Tzolk’in day name that isn't exactly like the ones in `tzolkin.day_names` (see \[8\]), there is the method `Tzolkin.parseTzolkinName`, that ignores upper- and lowercase and all non-alphanumeric and non-ascii characters.

```python
day_number = tzolkin.Tzolkin.parseTzolkinName("EtZ`nAB")
if day_number != 0:
    tzolkin_name = tzolkin_calendar.day_names[day_number]
tzolkin_name
```

```text
    'Etzʼnabʼ'
```

All 260 Tzolk’in days of a Tzolk’in year we can get as a list of strings from the static method `getTzolkinCalendar`.

```python
tzolkin.Tzolkin.getTzolkinCalendar()
```

```text
    ['1 Imix', '2 Ikʼ', '3 Akʼbʼal', '4 Kʼan', '5 Chikchan', '6 Kimi', '7 Manikʼ', '8 Lamat', '9 Muluk', '10 Ok',
     '11 Chuwen',
     ...
                                                                                    '1 Lamat', '2 Muluk', '3 Ok',
     '4 Chuwen', '5 Ebʼ', '6 Bʼen', '7 Ix', '8 Men', '9 Kʼibʼ', '10 Kabʼan', '11 Etzʼnabʼ', '12 Kawak', '13 Ajaw']
```

##### Search Gregorian Dates to a given Tzolk’in Date

We can search for the next (forward in time) or last (backwards in time) day with the same Tzolk’in date using the methods `getNextDate` and `getLastDate`. Both methods return a `datetime.date` object.

When searching for the next gregorian date that has the Tzolk’in date '7 Kawak', we get the 28th of March, 2021 - because we started searching 'today', which is the 24th of March 2021.

```python
# Set the Tzolk’in date to search for to '7 Kawak'.
tzolkin_date = tzolkin.Tzolkin(number=7, name_str="Kawak")

tzolkin_date.getNextDate()
```

```text
    datetime.date(2021, 3, 28)
```

When searching for the last gregorian date that has the Tzolk’in date '7 Kawak', we get the 11th of July, 2020 - because we started searching 'today', which is the 24th of March 2021.

```python
tzolkin_date.getLastDate()
```

```text
    datetime.date(2020, 7, 11)
```

Both methods, `getNextDate` and `getLastDate` take an optional argument `start_date`, which is the gregorian date to start
the search. If no `start_date` is given, 'today' is used as the start date.

So now we search again for '7 Kawak' in both directions, but this time we start at the 10th of July, 2020.

```python
# Set the Tzolk’in date to search for to '7 Kawak'.
tzolkin_date = tzolkin.Tzolkin(number=7, name_str="Kawak")

# Set the start date of the search to the 10th of July, 2020.
start_search = datetime.date.fromisoformat("2020-07-10")

start_search.isoformat()
```

```text
    '2020-07-10'
```

For the next day with a Tzolk’in date of '7 Kawak' we now get the 11th of July, 2020.

```python
tzolkin_date.getNextDate(start_date=start_search)
```

```text
    datetime.date(2020, 7, 11)
```

For the last day before our start date with a Tzolk’in date of '7 Kawak' we now get the 25th of October, 2019.

```python
tzolkin_date.getLastDate(start_date=start_search)
```

```text
    datetime.date(2019, 10, 25)
```

To get a list of `datetime.date` dates with the same Tzolk’in date, we can use the methods `getNextDateList` and `getLastDateList`.

Again, we can set the argument `start_date` to a gregorian date to start the search or not set it to start the search today.
The number of elements in the returned list is set using the parameter `list_size`, which defaults to 50.

Let's start the search for dates with a Tzolk’in date of ' 7 Kawak' today, the 24th of March 2021, and set the list size to 9 elements:

```python
# Set the Tzolk’in date to search for to '7 Kawak'.
tzolkin_date = tzolkin.Tzolkin(number=7, name_str="Kawak")

tzolkin_date.getNextDateList(list_size=9)
```

```text
    [datetime.date(2021, 3, 28),
     datetime.date(2021, 12, 13),
     datetime.date(2022, 8, 30),
     datetime.date(2023, 5, 17),
     datetime.date(2024, 2, 1),
     datetime.date(2024, 10, 18),
     datetime.date(2025, 7, 5),
     datetime.date(2026, 3, 22),
     datetime.date(2026, 12, 7)]
```

Now start searching for '7 Kawak' on the 29th of March, 2021 and set the returned list size to 5.

```python
# Set the start date of the search to the 29th of March, 2021.
start_search = datetime.date.fromisoformat("2021-03-29")

tzolkin_date.getLastDateList(start_date=start_search, list_size=5)
```

```text
    [datetime.date(2021, 3, 28),
     datetime.date(2020, 7, 11),
     datetime.date(2019, 10, 25),
     datetime.date(2019, 2, 7),
     datetime.date(2018, 5, 23)]
```

##### Calculations using  Tzolk’in Dates

There are 4 methods to get the difference in days between two Tzolk’in dates and to add (or subtract) days from a Tzolk’in date: `addDays`, `addTimedelta`, `getDayDiff` and `getDayTimedelta`.

Lets start with a Tzolk’in date of '6 Muluk'.

```python
tzolkin.Tzolkin(number=6, name_str="Muluk")
```

```text
    6 Muluk
```

Add 6 days to it, and we get a Tzolk’in date of '12 Men'.

```python
tzolkin.Tzolkin(number=6, name_str="Muluk").addDays(6)
```

```text
    12 Men
```

Instead of using ints, we can also add and subtract `datetime.timedelta` objects.
Now subtract 6 days from '12 Men' - we get '6 Muluk'.

```python
to_subtract = datetime.timedelta(days=-6)

tzolkin.Tzolkin(number=12, name_str="Men").addTimedelta(to_subtract)
```

```text
    6 Muluk
```

To get the difference between two Tzolk’in dates there exist the Methods `getDayDiff` and `getDayTimedelta`.

Lets calculate the difference in days between '6 Muluk' and '12 Men'.

```python
# Set start_tzolkin to '6 Muluk'.
start_tzolkin = tzolkin.Tzolkin(number=6, name_str="Muluk")

# Set end_tzolkin to '12 Men'.
end_tzolkin = tzolkin.Tzolkin(number=12, name_str="Men")

start_tzolkin.getDayDiff(end_tzolkin)
```

```text
    6
```

And using `getDayTimedelta`, which returnes a `datetime.timedelta` object.

```python
start_tzolkin.getDayTimedelta(end_tzolkin)
```

```text
    datetime.timedelta(days=6)
```

What happens, if we calculate the difference between '12 Men' and '6 Muluk'?

```python
end_tzolkin.getDayDiff(start_tzolkin)
```

```text
    254
```

We get 254 days, not -6. That's because the difference is always calculated forward in time. If you want to get negative days or the shortest possible time difference, subtract 260 from the the result (the number of days in a Tzolk’in year). As soon as the difference in days is greater than 130, to minimum time distance in days 'is negative'.

```python
day_diff = end_tzolkin.getDayDiff(start_tzolkin)

if day_diff > 130:
    day_diff = 260 - day_diff
day_diff
```

```text
    6
```

Or you can use the minimum of `result` and ``|result - 260|`` that is ``abs(result - 260)``.

```python
day_diff = end_tzolkin.getDayDiff(start_tzolkin)
shortest_diff = min(day_diff, abs(day_diff - 260))
shortest_diff
```

```text
    6
```

### More information

Detailed information is available at the [documentation website](https://tzolkin-calendar.readthedocs.io/en/latest/).

## Contributing

Any help is welcome!

If you encounter a problem using tzolkin-calendar, a task it not as easy as you'd like it to be
or you'd like something added to it: open an issue at GitHub.

### Report Issues (Bugs and Feature Requests)

File a bug report at [Github](https://github.com/Release-Candidate/tzolkin-calendar/issues/new?assignees=&labels=&template=bug_report.md&title=)

Add a feature request at [Github](https://github.com/Release-Candidate/tzolkin-calendar/issues/new?assignees=&labels=&template=feature_request.md&title=)

### Changing the Documentation and Source Code

If you'd like to contribute directly, e.g. better the documentation, add another language or
write some source code: fork tzolkin-calendar by clicking the `Fork`-button in the upper right
corner of the [GitHub project website](https://github.com/Release-Candidate/tzolkin-calendar).
Check out your fork of tzolkin-calendar using the URL from the `Code`-button of your fork on Github.
The URL should be something like *github.com/YOUR_USERNAME/tzolkin-calendar.git*.

Details about how to fork a repository on Github are [here](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/working-with-forks)

and set up the development environment using pipenv.

First, install pipenv if you don't already have it installed:

```shell
python -m pip install --upgrade pipenv
```

and install all needed packages to develop tzolkin-calender:

```shell
cd tzolkin-calendar
python -m pipenv install --dev
```

That command installs all packages in `Pipfile`/`Pipfile.lock` in the directory `tzolkin-calender`,
the root directory of tzolkin-calendar.

More information about pipenv can be found at [Pipenv](https://pipenv.pypa.io/en/latest/).

Make your changes, push them to your forked repository and make a pull-request (e.g.
using the `Pull request`-button above and right of GitHubs source file view).

See [GitHub on Pull-Requests](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/proposing-changes-to-your-work-with-pull-requests)

### Github Documentation on Collaborating with Issues and Pull Requests

See GitHub's documentation about how to contribute for details: [Contributing at Github](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests)

## License

Everything in `tzolkin-calendar` is licensed under the MIT license, see file [LICENSE](./LICENSE)

## Badges

### External Checks

[![DeepSource](https://deepsource.io/gh/Release-Candidate/tzolkin-calendar.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/Release-Candidate/tzolkin-calendar/?ref=repository-badge)
[![Maintainability](https://api.codeclimate.com/v1/badges/023820a03165a9846d8c/maintainability)](https://codeclimate.com/github/Release-Candidate/tzolkin-calendar/maintainability)
[![codecov](https://codecov.io/gh/Release-Candidate/tzolkin-calendar/branch/main/graph/badge.svg?token=VAYTZWLGPO)](https://codecov.io/gh/Release-Candidate/tzolkin-calendar)

### Static Code Checks

[![Bandit](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/bandit.yml/badge.svg)](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/bandit.yml)
[![Black](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/black.yml/badge.svg)](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/black.yml)
[![Flake8](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/flake8.yml/badge.svg)](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/flake8.yml)
[![Pycodestyle](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/pycodestyle.yml/badge.svg)](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/pycodestyle.yml)
[![Pydocstyle](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/pydocstyle.yml/badge.svg)](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/pydocstyle.yml)
[![Pyflakes](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/pyflakes.yml/badge.svg)](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/pyflakes.yml)

### Tests

[![Mac OS X latest](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/osx.yml/badge.svg)](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/osx.yml)
[![Tests Mac OS X latest](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/osx_test.yml/badge.svg)](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/osx_test.yml)
[![Ubuntu 20.04](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/linux.yml/badge.svg)](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/linux.yml)
[![Tests Ubuntu 20.04](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/linux_test.yml/badge.svg)](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/linux_test.yml)
[![Tests Windows 2019](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/windows_test.yml/badge.svg)](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/windows_test.yml)

Problem with Unicode output on GitHub's Windows 2019 Server: [![Windows 2019](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/windows.yml/badge.svg)](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/windows.yml), see [Issue #1](https://github.com/Release-Candidate/tzolkin-calendar/issues/1)

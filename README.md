# tzolkin-calendar - Converter for Maya Tzolk’in Dates

This program converts mayan Tzolk’in dates to gregorian dates and vice versa.
If you want to know more about the maya calendar systems, see [Links](#links).

Information about the installation and usage you find at [Installation and Usage](#installation-and-usage)

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
[![Windows 2019](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/windows.yml/badge.svg)](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/windows.yml)
[![Tests Windows 2019](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/windows_test.yml/badge.svg)](https://github.com/Release-Candidate/tzolkin-calendar/actions/workflows/windows_test.yml)

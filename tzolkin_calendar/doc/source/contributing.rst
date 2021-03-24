Contributing
============

Any help is welcome!

If you encounter a problem using tzolkin-calendar, a task it not as easy as you'd like it to be
or you'd like something added to it: open an issue at GitHub.

Report Issues (Bugs and Feature Requests)
-----------------------------------------

| File a bug report at `Github <https://github.com/Release-Candidate/tzolkin-calendar/issues/new?assignees=&labels=&template=bug_report.md&title=>`_.
Add a feature request at `Github <https://github.com/Release-Candidate/tzolkin-calendar/issues/new?assignees=&labels=&template=feature_request.md&title=>`_.

Forking the Repository
----------------------

If you'd like to contribute directly, e.g. better the documentation, add another language or
write some source code: fork tzolkin-calendar by clicking the ``Fork``-button in the upper right
corner of the `GitHub project website <https://github.com/Release-Candidate/tzolkin-calendar>`_.
Check out your fork of tzolkin-calendar using the URL from the ``Code``-button of your fork on Github.
The URL should be something like **github.com/YOUR_USERNAME/tzolkin-calendar.git**.

Details about how to fork a repository on Github are `here <https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/working-with-forks>`_.

Setting the Development Environment
-----------------------------------

All needed packages to develop tzolkin-calendar are installed in a virtual environment using
``pipenv``, so your system-wide Python installation isn't affected by it.

First, install pipenv if you don't already have it installed:

.. code-block:: shell

    python -m pip install --upgrade pipenv


and install all needed packages to develop tzolkin-calender:

.. code-block:: shell

    cd tzolkin-calendar
    python -m pipenv install --dev

That command installs all packages in ``Pipfile``/``Pipfile.lock`` in the directory ``tzolkin-calender``,
the root directory of tzolkin-calendar.

More information about pipenv can be found at `Pipenv <https://pipenv.pypa.io/en/latest/>`_.

Make your changes, push them to your forked repository and make a pull-request (e.g.
using the `Pull request`-button above and right of GitHubs source file view).

See [GitHub on Pull-Requests](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/proposing-changes-to-your-work-with-pull-requests)

Github Documentation on Collaborating with Issues and Pull Requests
-------------------------------------------------------------------

See GitHub's documentation about how to contribute for details: `Contributing at Github <https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests>`_.

Common Tasks Developing tzolkin-calendar
----------------------------------------

Jupyter Notebooks
.................

The 3 Jupyter Notebooks are located in the project root directory `tzolkin_calendar`, named
``Tzolk’in Calendar.ipynb``, ``Tzolk’in Command Line.ipynb`` and ``Tzolk’in Calender Python Module.ipynb``

Changing and Generating Documentation
.....................................

All files to generate the Sphinx documentation for Read The Docs are located in the directory
``tzolkin_calendar/tzolkin_calendar/doc/source``.

* conf.py ... the Sphinx documentation
* *.rst ... the reStructuredText source file to generate the HTML documentation.

After changing any of these files, you need to run ``sphinx-build`` using the ``Makefile``
or the ``make`` script.

On Windows use the batch file ``make.bat`` with the argument ``html``:

.. code-block:: shell

    cd tzolkin_calendar\tzolkin_calendar\doc\
    make html

Anywhere else use ``make`` with the argument ``html``:

.. code-block:: shell

    cd tzolkin_calendar/tzolkin_calendar/doc/
    make html

After that, the new HTML documentation should have been generated in ``tzolkin_calendar/tzolkin_calendar/doc/html``
and you can open ``tzolkin_calendar/tzolkin_calendar/doc/html/index.html`` in a browser to see it.

GitHub Documentation
,,,,,,,,,,,,,,,,,,,,

The Markdown documentation for GitHub are the files ``README.md`` and ``CHANGELOG.md``
in the project root directory `tzolkin_calendar`.

Python Source Code
..................

The Python source code is located in the directory ``tzolkin_calendar/tzolkin_calendar/``.

* __main__.py    ... Just a wrapper to call ``main()`` in the file ``main.py``
* __init__.py    ... Some constants, like ``VERSION``, which holds the package's version string.
* tzolkin.py     ... The Tzolk’in date class ``Tzolkin``, the main interface of the package
* calculate.py   ... Function that do the actual date calculations are are used by the Tzolk’in date class.
* main.py        ... Main entry point of the command line client, when the module is executed instead of imported.
* commandline.py ... The command line parsing for the command line client.

See also :ref:`tzolkin_calendar`.

Tests
.....

All test code is located in the directory ``tzolkin-calendar/tests/``. Pytest is used as
test runner.

* test_tzolkin.py  ... Tests of the Tzolk’in date class ``Tzolkin``
* test_calender.py ... Tests of the Tzolk’in date calculation functions in ``calculate.py``
* test_main.py     ... Tests of the command line client, files ``main.py`` and ``commandline.py``
* __init__.py      ... some program or external site needs that(?)

To run the tests, go to the root directory ``tzolkin-calendar`` (not ``tzolkin_calendar``) 
and call Pytest.

.. code-block:: shell

    pytest --no-cov

which runs the tests without coverage analysis.

To see statistics of Hypothesis, add the argument ``--hypothesis-show-statistics``

.. code-block:: shell

    pytest --hypothesis-show-statistics --no-cov

To speed up the execution, use more than one process, the argument to ``-n`` is the number
processes to use.

.. code-block:: shell

    pytest --hypothesis-show-statistics --no-cov -n 24

uses 24 processes to run the tests.

There are two scripts, ``run_test.bat`` and ``run_tests.sh`` that you can use to run the
tests.

.. code-block:: shell

    run_tests

or

.. code-block:: shell

    ./run_tests.sh

Local Source Code Linters
.........................

To check the Python sources and tests using static code checkers and fix import order and
the formatting, call the script ``run_local_linters.sh`` or ``run_local_linters.bat``

.. code-block:: shell

    run_local_linters

or

.. code-block:: shell

    ./run_local_linters.sh

GitHub Workflows/Actions
........................

The GitHub Workflows/Actions are located in ``tzolkin-calendar/.github/workflows/``

* bandit.yml     ... Run Bandit, static code checker
* black.yml      ... Run Black, Python code formatter
* create_pip.yml ... Create the tzolkin-calendar pip package and upload it to PyPI
* flake8.yml     ... Run Flake8, static code checker
* linux.yml      ... Run the command line client under Linux, from src and the package
* linux_test.yml ... Run the tests under Linux, from src and the package
* osx.yml        ... Run the command line client under OS X, from src and the package
* osx_test.yml   ... Run the tests under OS X, from src and the package
* pycodestyle.yml ... Run PyCodeStyle, static code checker
* pydocstyle.yml  ... Run PyDocStyle, static code checker
* pyflakes.yml    ... Run PyFlakes, static code checker
* windows.yml      ... Run the command line client under Windows, from src and the package
* windows_test.yml ... Run the tests under Windows, from src and the package

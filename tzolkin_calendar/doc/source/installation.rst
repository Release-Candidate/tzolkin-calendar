Installation
============

Prerequisites
-------------

You need Python, at least version 3.9 to be able to use tzolkin-calendar. You can
download it from `python.org <https://www.python.org/downloads/>`_.

To install the package, you need pip, see [Installing pip](https://pip.pypa.io/en/stable/installing/).
But normally pip is installed with Python, if the version is sufficiently recent.

Windows
.......

Download and install the latest Python from `python.org <https://www.python.org/downloads/>`_.
The official documentation about how to install Python on Windows:
`Using Python on Windows <https://docs.python.org/3/using/windows.html>`_
Use the options to add Python to your ``PATH`` and install pip, the package manager used to
install Python packages like tzolkin_calendar.

Linux
.....

Use your distribution's package management system (apt, dnf, ...) to install Python 3.9 and pip.
If your distribution'S official packages are too old, you can install from source from
`python.org <https://www.python.org/downloads/>`_ or search for a newer package or repository.

Mac OS X
........

Download and install the latest Python from `python.org <https://www.python.org/downloads/>`_.
The official documentation about how to install Python on OS X:
`Using Python on OS X <https://docs.python.org/3/using/mac.html>`_

Or you can use the `Homebrew <https://brew.sh/>`_ package manager to install PYthon (and many other OSS packages)
`Homebrew Python 3.9 <https://formulae.brew.sh/formula/python@3.9>`_.


Installation
-------------

Install the package using pip on a shell or command prompt:

.. code-block:: shell

    python -m pip install tzolkin-calendar


Depending on your Python installation and/or OS, you may also need to call Python 3.9 using

.. code-block:: shell

    python3 -m pip install tzolkin-calendar

or

.. code-block:: shell

    python3.9 -m pip install tzolkin-calendar


If neither version works, the right Python executable is not in your ``PATH``.

To upgrade an installed version of tzolkin-calendar to the latest version, add the argument ``--upgrade``.

.. code-block:: shell

    python -m pip install --upgrade tzolkin-calendar

More information about using pip you get at `pip Quickstart <https://pip.pypa.io/en/stable/quickstart/>`_.

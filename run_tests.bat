:: SPDX-License-Identifier: MIT
:: Copyright (C) 2021 Roland Csaszar
::
:: Project:  tzolkin-calendar
:: File:     run_tests.bat
:: Date:     23.Mar.2021
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:: slow version
:: pytest --hypothesis-show-statistics --no-cov

:: Running the tests using 12 processes.
pytest --hypothesis-show-statistics --no-cov -n 12

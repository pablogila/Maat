# Maat v2.4.2

Welcome to **M**y **A**n**A**lysis **T**ools; or just **Maat**, as the Egyptian goddess of truth, order, and justice.  

Just as an egyptian goddess fallen from the sky, this Python package makes my life easier when analyzing INS, FTIR and Raman CSV data files, among others.
Bear in mind that, as any egyptian god, Maat is not perfect and may be full of bugs. Please report any issues you may find.  


## Installation

As always, it is strongly recommended to install this package inside a Python virtual environment.  

Install the required dependencies by running:  
```shell
pip install numpy pandas matplotlib scipy
```

To install Maat, clone the repository from [GitHub](https://github.com/pablogila/Maat/) or download it as a ZIP and run:  
```shell
pip install .
```


## Usage

You can [check the latest documentation online](https://pablogila.github.io/Maat/).
An offline copy is also available in `/docs/maat.html`.
Note that code examples are also provided in the `/examples/` folder.  

Maat has the following submodules:

- [Classes](https://pablogila.github.io/Maat/maat/classes.html). Here are the objects that allow you to work with the data. Loaded directly as `maat.Class(options)`.
- [Constants](https://pablogila.github.io/Maat/maat/constants.html). Common constants and conversion factors. Loaded directly as `maat.value`.
- [Fit](https://pablogila.github.io/Maat/maat/fit.html). Fitting operations.
- [Normalize](https://pablogila.github.io/Maat/maat/normalize.html). Normalization operations.
- [Plot](https://pablogila.github.io/Maat/maat/plot.html). Plotting operations.
- [Deuteration](https://pablogila.github.io/Maat/maat/deuteration.html). Deuteration estimation.
- [Sample](https://pablogila.github.io/Maat/maat/sample.html). Sample data for testing.
- [Utils](https://pablogila.github.io/Maat/maat/utils.html). Utility functions to make things easier.

The documentation can be compiled automatically using [pdoc](https://pdoc.dev/), by running:
```shell
source pdoc.sh
```


## License

> TL;DR: Do what you want with this, as long as you share the source code of your modifications, also under GNU AGPLv3.  

Copyright (C) 2024  Pablo Gila-Herranz

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the attached GNU Affero General Public License for more details.

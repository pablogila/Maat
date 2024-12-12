# Maat v2.6.0-dev1

Welcome to **M**y **A**n**A**lysis **T**ools; or just **Maat**, as the Egyptian goddess of truth, order, and justice.  

Just as an Egyptian goddess fallen from the sky, this Python package makes my life easier when analyzing scientific data, such as experimental INS, FTIR and Raman CSV data files, among others.

Like the Egyptian goddess, Maat is *married* to [Thoth](https://github.com/pablogila/Thoth), a super useful text file management package. Note that Thoth is required to run Maat. I don't know if this is lore accurate, but seriously, Thoth is a dependency to run the Maat package, so go ahead and install it.  


## Installation

As always, it is strongly recommended to install this package inside a Python virtual environment.  

Install the required dependencies by running:  
```shell
pip install numpy pandas matplotlib scipy
```
Additionally, you need to install the [Thoth]() python package.

To install Maat, clone the repository from [GitHub](https://github.com/pablogila/Maat/) or download it as a ZIP and run:  
```shell
pip install .
```


## Documentation

You can [check the latest documentation online](https://pablogila.github.io/Maat/).
An offline copy is also available in `/docs/maat.html`.
Note that code examples are also provided in the `/examples/` folder.  

Maat has the following submodules:

- [alias](https://pablogila.github.io/Maat/maat/alias.html). Similar to [thoth.alias](https://pablogila.github.io/Thoth/thoth/alias.html), contains common dictionaries with science-related strings, to correct user inputs.
- [classes](https://pablogila.github.io/Maat/maat/classes.html). Here are the objects that allow you to work with the data. Loaded directly as `maat.Class(options)`.
- [constants](https://pablogila.github.io/Maat/maat/constants.html). Common constants and conversion factors. Loaded directly as `maat.value`.
- [fit](https://pablogila.github.io/Maat/maat/fit.html). Fitting operations.
- [normalize](https://pablogila.github.io/Maat/maat/normalize.html). Normalization operations.
- [plot](https://pablogila.github.io/Maat/maat/plot.html). Plotting operations.
- [deuteration](https://pablogila.github.io/Maat/maat/deuteration.html). Deuteration estimation.
- [sample](https://pablogila.github.io/Maat/maat/sample.html). Sample data for testing.

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

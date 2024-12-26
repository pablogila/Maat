# Maat v3.0.1

Welcome to **M**y **A**n**A**lysis **T**ools; or just **Maat**, as the Egyptian goddess of truth, order, and justice.  

Just as an Egyptian goddess fallen from the sky, this Python package makes my life easier when analyzing scientific data, such as experimental INS, FTIR and Raman CSV data files, among others.

Like the Egyptian goddess, Maat is *married* to [Thoth](https://github.com/pablogila/Thoth), a super useful text file management package.
Note that although Thoth is not required to run Maat, it is needed to compile Maat's documentation.  


## Installation

As always, it is strongly recommended to install this package inside a Python virtual environment:  
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required dependencies by running:  
```shell
pip install numpy pandas matplotlib scipy
```

To install Maat, clone the repository from [GitHub](https://github.com/pablogila/Maat/) or download the [latest stable release](https://github.com/pablogila/Maat/tags)  as a ZIP and run inside the `/Maat/` directory:  
```shell
pip install .
```


## Documentation

You can [check the latest documentation online](https://pablogila.github.io/Maat/).
An offline copy is also available in `/docs/maat.html`.
Code examples are provided in the `/tests/` folder.  

Maat has the following submodules:

- [alias](https://pablogila.github.io/Maat/maat/alias.html). Common dictionaries to correct user inputs.
- [constants](https://pablogila.github.io/Maat/maat/constants.html). Universal constants and conversion factors. Use them directly as `maat.value`.
- [elements](https://pablogila.github.io/Maat/maat/elements.html). Contains the `maat.atom` dictionary, with the properties of all the elements (mass, cross section, etc).
- [atoms](https://pablogila.github.io/Maat/maat/atoms.html). Used to build and manage atomic elements.
- [classes](https://pablogila.github.io/Maat/maat/classes.html). Classes that allow you to work with the data, such as loading INS spectra, etc.
- [plot](https://pablogila.github.io/Maat/maat/plot.html). Plotting functions.
- [fit](https://pablogila.github.io/Maat/maat/fit.html). Fitting operations.
- [normalize](https://pablogila.github.io/Maat/maat/normalize.html). Normalization operations.
- [deuteration](https://pablogila.github.io/Maat/maat/deuteration.html). Tools to estimate deuteration levels.
- [sample](https://pablogila.github.io/Maat/maat/sample.html). Sample data for testing purposes.

The documentation can be compiled automatically using [pdoc](https://pdoc.dev/) and [Thoth](https://github.com/pablogila/Thoth), by running:
```shell
source makedocs.py
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

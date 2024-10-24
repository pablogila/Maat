'''
.. include:: ../README.md
    :end-before: Usage

## Usage

You can check the latest documentation [online](https://pablogila.github.io/Maat/).
An offline copy is also available [here](./maat.html).
Note that code examples are also provided in the `/examples/` folder.  

Maat has the following submodules:

- `maat.classes`. Here are the objects that allow you to work with the data.
- `maat.constants`. Common constants and conversion factors.
- `maat.fit`. Fitting operations.
- `maat.normalize`. Normalization functions.
- `maat.plot`. Plotting operations.
- `maat.deuteration`. Functions to estimate the deuteration level in your samples.
- `maat.sample`. Sample data for testing.
- `maat.utils`. Utility functions to make things easier.

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
'''


from .constants import *
from .classes import *
from .utils import *
from . import sample
from . import normalize
from . import fit
from . import plot
from . import deuteration


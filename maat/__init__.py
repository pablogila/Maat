'''
.. include:: ../_README_temp.md
'''


from . import alias
from .constants import *
from .atomsclass import Isotope, Element
from .atomsdict import atom
from . import atoms
from .classes import *
from . import sample
from . import normalize
from . import fit
from . import plot
from . import deuteration


# Do not use spaces between the = sign,
# it is the keyword to deduce the version when making the docs!
version='v3.0.0-dev3'


from .constants import *
from .classes import *


'''This module contains premade examples of material compositions and other experimental values.'''


#############################
##  MATERIAL COMPOSITIONS  ##
#############################
MAPI = Material(
    atoms={'Pb': 1, 'I': 3, 'C': 1, 'N': 1, 'H': 6},
    name='MAPbI3'
    )
MAPI.set()

MAPI_CDND = Material(
    atoms={'Pb': 1, 'I': 3, 'C': 1, 'N': 1, 'D': 6},
    name='CD3ND3PbI3'
    )
MAPI_CDND.set()

MAPI_ND = Material(
    atoms={'Pb': 1, 'I': 3, 'C': 1, 'N': 1, 'H': 3, 'D': 3},
    name='CH3ND3PbI3'
    )
MAPI_ND.set()

MAPI_CD = Material(
    atoms={'Pb': 1, 'I': 3, 'C': 1, 'N': 1, 'H': 3, 'D': 3},
    name='CD3NH3PbI3'
    )
MAPI_CD.set()

CH3NH3I = Material(
    atoms={'C' : 1, 'N': 1, 'H': 6},
    name='CH3NH3'
    )
CH3NH3I.set()

CH3ND3I = Material(
    atoms={'C' : 1, 'N': 1, 'H': 3, 'D': 3},
    name='CH3ND3'
    )
CH3ND3I.set()


###########################
##  EXPERIMENTAL VALUES  ##
###########################
MAPI_peaks = {
    'baseline'       : None,
    'baseline_error' : None,
    'h6d0'           : [36.0, 39.0],
    'h5d1'           : [33.0, 35.0],
    'h4d2'           : [30.7, 33.0],
    'h3d3'           : [28.8, 30.7],
}
'''
Experimental values of the partially-deuterated amine peaks\n
for the disrotatory mode of MAPbI3's methylammonium.\n
Measured at TOSCA, ISIS RAL, UK, May 2024.
'''


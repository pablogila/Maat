'''
## Description
This module contains utility functions.

---
'''


import os
import sys


def run_here():
    '''
    Run from the same directory as the current script, with `maat.run_here()`.
    Useful to run scripts from the VSCode terminal, etc.
    '''
    caller = os.path.dirname(os.path.abspath(os.path.realpath(sys.argv[0])))
    os.chdir(caller)
    return caller


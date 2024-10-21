'''
This module contains utility functions.
'''


import os
import sys


def run_here():
    '''Run the script from anywhere with `mt.run_here()`. Useful to run scripts from the VSCode terminal, etc.'''
    caller = os.path.dirname(os.path.abspath(os.path.realpath(sys.argv[0])))
    os.chdir(caller)
    return caller


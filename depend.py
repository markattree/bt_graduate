#!/usr/bin/python

"""

depend.py -- BT Graduate Test Coding Test Submission

Author: Mark Attree

"""

import sys

class Dependencies():

    def __init__(self, filename, pkgs):
        self.filename = filename
        self.pkgs = pkgs
        
        print self.filename
        print self.pkgs

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print "Not enough arguments"
    else:
        #Index 0 is the python script filename, so ignore
        depend = Dependencies(sys.argv[1], sys.argv[2:])

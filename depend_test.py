#!/usr/bin/python

"""

depend_test.py -- Automated testing harness for the BT Graduate Test Coding Test Submission

Author: Mark Attree

"""

import os

#Test 1 - Normal input file, all other arguments contained in the file
print "******************** TEST 1 ********************"
print "Expected results:"
print "gui -> awtui extensions framework runner swingui"
print "swingui -> extensions framework runner"
print ""
print "Actual results"
os.system("python depend.py input.txt gui swingui")
print ""

#Test 2 - Normal input file with blank lines, all other arguments contained in the file
print "******************** TEST 2 ********************"
print "Expected results:"
print "gui -> awtui extensions framework runner swingui"
print "swingui -> extensions framework runner"
print ""
print "Actual results"
os.system("python depend.py blank_lines.txt gui swingui")
print ""

#Test 3 - Normal input file, mixture of arguments contained or not contained in the file
print "******************** TEST 3 ********************"
print "Expected results:"
print "awtui -> framework runner"
print "extensions -> framework"
print "unknown ->"
print ""
os.system("python depend.py input.txt awtui extensions unknown")

#Test 4 - Normal input file with blank lines, mixture of arguments contained or not contained in the file
print "******************** TEST 4 ********************"
print "Expected results:"
print "awtui -> framework runner"
print "extensions -> framework"
print "unknown ->"
print ""
os.system("python depend.py blank_lines.txt awtui extensions unknown")

#Test 5 - Empty input file
print "******************** TEST 5 ********************"
print "Expected results:"
print "gui ->"
print "swingui ->"
print ""
print "Actual results"
os.system("python depend.py empty.txt gui swingui")
print ""

#Test 6 - Malformed input file
print "******************** TEST 6 ********************"
print "Expected results:"
print "Error: input file must contain a package name followed by '->'."
print ""
print "Actual results"
os.system("python depend.py bad_input.txt gui swingui")
print ""

#Test 7 - Missing input file
print "******************** TEST 7 ********************"
print "Expected results:"
print "Error: the input file does not exist."
print ""
print "Actual results"
os.system("python depend.py does_not_exist.txt framework runner awtui")
print ""

#Test 8 - Not enough arguments specified
print "******************** TEST 8 ********************"
print "Expected results:"
print "Error: you must specify at least an input file and a package name."
print ""
print "Actual results"
os.system("python depend.py input.txt")
print ""

#Test 9 - Input file containing a circular dependency and some blank lines
print "******************** TEST 9 ********************"
print "Expected results:"
print "gui -> awtui extensions framework runner swingui"
print ""
print "Actual results"
os.system("python depend.py input_circular.txt gui")
print ""

#Test 10 - Normal input file, with a package depending on all the others + testing a package with an empty list of dependencies
print "******************** TEST 10 ********************"
print "Expected results:"
print "other -> awtui empty extensions framework gui other runner swingui textui"
print "empty ->"
print ""
print "Actual results"
os.system("python depend.py input_all.txt other empty")
print ""

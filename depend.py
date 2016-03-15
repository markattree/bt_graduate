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
        self.dependencies = {} #Dictionary data structure to map a package to a list of its direct dependencies

        #Read in each line of the file, ignore empty lines
        try:
            for line in open(self.filename, "r"):
                words = line.split()

                #Ignore the empty lines
                if len(words) > 0:
                    try:
                        if words[1] == "->":
                            self.dependencies[words[0]] = words[2:]
                        #Exit if second word of the line is not an arrow
                        else:
                            sys.exit("Error: input file must contain a package name followed by '->'.")
                    #Also exit if words[1] doesn't exist
                    except IndexError:
                        sys.exit("Error: input file must contain a package name followed by '->'.")

        except IOError:
            sys.exit("Error: the input file does not exist.")

        #Retrieve dependencies for each of the specified packages
        for pkg in self.pkgs:
            self.get_dependencies(pkg)

    #Prints dependencies for a given package
    def get_dependencies(self, pkg):
        #If the pkg is provided in the input file, find its dependencies
        if pkg in self.dependencies:
            deps = self.dependencies[pkg]

            #Loop through the dependencies to find transitive dependencies
            for i in range(0, len(deps)):
                if deps[i] in self.dependencies:
                    #For the dependencies found, add them to the list to find their dependencies too
                    for dep in self.dependencies[deps[i]]:
                        #Only added if they have not already been added, or it is not circular
                        if dep not in deps and dep != pkg:
                            deps.append(dep)

            #Sort the list before printing
            deps.sort()

            #Join the list to remove brackets, then use replace to remove commas
            print "{0} -> {1}".format(pkg, ", ".join(deps).replace(",", ""))

        #If pkg is not in the file, print the pkg with no dependencies
        else:
            print "{0} ->".format(pkg)


if __name__ == '__main__':
    #Exit if the user does not specify enough arguments
    if len(sys.argv) < 3:
        sys.exit("Error: you must specify at least an input file and a package name.")

    else:
        #Index 0 is the python script filename, so ignore
        depend = Dependencies(sys.argv[1], sys.argv[2:])

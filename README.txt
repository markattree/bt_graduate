******************** Usage ********************

To check the dependencies of a given file, run the following command:

    python depend.py <input file> <package name> <package name>

Any number of packages can be specified in a space separated list after the input file, as long as there is at least 1.

The input file can be of any type, provided it can be read using Python. Recommended types are .txt or .dat. Each line of the input file must follow the format:

    package_name -> dependency1 dependency2 dependencyN

Any blank lines in the file will be ignored, however any lines not in the format stated above or that do not contain at least a package name and a '->' will cause the program to terminate.

******************** Automated Test Harness ********************

To run the automated test harness, run the following command:

    python depend_test.py

This test harness performs a series of tests, printing out the expected results of each test before running 'depend.py' to show the actual results.

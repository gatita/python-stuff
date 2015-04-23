#!/usr/bin/env python

#Take a filename and remove all the leading and trailing
#whitespace from each line. 

import io, sys, string

#using map

def clean_file(filename, outfile=None):
    f = io.open(filename).readlines()
    output = map(string.strip, f)
    if not outfile:
        outfile = filename
    outfile = io.open(outfile, 'w')
    for line in output:
        outfile.write(line+'\n')

clean_file('test_file_with_spaces.txt', 'output_test.txt')
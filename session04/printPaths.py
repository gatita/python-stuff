#!/usr/bin/env python
import sys, os

def print_paths():
    file_list = os.listdir(os.getcwd())
    for infile in file_list:
        print os.path.abspath(infile)
    
print_paths()




#!/usr/bin/env python

# Simple script to find file duplicates.
# WIP :D

import os
import sys
import hashlib

def find_duplicates(directory):
    filenumber = 0
    dir_number = 0
    for root, dirs, files in os.walk(directory):
        print "%s with #dirs: %s and #files: %s" % (root, len(dirs),
                                                    len(files))

        already_counted_directory = False

        for filename in files:
            filename = filename.lower()

            if filename.endswith("jpg") or filename.endswith("cr2"):
                filenumber += 1

                if not already_counted_directory:
                    dir_number += 1
                    already_counted_directory = True

    print "total files: %s" % filenumber
    print "total directories: %s" % dir_number


if __name__ == '__main__':
    find_duplicates(sys.argv[1])



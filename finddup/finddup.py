#!/usr/bin/env python

# Simple script to find file duplicates.
# WIP :D

import os
import sys
import hashlib
from collections import defaultdict

import re

IMAGE_REGEX = re.compile("JPG$|CR2$", re.IGNORECASE)

digests = defaultdict(list)

def hash_file(filename):
    with open(filename, 'rb') as handle:
        hasher = hashlib.md5()

        data = handle.read(128)
        while data:
            hasher.update(data)
            data = handle.read(128)

        return hasher.digest()

def find_duplicates(directory):
    filenumber = 0
    dir_number = 0
    for root, dirs, files in os.walk(directory):
        already_counted_directory = False

        for filename in files:
            if IMAGE_REGEX.search(filename):
                filenumber += 1
                print filename

                digest = hash_file(os.path.join(root, filename))

                dirname = os.path.dirname(root)

                if digest in digests:
                    "Oops, file %s already found" % filename
                digests[digest].append((filename, dirname))

                if not already_counted_directory:
                    dir_number += 1
                    already_counted_directory = True

    print "total files: %s" % filenumber
    print "total directories: %s" % dir_number


if __name__ == '__main__':
    find_duplicates(sys.argv[1])



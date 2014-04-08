#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import matplotlib.pyplot as plt

def main():
    with open(sys.argv[1]) as handle:
        for line in handle:
            tokens = line.strip().split()

            pos = tokens[0]
            inscr = tokens[1]
            name = tokens[2]

            if name.startswith("não"):
                print "skipping"
                continue

            time_str = tokens[-1]
            minutes, seconds = map(int, re.split(":|;", time_str))
            time = minutes*60 + seconds
            try:
                age = int(tokens[-2]) # May be the group
            except Exception, e:
                age = int(tokens[-3])

            print age, time



if __name__ == '__main__':
    main()
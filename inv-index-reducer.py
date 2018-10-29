#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator):
    for line in file:
        yield line.rstrip().split(separator, 2)

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator)
    
    for current_word, group in groupby(data, itemgetter(0)):
        fileList = []
        for current_word, fileName, count in group:
            fileList.append('"%s": %s' % (fileName, count))
        print ("%s\t{%s}" % (current_word, ','.join(fileList)))

if __name__ == "__main__":
    main()
#!/usr/bin/python

import sys
import re


for line in sys.stdin:
    # Split document ID and document string
    line = line.strip()
    file_name = line.split('\t')[0]
    document = line.split('\t')[1]
    frequencies = {}
    for bigram in re.findall(r'(?=([!-zA-Z]{2}))', document):
        try:
            frequencies[bigram] += 1
        except KeyError:
            frequencies[bigram] = 1
        
        # Print word frequencies to stdout for ingestion by reducer.
    for bigram in frequencies:
        print ('%s;%s\t%s\t%s' % (bigram, file_name, document, frequencies[bigram]))

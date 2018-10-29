#!/usr/bin/env python

import sys

old_bigram=""
old_file=""
old_sentencedict={}

for input_line in sys.stdin:
  input_line = input_line.strip()
  bigram_plus_file=input_line.split("\t")[0]
  actual_file=bigram_plus_file.split(";")[1]
  actual_bigram=bigram_plus_file.split(";")[0]
  actual_sentencedict=eval(input_line.split("\t")[1])
  if old_bigram==actual_bigram and old_file!=actual_file:
  	combination={(k1,k2):min(v1,v2) for k1,v1 in actual_sentencedict.items() for k2,v2 in old_sentencedict.items()}
  	for pair_of_sentence in combination:
  		print(str(pair_of_sentence)+"\t"+str(combination[pair_of_sentence]))
  old_bigram=actual_bigram
  old_file=actual_file
  old_sentencedict=actual_sentencedict



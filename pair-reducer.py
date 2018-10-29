#!/usr/bin/env python

import sys

old_lines=None
total_score=0
actual_lines=None

for input_line in sys.stdin:
	input_line = input_line.strip()
	actual_lines=eval(input_line.split("\t")[0])
	actual_score=int(input_line.split("\t")[1])
	total_score=total_score+actual_score
	if old_lines!=actual_lines and old_lines!=None:
		jaccard=1-(total_score/(len(old_lines[0])+len(old_lines[1])-2-total_score))
		print(str(old_lines)+"\t"+str(jaccard))
		total_score=0
	old_lines=actual_lines

if old_lines == actual_lines:
	total_score=total_score+actual_score
	jaccard=1-(total_score/(len(old_lines[0])+len(old_lines[1])-2-total_score))
	print(str(old_lines)+"\t"+str(jaccard))
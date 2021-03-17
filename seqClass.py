#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")


if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
#tells you whether the sequence you input is an RNA, DNA, or neither. 
args.seq = args.seq.upper()
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq) and re.search('U', args.seq): #This line checks whether the sequence contains both a T and U
        print('The sequence contains T and U together')
    elif re.search('T', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

# For each nucleotide computes its percentage in the sequence
for nucleotide in ["A","C","G","T","U"]:
    percent = 100*args.seq.count(nucleotide)/len(args.seq)
    if percent > 0:
        print(nucleotide + " " + str(percent) + "%")

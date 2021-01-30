#!/usr/bin/env python

# Task 4 program : Uncommon k-mers

import argparse
import sys
import seqlib

parser = argparse.ArgumentParser(
    description = "Find most and least common k-mers")
parser.add_argument("--file", required=True, help="path to input file")
parser.add_argument("--k", required=False, type=int,
 metavar='<int>', default=3, help="size of kmers, default = 3")
parser.add_argument("--n", required=False, type=int, metavar="<int>",
default=10, help="number of kmers to report")
arg = parser.parse_args()

def uncommon_Kmers():
    file = seqlib.read_fasta(arg.file)
    count = {}
    for name, seq in file: 
        seq = seq.upper()
        for i in range(len(seq)-arg.k+1):
            if seq[i:(i+arg.k)] not in count: 
                count[seq[i:(i+arg.k)]] = 1
            else:
                count[seq[i:(i+arg.k)]] += 1

    sortedKmers = sorted(count, key= count.__getitem__)
    mostKmers = {}
    leastKmers = {}
    for i in range(arg.n):
        leastKmers[sortedKmers[i]] = count[sortedKmers[i]]
        mostKmers[sortedKmers[-i-1]] = count[sortedKmers[-i-1]]
    
    print(f"The most common kmers are {mostKmers}")
    print(f"The least common kmers are {leastKmers}")

    
uncommon_Kmers()

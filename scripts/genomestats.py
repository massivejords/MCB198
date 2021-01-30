#!/usr/bin/env python
# file to calculate stats about a genome

import argparse
import sys
import seqlib

parser = argparse.ArgumentParser(
    description="Dislpays stats about a genome such as N50, GC fraction, and so on... ")
parser.add_argument("--file", required=True, help="the path to the input file")
arg = parser.parse_args()


def genome_stats():
    file = seqlib.read_fasta(arg.file)
    # empty list for the size of each contig
    sizes = []
    # empty dictionary for the counts of each nucleotide (nt) found in the genome
    count = {}

    # adds the sizes of each contig to the list
    # also counts the number of each type of nt found in the genome
    for name, seq in file:
        sizes.append(len(seq))
        # turn all letters to uppercase using .upper()
        seq = seq.upper()
        for nt in seq:
            if nt not in count: count[nt] = 1
            else: count[nt] += 1
    
    # sort the list of contig sizes; largest first, smallest last
    sizes = sorted(sizes, reverse=True)
    min = sizes[-1]
    max= sizes[0]

    # total number of contigs 
    num = len(sizes)
    
    # sum will hold the total number of bases in the genome
    sum = 0
    for length in sizes:
        sum += length
    # avg is the avg length of each contig (total bp over # contigs)
    avg = sum/num
    med = None

    # finding the length of the middle contig 
    # if odd number of contigs, length is just that of middle contig
    if num % 2 == 1:
        med = sizes[int(num/2)]
    # if even number contigs, length is avg of middle 2 contigs 
    else:
        med = (sizes[int(num/2)] + sizes[int(num/2) + 1]) / 2
    
    # the n50 value means that 50% of the genome is in contigs n50 length or longer
    n50 = None
    tot = 0
    # find the n50 by adding contig lengths largest to smallest
    # when your added length is greater than half of the genome length
    # the n50 is the length of the most recently added contig 
    for length in sizes:
        tot += length
        if tot > sum/2:
            n50 = length
            break
    
    print(f'Nucleotide Counts: {count}')
    print(f'Number of contigs: {num}')
    print(f'Min contig length: {min}')
    print(f'Max contig length: {max}')
    print(f'Avg contig length: {avg:.1f}')
    print(f'Median contig length: {med}')
    print(f'N50: {n50}')
    

genome_stats()

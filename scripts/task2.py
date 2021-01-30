#!/usr/bin/env python

import random
import argparse
import sys

parser = argparse.ArgumentParser(
    description="A resequencing genome coverage simulator")
parser.add_argument('--size', required=True, type=int, 
    metavar="<int>", help="size of the genome")
parser.add_argument("--coverage", required=True, type=int,
    metavar="<int>", help="sequencing coverage")
parser.add_argument("--threshold", required=False, type=int, 
    default=1, metavar="<int>", 
    help="the minimum number of reads you want at any given position; default = 1")
arg = parser.parse_args()

def coverage_sim():
    genome = []
    for i in range(arg.size):
        genome.append(0)
    
    for i in range(int(arg.size*arg.coverage)):
        gotcha = random.randint(0, arg.size-1)
        genome[gotcha] += 1
    
    covered=0
    for i in range(arg.size):
        if genome[i] >= arg.threshold:
            covered += 1
    
    print(covered/arg.size,"% of the genome is covered by at least",arg.threshold,"reads.")

coverage_sim()

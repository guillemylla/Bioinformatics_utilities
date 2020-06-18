#!/usr/bin/env python

# Guillem Ylla

## Script that given a list of Old sequence names, creates adds a column with the new names formed by a base name and a consecutive number
### Useful to create a dictioanry to rename large fasta files.
#### For instance, to rename all the scaffoldds/chromosomes/contigs of a genome
#### Firts you extract the old names: grep ">" Genome.fasta | sed 's/>//g'  > Old_Names.txt
#### Then, you use this script to create a name dictionary

## python Create_Names_Dictionary.py Old_Names.txt Dictionary_names.txt

#### With the script Update_Names_usingDictionary you can later use this dictionary to rename  the fasta files, the gff3 files, etc.

##############################
__version__ = '1'

import os, sys
from Bio import SeqIO

newbasename="Scaffold"

def make_names_dict(input, out):

   
    Outfile= open(out, 'w') 
    
    with open(input) as f:
        seq_number=1
        for line in f:
            oldname=line.rstrip()
            Outfile.writelines(oldname+"\t"+newbasename+str(seq_number)+"\n")        
            seq_number+= 1
            
    Outfile.close()  
    
    print >> sys.stderr, "Dictionary done", Outfile.name




if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser("Input Names file")
    parser.add_argument("oldnames_filename", help="Input file name with old names")
    parser.add_argument("Out_filename", help="Output file name")
    
    args = parser.parse_args()

    make_names_dict(args.oldnames_filename, args.Out_filename)

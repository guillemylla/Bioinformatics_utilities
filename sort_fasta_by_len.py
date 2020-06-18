#!/usr/bin/env python


# From Liz Tseng  https://github.com/Magdoll/cDNA_Cupcake/blob/c150d827301048552d874404368c176d3de6c396/sequence/sort_fasta_by_len.py


#pyright (c) 2018, Pacific Biosciences of California, Inc.
#All rights reserved.
#Redistribution and use in source and binary forms, with or without modification, are permitted (subject to the limitations in the disclaimer below) provided that the following conditions are met: 
#    *  Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#    *  Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#    *  Neither the name of Pacific Biosciences nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
#NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY THIS LICENSE. THIS SOFTWARE IS PROVIDED BY PACIFIC BIOSCIENCES AND ITS CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PACIFIC BIOSCIENCES OR ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 

__version__ = '1.0'

import os, sys
from Bio import SeqIO

def sort_by_len(input, reverse):
    if input.endswith('.fasta'):
        output = input[:-6] + '.sorted.fasta'
    elif input.endswith('.fa'):
        output = input[:-3] + '.sorted.fa'
    else:
        print >> sys.stderr, "Input must end with .fasta or .fa! Abort!"
        sys.exit(-1)
    
    with open(input) as f:
        d = SeqIO.to_dict(SeqIO.parse(f, 'fasta'))
    
    keys = d.keys()
    keys.sort(key=lambda x: len(d[x].seq),reverse=reverse)
    
    with open(output, 'w') as f:
        for k in keys: 
            f.write(">{0}\n{1}\n".format(k, d[k].seq))
    
    print >> sys.stderr, "Sorted output printed to", f.name

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser("Sort input fasta file")
    parser.add_argument("fasta_filename", help="Input fasta filename (must end with .fasta or .fa)")
    parser.add_argument("-r", "--reverse", default=False, action="store_true", help="Sort by decreasing length (default: off)")

    args = parser.parse_args()

    sort_by_len(args.fasta_filename, args.reverse)

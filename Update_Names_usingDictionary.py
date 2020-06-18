#!/usr/bin/env python

# Guillem Ylla
## Python script to change the names of any file, based on a dictionary (a file with 2 coulmns: old_name \t new_name)
## The Dictionary can be creaetd with Create_Names_Dictionary.py

## Useful to rename large genome fasta files, gff3 files, etc.


__version__ = '1'

import os, sys, re



Names_dictionary=dict()

def creaet_python_dict(dictionary):
	with open(dictionary) as f:
		for line in f:  
			#print(line)
			old=line.split("\t")[0]    
			new=line.split("\t")[1].rstrip()
			#print(old+"--"+new+"\n")
			Names_dictionary[str(old)]=str(new)
			#print(old+"---->"+ Names_dictionary[old])
			#break
	print >> sys.stderr, "Dictionary processed"

def make_names_dict(input, out):

    Outfile= open(out, 'w') 
    
    with open(input) as f:
        for line in f:
        	if "Contig" in line:
			print("Found : "+line.rstrip())
       		
			for contig in Names_dictionary.keys():
				line = re.sub( r"%s\b" % contig, Names_dictionary[contig], line )#\b indicates word boundary
				newline=line
			print ("New Name : "+ newline)
		else:
			newline=line

		Outfile.writelines(newline)        
            
    Outfile.close()  
    
    print >> sys.stderr, "Done!"




if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser("Input Names file")
    parser.add_argument("filetorename", help="File to rename")
    parser.add_argument("dictionary", help="Dictionary file name")
    parser.add_argument("out", help="Output file name")
    args = parser.parse_args()
    
    
    creaet_python_dict(args.dictionary)
    make_names_dict(args.filetorename, args.out)

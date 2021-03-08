import pandas as pd
import os
import requests
import json
from optparse import OptionParser
import sys

parser = OptionParser()
parser.add_option( "-o","--fileout", dest="pathcsv", default="None", help="[Required] File where to save results'")
parser.add_option( "-i","--taxon_id", dest="Querytaxon", default="None", help="[Required] NSBI Taxon ID to query '")


(options, args) = parser.parse_args()

pathcsv = options.pathcsv
Querytaxon = options.Querytaxon

if pathcsv == "None":
    print("Missing inputs.\n -h for more information")
    sys.exit(1)
    

print("Taxon to query:", Querytaxon)
#Querytaxon=85823#blattaria
baseURL = "https://api.ncbi.nlm.nih.gov/datasets/v1alpha/genome/taxon/"+ str(Querytaxon)


response =requests.get(baseURL)

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

f = open(pathcsv, "w")


#response.json()

jsonresponse=response.json()


line=["sppname", "taxid", "seq_length","estimated_size","submission_date","assembly_level"]
f.write("\t".join(line))
f.write("\n")

for element1 in jsonresponse.items():
 if(element1[0]=="total_count"):
   print("-----\n TOTAL genomes: ",element1[1] )
 if(element1[0]=="assemblies"):
  for element2 in element1[1]:
    #print("element2",element2)
    for element3 in element2["assembly"].items():
     #print("  E3 ", element3, type(element3))
     if (element3[0] == "org"):
      sppname=element3[1]['sci_name']
      taxid= element3[1]['tax_id']
     if (element3[0] == "seq_length"):
      Seqlen=element3[1]
     if (element3[0] == 'submission_date'):
      date=element3[1]
     if (element3[0] == 'assembly_level'):
      level=element3[1]
     if (element3[0] == 'estimated_size'):
      estimated=element3[1]
     if (element3[0] == 'annotation_metadata'):
      element3[1]
    # if (element3[0] == 'annotation_metadata'):
    #  print("  E3 ", element3, type(element3))
    #  print("  E4 ", element3[1]["file"][0]["type"], type(element3))
    #  if(element3[1]["file"][0]["type"] =="GENOME_GFF"):
    #    gff="yes"
    #  else:
     #   gff="no"
     # submissiondate=element3[1]
     # submissiondate=element3[1]
    line=[sppname, taxid, Seqlen,estimated,date,level]
    f.write("\t".join(line))
    f.write("\n")
f.close()



import glob, os

# Guillem ylla January 2019
## Creates a table with the numbers and percentages of mapped and unmapped reads per sample using RSEM log file

outfile = open("Mapping_Summary.txt","w") 

outfile.write('\t'.join(["Sample","Reads","Mapped reads", "p mapped reads","Unmapped too short"]))
outfile.write('\n')

#path="../rsem_output/Austen_EggPolarity/"
path="rsem_output_v2/"
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
  for file in f:
    if '.log' in file: # new version of RSEM changed the filename and lcoation
      samplename=file.split("Log")[0]
      print(samplename)
      with open( os.path.join(r, file)) as f:
        for line in f:
          if "Number of input reads" in line:
            inputreads=line.split("\t")[1].rstrip()
      #print(inputreads)
          if "Uniquely mapped reads number" in line:
            uniqmapped=line.split("\t")[1].rstrip()
      #print(uniqmapped)
          if "Number of reads mapped to multiple loci" in line:
            multiplemapped=line.split("\t")[1].rstrip()
      #print(multiplemapped)
          if "% of reads unmapped: too short " in line:
            tooshort=line.split("\t")[1].rstrip()
        #print(multiplemapped)
      totalmappedreads=(float(uniqmapped)+float(multiplemapped))
      percentmapped=(float(totalmappedreads)/float(inputreads))*100
      percentmappedround= str(round(percentmapped, 2))
      percentmappedtoprint= "".join([percentmappedround,"%"])
  
      outline=[str(samplename),str(inputreads),str(int(totalmappedreads)), percentmappedtoprint ,tooshort]
  
      outfile.write('\t'.join(outline))
      outfile.write('\n')
  break## New version of RSEM only puts log file sto 1st level, no need to go to subdirectroies

outfile.close() 

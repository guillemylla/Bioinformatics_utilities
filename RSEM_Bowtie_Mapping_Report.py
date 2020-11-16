import glob, os, sys

# Guillem ylla January 2019
## Creates a table with the numbers and percentages of mapped and unmapped reads per sample using RSEM log file

## Usage
### RSEM_Mapping_Report.py  Rsem_output_directory/ 
### Will generate the file "Mapping_Summary.txt" on the CWD 



outfilename = sys.argv[-1] # last argument
outfile = open(outfilename,"w") 

path = sys.argv[-2] # last argument


outfile.write('\t'.join(["Sample","Reads","Mapped reads", "p mapped reads","Unmapped too short"]))
outfile.write('\n')



files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
  for file in f:
    if '.log' in file: # new version of RSEM changed the filename and lcoation
      samplename=file.split("Log")[0]
      print(samplename)
      with open( os.path.join(r, file)) as f:
        for line in f:
          if "reads; of these:" in line:
            inputreads=line.split(" ")[0].rstrip()
      #print(inputreads)
          if "aligned concordantly exactly 1 tim" in line:
            uniqmapped=line.split(" ")[4].rstrip()
      #print(uniqmapped)
          if "aligned concordantly >1 times" in line:
            multiplemapped=line.split(" ")[4].rstrip()
      #print(multiplemapped)
          if "aligned concordantly 0 times" in line:
            tooshort=line.split(" ")[4].rstrip()
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

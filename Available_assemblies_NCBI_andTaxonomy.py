import sys
import zipfile
import pandas as pd
from pprint import pprint
from datetime import datetime
from collections import defaultdict, Counter
#from IPython.display import display

#import matplotlib.pyplot as plt
#plt.style.use('ggplot')

try:
    import ncbi.datasets
except ImportError:
    print('ncbi.datasets module not found. To install, run `pip install ncbi-datasets-pylib`.')


## Using NCBI datasets
##https://www.ncbi.nlm.nih.gov/datasets/
##https://hub-binder.mybinder.ovh/user/ncbi-datasets-1vungzql/notebooks/examples/jupyter/ncbi-datasets-pylib/ncbi-datasets-assembly.ipynb

## start an api_instance 
api_instance = ncbi.datasets.GenomeApi(ncbi.datasets.ApiClient())

tax_name = 'crickets'

genome_summary = api_instance.assembly_descriptors_by_taxon(
    taxon=tax_name,
    limit='all')
    
print(f"Number of assemblies in the group '{tax_name}': {genome_summary.total_count}")


print("Acc\tLevel\t#scaf_chr\tdate\trank\tsciname\ttaxid\tseqlen\t")
for assembly in map(lambda d: d.assembly, genome_summary.assemblies):
    print(
        assembly.assembly_accession,
        assembly.assembly_level,
        len(assembly.chromosomes),
        assembly.submission_date,
        assembly.org.rank,
        assembly.org.sci_name,
        assembly.org.tax_id,
        assembly.seq_length,
#        assembly.estimated_size,
#        assembly.annotation_metadata,
        sep='\t')

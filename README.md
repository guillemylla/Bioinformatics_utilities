# Bioinformatics_utilities
Useful scripts to deal with sporadic issues in bioinformatics

- [**Create_Names_Dictionary.py**](Create_Names_Dictionary.py): Given a list of names, adds a new column with new names composed by base name plus an index. Useful to create a names dictionary from fasta files. For example, after sorting contigs/scaffolds by length ([see this script]([https://github.com/Magdoll/cDNA_Cupcake/blob/c150d827301048552d874404368c176d3de6c396/sequence/sort_fasta_by_len.py])), you want to re-name them starting by Scaffold1 to ScaffoldXXX. You can use this script to create a dictionary between Old name and the new name, and then use the **Update_Names_usingDictionary** to use this dictionary to rename all you fasta files, gff3 files, etc.

- [**Update_Names_usingDictionary.py**](Update_Names_usingDictionary.py): Given a dictionary file (can be created with the **Create_Names_Dictionary.py** script ) re-names any file. Ideal to rename Gff3, fasta files, etc. after changing the scaffolds/contigs names.

- [**Create_Names_Dictionary.jl**](Create_Names_Dictionary.jl): Same than before but written in Julia, what makes it much faster.

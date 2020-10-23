#!/bin/sh

for  fastqfile  in  $(ls *.fastq |  grep -v "clean"); do
    printf "\n"
    fname=`echo $fastqfile | sed 's/.fastq//'`
    printf $fname
    fastp --in1 $fastqfile --out1 $fname"_clean.fastq" --qualified_quality_phred 15 --unqualified_percent_limit 40 --length_required 15 --html $fname"_fastp.html"
done;

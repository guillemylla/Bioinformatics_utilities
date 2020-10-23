#!/bin/sh

for  R1  in  $(ls *_1.fastq |  grep -v "clean"); do
    R2=`echo $R1 | sed 's/_1/_2/'`
    printf "\n"
    R1name=`echo $R1 | sed 's/.fastq//'`
    printf "\nRead 1: "$R1
    R2name=`echo $R2 | sed 's/.fastq//'`
    printf "\nRead 2: "$R2


    fastp --in1 $R1 --in2 $R2 --out1 $R1name"_clean.fastq" --out2 $R2name"_clean.fastq" --qualified_quality_phred 15 --unqualified_percent_limit 40 --length_required 15 --html $R1"_fastp.html" --json $R1"_fastp.json"
done;

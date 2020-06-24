# Guillem Ylla

## Julia script to change the names of any file, based on a dictionary (a file with 2 coulmns: old_name \t new_name)
## The Dictionary can be creaetd with Create_Names_Dictionary.py

## Useful to rename large genome fasta files, gff3 files, etc.

## To rename fasta files use option --isFasta yes will make it much faster, since will only check headers

##Usage:
## Fasta
#julia Update_Scaffold_Names_Juliaversion.jl --filetorename input.fa --dictionary Dictionary.txt --out out.fa --isFasta yes
## nay text file
#julia Update_Scaffold_Names_Juliaversion.jl --filetorename input.txt --dictionary Dictionary.txt --out output.txt --isFasta no

# Guillem Ylla
using ArgParse
using FastaIO


######## Fucntion read input parameters
function parse_commandline()
	   s = ArgParseSettings()
	   @add_arg_table! s begin
	       "--filetorename"
	           help = "Input file to rename"
			   required = true
        "--dictionary"
			   help = "Dictionary file"
			   required = true
	 	"--isFasta"
			   help = "yes if it's a fasta file. Will make it faster."
			   required = false
	     "--out","-o"
	          help = "Output file"
	          required = true
	    end

	    return parse_args(s)
end

######## Function create a dictionary

function create_julia_dict(inputdictfile)
	global Names_dictionary=Dict()
	global Names_dictionary_2=()

	open(inputdictfile) do file
	    for ln in eachline(file)
	        #println(split(ln)[1])
			#println(split(ln)[2])
			Names_dictionary[split(ln)[1]]=split(ln)[2]
	    end
		println("Finish reading dictionary")
	end
end



#######
function replacename(contig)
	  newline0=replace(newline, contig*r"\b" => Names_dictionary[contig])
	  return(newline0)
end

####### Read and write
function main_replace(filein, fileout)
	i=1
	open(fileout, "w") do fileout
		open(filein) do file
		    for line in eachline(file)
				global newline=line
				if occursin("Contig", line)
					println("Found :: ",line)
					for contig in keys(Names_dictionary)
					      #println("Check contig ... ", contig )
						  if occursin( contig*r"\b", newline)
						  	newline=replacename(contig)
							break# if replaced, stop trying. To make it faster
						  end
					end
					println("New Name :: ",newline)
					print("\n")
				end
				write(fileout, newline*"\n")
				if i ==10000
					 GC.gc()
					 i=1
				 end
				#i=i	+1
		    end
		end
	end
	close(file)
	close(fileout)
end


################# replace in fasta files
function main_inFasta(filein, fileout)
	#open(fileout, "w") do fileout
	#fastawrite=open(FASTA.Writer, fileout)
	#open(fileout, "w") do fileout
	FastaWriter(fileout) do fastaout
		FastaReader(filein) do rec
			for (desc, seq) in rec
		#fastareader = open(FASTA.Reader, filein)
			#for rec in fastareader
				global newline=desc
				println("Input Sequence :: ", newline)
					for contig in keys(Names_dictionary)
						  if occursin( contig*r"\b", newline)
							newline=replacename(contig)
							break# if replaced, stop trying. To make it faster
						  end
					end

				println("New seq name    :: " , newline)
				writeentry(fastaout, newline, seq)
			end
			close(rec)
		end
		close(fastaout)
	end
end


####### MAIN
function main()
    parsed_args = parse_commandline()
    println("Parsed args:")
    for (arg,val) in parsed_args
        println("  $arg  =>  $val")
    end
	create_julia_dict(parsed_args["dictionary"])
	if !isnothing(parsed_args["isFasta"])
		if lowercase(parsed_args["isFasta"]) == "yes"
			println("FASTA file")
			main_inFasta(parsed_args["filetorename"], parsed_args["out"])
		else
			main_replace(parsed_args["filetorename"], parsed_args["out"])
		end
	else
		main_replace(parsed_args["filetorename"], parsed_args["out"])
	end
	println("Done!!!")
end

main()

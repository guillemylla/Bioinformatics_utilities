# Guillem Ylla

## Julia script to change the names of any file, based on a dictionary (a file with 2 coulmns: old_name \t new_name)
## The Dictionary can be creaetd with Create_Names_Dictionary.py

## Useful to rename large genome fasta files, gff3 files, etc.




using ArgParse

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

####### Rename

function make_names_dict(filein, fileout)
	#i=1
	open(fileout, "w") do fileout
		open(filein) do file
		    for line in eachline(file)
				global newline=line
				if occursin("Contig", line)
					println("Found :: ",line)
					for contig in keys(Names_dictionary)
					      #println("Check contig ... ", contig )
					      global newline=replace(newline, contig*r"\b" => Names_dictionary[contig])
					end
					println("New Name :: ",newline)
				end
				write(fileout, newline*"\n")
				#if i ==10
				#	 break
				 #end
				#i=i	+1
		    end
		end
	end
	close(file)
	close(fileout)
end


####### MAIN
function main()
    parsed_args = parse_commandline()
    println("Parsed args:")
    for (arg,val) in parsed_args
        println("  $arg  =>  $val")
    end
	create_julia_dict(parsed_args["dictionary"])
	make_names_dict(parsed_args["filetorename"], parsed_args["out"])
	println("Done!!!")
end

main()

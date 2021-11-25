#input file
fin = open("data.txt", "rt")
#output file to write the result to
fout = open("out.txt", "wt")
#for each line in the input file
for str in fin:
	#read replace the string and write to output file
	fout.write(str.replace('pyton', 'python'))
#close input and output files
fin.close()
fout.close()

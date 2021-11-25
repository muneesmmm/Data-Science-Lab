#read input file
fin = open("1.txt", "rt")
#read file contents to string
str = fin.read()
#replace all occurrences of the required string
str = str.replace('pyton', 'python')
#close the input file
fin.close()
#open the input file in write mode
fin = open("1.txt", "wt")
#overrite the input file with the resulting data
fin.write(str)
#close the file
fin.close()

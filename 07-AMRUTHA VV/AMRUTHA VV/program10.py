fin = open("program10.txt", "rt")
data = fin.read()
data = data.replace('surya', 'Ammu')
fin.close()
#open the input file in write mode
fin = open("program10.txt", "wt")
#overrite the input file with the resulting data
fin.write(data)
#close the file
fin.close()

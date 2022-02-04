fin = open("pgm10.txt", "rt")
data = fin.read()
data = data.replace('Varsha', 'Ammu')
fin.close()
#open the input file in write mode
fin = open("pgm10.txt", "wt")
#overrite the input file with the resulting data
fin.write(data)
#close the file
fin.close()

fin = open("se.txt", "rt")

data = fin.read()

data = data.replace('anjalii', 'amritha')

fin.close()

fin = open("fi.txt", "wt")

fin.write(data)

fin.close()

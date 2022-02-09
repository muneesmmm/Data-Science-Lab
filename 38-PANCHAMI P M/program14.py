import numpy
def translationM(tx=0,ty=0):
    return numpy.matrix([[1,0,tx],[0,1,ty],[0,0,1]])
matrix=translationM(1,1)
print(matrix)


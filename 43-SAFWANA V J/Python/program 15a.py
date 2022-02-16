import numpy
def translationMatrix(tx=0, ty=0,tz=0):
    return numpy.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[tx,ty,tz,1]])
matrix=translationMatrix(1,1,1)
print(matrix)

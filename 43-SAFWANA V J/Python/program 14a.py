import numpy
def translationMatrix(tx=0, ty=0):
  return numpy.matrix([[1,tx],[0,1]])
matrix=translationMatrix(1,1)
print(matrix)

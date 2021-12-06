import numpy
def translationM(tx=0,ty=0):
    return numpy.matrix([[1,0,tx],[0,1,ty],[0,0,1]])
matrix=translationM(1,1)
print(matrix)
import numpy
def rotationMatrix(degree): 
    theta = numpy.radians(degree)
    c,s=numpy.cos(theta),numpy.sin(theta)
    return numpy.matrix([[c, -s, 0],[s, c, 0],[0, 0, 1]])
matrix=rotationMatrix(30)
print(matrix)

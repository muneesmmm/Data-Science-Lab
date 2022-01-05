import numpy
def rotationMatrix(degree):
    theta = numpy.radians(degree)
    c,s,t=numpy.cos(theta),numpy.sin(theta),numpy.tan(theta)
    return numpy.matrix([[c, -s, 0],[s, c, 0],[0, 0, t]])
matrix=rotationMatrix(30)
print(matrix)

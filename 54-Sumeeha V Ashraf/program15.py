import numpy
def translationMatrix(tx=0, ty=0, tz=0):
    return numpy.matrix([[1,0,0,0],
                         [0,1,0,0],
                         [0,0,1,0],
                         [tx,ty,tz,1]])
matrix=translationMatrix(1,1,2)
print("Translation:")
print(matrix)
def rotationMatrix(degree):
    theta = numpy.radians(degree)
    c,s=numpy.cos(theta),numpy.sin(theta)
    return numpy.matrix([[c,-s,0,0],
                         [s,c,0,0],
                         [0,0,1,0],
                         [0,0,0,1]])
matrix=rotationMatrix(30)
print("\nRotation:")
print(matrix)
def scalingMatrix(sx=0, sy=0, sz=0):
    return numpy.matrix([[sx,0,0,0],
                         [0,sy,0,0],
                         [0,0,sz,0],
                         [0,0,0,1]])
smatrix=scalingMatrix(2,2,2)
print("\nScaling:")
print(smatrix)

import numpy
def translationMatrix(tx=0,ty=0,tz=0):
    return numpy.matrix([[1,0,0,tx],
                        [0,1,0,ty],
                        [0,0,1,tz],
                        [0,0,0,1]])
matrix=translationMatrix(1,1,1)
print("Translation")
print(matrix)
def scalingMatrix(sx=0,sy=0,sz=0):
  return numpy.matrix([[sx,0,0,0],
                       [0,sy,0,0],
                       [0,0,sz,0],
                       [0,0,0,1]])

matrix1=scalingMatrix(2,2,2)
print("Scaling")
print(matrix1)
def rotationMatrix(degree):
  theta = numpy.radians(degree)
  c,s=numpy.cos(theta),numpy.sin(theta)
  return numpy.matrix([[c, -s, 0,0],[s, c, 0,0],[0, 0, 1,0],[0,0,0,1]])
matrix3=rotationMatrix(30)
print("Rotation")
print(matrix3)


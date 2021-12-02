import numpy
#Translation matrix 3D
def translationMatrix(tx=0, ty=0,tz=0):
    return numpy.matrix([[1,0,tx],[0,1,ty],[0,0,tz]])
matrix=translationMatrix(1,1,1)
print(matrix)
#Rotation matrix 3D
#Scaling matrix 3D
def scalingMatrix(sx=0, sy=0,sz=0):
  return numpy.matrix([[sx,0,0],[0,sy,0],[0, 0,sz]])

matrix=scalingMatrix(2,2,2)
print(matrix)

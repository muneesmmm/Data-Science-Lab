import numpy
def scalingMatrix(sx=0, sy=0):
    return numpy.matrix([[sx,0,0],[0,sy,0],[0, 0,1]])
matrix=scalingMatrix(2,2)
print(matrix)

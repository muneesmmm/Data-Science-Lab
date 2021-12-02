import numpy
def scalingMatrix(sx=0, sy=0, sz=0):
    return numpy.matrix([[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]])
matrix=scalingMatrix(2,2,2)
print(matrix)

def rotationMatrix(degree):
    theta = numpy.radians(degree)
    axis=input("Enter the axis(x,y,z) to rotate about: ")
    c,s=numpy.cos(theta),numpy.sin(theta)
    if axis=='x':
        return numpy.matrix([[1,0, 0,0],
                         [0, c,-s,0],
                         [0,s, c,0],
                        [0,0, 0,1]])
    elif axis=='y':
        return numpy.matrix([[c, 0, s,0],
                         [0, 1, 0,0],
                         [-s,0, c,0],
                         [0,0, 0,1]])
    elif axis=='z':
        return numpy.matrix([[c, -s, 0,0],
                         [s, c, 0,0],
                         [0,0, 1,0],
                        [0,0, 0,1]])
    else:
        print("Axis not correct")
matrix=rotationMatrix(30)
print(matrix)

def scalingMatrix(sx=0, sy=0, sz=0):
    return numpy.matrix([[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,1]])
matrix=scalingMatrix(2,2,2)
print(matrix)

import numpy
print("Transalation Matrix")
def translationMatrix(tx=0, ty=0,tz=0):
    return numpy.matrix([[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]])
matrix=translationMatrix(1,1,1)
print(matrix)

print("Rotation in z axis")
def rotationMatrix(degree):
    theta=numpy.radians(degree)
    c=numpy.cos(theta)
    s=numpy.sin(theta)
    return numpy.matrix([[c,-s,0,0],[s,c,0,0],[0,0,1,0],[0,0,0,1]])
matrix=rotationMatrix(30)
print(matrix)

print("Scaling")
def ScalingMatrix(sx=0,sy=0,sz=0):    
    return numpy.matrix([[sx,0,0,0],[0,sy,0,0],[0,0,sz,0],[0,0,0,0]])
matrix=ScalingMatrix(2,2,2)
print(matrix)

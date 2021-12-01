import numpy
x=numpy.array([[1,2,3],[3,4,1],[4,5,6]])
y=numpy.array([[4,3,2],[2,1,0],[2,3,1]])
print("Matrix addition is:")
print(numpy.add(x,y))
print("Matrix subtraction is:")
print(numpy.subtract(x,y))
print("Matrix maultiplication is:")
print(numpy.multiply(x,y))
print("transpose of matrix is:")
print(numpy.transpose(x))
print(numpy.transpose(y))
print("Scalar multiplication is:")
z=2*x
w=2*y
print(z)
print(w)


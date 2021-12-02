
import numpy
matrix1=numpy.matrix([[1,2,3],[4,5,6],[7,8,9]])
matrix2=numpy.matrix([[10,11,12],[13,14,15],[16,17,18]])
#addition
matrix3=numpy.add(matrix1,matrix2)
print("matrix after addition")
print(matrix3)
#substraction
matrix4=numpy.subtract(matrix1,matrix2)
print("matrix after subtraction")
print(matrix4)
#multiplication
matrix5=numpy.matmul(matrix1,matrix2)
print("matrix after multiplication")
print(matrix5)
#scalarmultipliocation
matrix6=2*matrix1
print("matrix1 after scalar multiplication")
print(matrix6)
#transpose
matrix7=numpy.transpose(matrix1)
print("matrix1 after transpose")
print(matrix7)

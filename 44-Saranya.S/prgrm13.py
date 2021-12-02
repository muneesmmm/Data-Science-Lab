import numpy
matrix1=numpy.matrix([[1,2,4],[3,4,1],[5,6,2]])
matrix2=numpy.matrix([[4,3,3],[2,1,6],[6,7,8]])
matrix3=numpy.add(matrix1,matrix2)
print(matrix3)
print("matrix after addition:")
matrix1=numpy.matrix([[2,2,3],[2,2,9],[1,2,1]])
matrix2=numpy.matrix([[1,1,5],[1,1,7],[2,2,6]])
matrix3=numpy.subtract(matrix1,matrix2)
print(matrix3)
print("matrix after subtraction:")
matrix1=numpy.matrix([[2,2,8],[2,2,6],[5,6,7]])
matrix2=numpy.matrix([[1,1,4],[1,1,5],[8,7,3]])
matrix3=numpy.matmul(matrix1,matrix2)
print(matrix3)
print("matrix after multiplication:")
matrix1=numpy.matrix([[2,2,5],[2,2,7],[2,4,6]])
matrix2=2*matrix1
print(matrix2)
print("matrix after scalar multiplication:")
matrix1=numpy.matrix([[1,2,4],[3,4,6],[1,2,3]])
print(matrix1)
matrix2=numpy.transpose(matrix1)
print(matrix2)
print("matrix after transpose:")

import numpy
matrix1=numpy.matrix([[2,2,4],[2,2,6],[3,5,6]])
matrix2=numpy.matrix([[1,1,1],[1,1,4],[3,4,5]])
matrix3=numpy.matmul(matrix1,matrix2)
print(matrix3)
#Matrix substarction
matrix1=numpy.matrix([[2,2,2],[2,2,2],[4,7,8]])
matrix2=numpy.matrix([[1,1,1],[1,1,1],[3,4,5]])
matrix3=numpy.subtract(matrix1,matrix2)
print(matrix3)
#Matrix addition
matrix1=numpy.matrix([[8,6,3],[4 ,5, 6],[7 ,8, 3]])
matrix2=numpy.matrix([[2,5,5],[6,5,5],[3,2,2]])
matrix3=numpy.add(matrix1,matrix2)
print(matrix3)
#Matrix transpose
matrix1=numpy.matrix([[1,2,3],[3,4,1],[1,3,4]])
print(matrix1)
matrix2=numpy.transpose(matrix1)
print(matrix2)
#scalar mulitplication
matrix1=numpy.matrix([[2,2,2],[2,2,2],[1,2,3]])
matrix2=3*matrix1
print(matrix2)
2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Co

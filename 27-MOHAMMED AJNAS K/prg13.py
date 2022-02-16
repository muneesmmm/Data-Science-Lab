import numpy
matrix1=numpy.matrix([[1,2,3],[4,5,6],[7,8,9]])
matrix2=numpy.matrix([[2,2,3],[5,5,6],[10,8,9]])
matrix3=numpy.add(matrix1,matrix2)
matrix4=numpy.subtract(matrix1,matrix2)
matrix5=numpy.matmul(matrix1,matrix2)
matrix6=2*matrix1
matrix7=numpy.transpose(matrix1)
print ("Addition \n",matrix3)
print ("\n subtract \n",matrix4)
print ("\n mul \n",matrix5)
print ("\n scaler mul \n",matrix6)
print ("\n transpose \n",matrix7)

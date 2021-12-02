import numpy
import scipy.linalg
A = matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
u,s,v=svd(A)
print(u)
print(s)
print(v)
Sigma=diag(s)
print(Sigma)
b=numpy.multiply(u,numpy.multiply(s,v))
print(b)

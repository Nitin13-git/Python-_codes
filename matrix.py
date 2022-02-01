def initilising_matrix(dim):
    c=[]
    for i in range(dim):
        c.append([])
    for i in range(dim):
        for j in range(dim):
            c[i].append(0)
    return c
# dot product of matrix
def dot_product(u,v):
    ans=0
    dim=len(u)
    for  i in range (dim):
        ans=ans+u[i]*v[i]
    return ans
# find the row of a matrix
def row_matrix(m,i):
    l=[]
    dim=len(m)
    for j in range(dim):
        l.append(m[i][j])
    return l

def column_matrix(m,j):
    pass
M=[[1,2,3],[4,5,6],[6,7,8]]
print(row_matrix(M,0))

def column_matrix(m,j):
    l=[]
    dim=len(m)
    for i in range(dim):
        l.append(m[i][j])
    return l
print(column_matrix(M,2))


def matrix_mul(M,X): 
    dim=len(M)
    c= initilising_matrix(dim)
   
    for i in range(dim):
        for j in range(dim):
            c[i][j]=c[i][j]+(dot_product(row_matrix(M,i),column_matrix(x,j)))
    return c
x=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix_mul(M,x))
import numpy
X=numpy.mat(M)
y=numpy.mat(x)
b=(X*y)
print(b)
import pandas as pd

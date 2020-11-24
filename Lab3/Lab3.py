import numpy as np
from numpy import inf
import pandas as pd


class myMatrix:
    def __init__(self, N, m):
        self.N = N
        self.m = m

    def getMatrix(self):
        if (N < 4 or N > 7):
            print('Error: *** This dimension is out of bound. The program stops in here.')
            print('******** End of the Program *********')
            exit()
        else:

            mat = self.m[:N, :N]
            if (N * N == mat.size):
                print('The Dimensions match')
            else:

                print('Not enough data in the file as compared to the dimensions provided')
                print(f'The dimensions provided was {N}. So {N}*{N} is {N*N}')
                print(f'And the size of the matrix is {mat.size}')
                print('******** End of the Program *********')
                exit()
            return mat

    def Product(a, b):
        return np.multiply(a, b)

    def dotProduct(a, b):
        return np.dot(a, b)

    def Division(a, b):
        return np.divide(a, b)


f1 = open('File1.txt')
file1 = np.loadtxt('File1.txt', dtype=int)
print('Original Contents of File 1 is:')
print(file1)
print()
f2 = open('File2.txt')
file2 = np.loadtxt('File2.txt', dtype=int)
print('Original Contents of File 2 is:')
print(file2)
print()

N = int(input("Enter the dimension of matrix: "))
print()

m1 = myMatrix(N, file1)
M1 = m1.getMatrix()
print('N*N value is: ',N*N)
print('Matrix 1 Size is:',M1.size)
print()
print('The content of Matrix 1 is:')
print(M1)
print('================================================')
print()

m2 = myMatrix(N, file2)
M2 = m2.getMatrix()
print('N*N value is: ',N*N)
print('Matrix 2 Size is:',M2.size)
print()
print('The content of Matrix 2 is:')
print(M2)
print('================================================')

print()
M1_Multiply_M2 = myMatrix.Product(M1, M2)
print('Product of two matrices matrix1 * matrix2 is:')
print(M1_Multiply_M2)
print('================================================')
print()

M1_DotMultiply_M2 = myMatrix.dotProduct(M1, M2)
print('Dot Product of two matrices matrix1 * matrix2 is:')
print(M1_DotMultiply_M2)
print()
print('================================================')

M1_Divde_M2 = myMatrix.Division(M1, M2)
M1_Divde_M2 = M1_Divde_M2.round(decimals=2)
print('Result of matrix1 divided by matrix 2 (UPTO 2 DECIMAL) is:')
print(M1_Divde_M2)
print('================================================')
print()

Modified_matrix2 = np.where(file2 == [233], 0, file2)
Modified_matrix2 = np.where(file2 == [12620], 0, Modified_matrix2)
Modified_matrix2 = np.where(file2 == [1360], 0, Modified_matrix2)
print('Modified Updated Matrix 2 is:')
print(Modified_matrix2)
new_m2 = myMatrix(N, Modified_matrix2)
M2_new = new_m2.getMatrix()
print()
print('Entered Dimensionswise Modified Matrix2 is: ')
print(M2_new)
print('================================================')
print()
M1_Multiply_M2new = myMatrix.Product(M1, M2_new)
print('Product of two matrices matrix1 * Modified Matrix2 is:')
print(M1_Multiply_M2new)
print('================================================')
print()

M1_DotMultiply_M2new = myMatrix.dotProduct(M1, M2_new)
print('Dot Product of two matrices matrix1 * Modified Matrix2 is:')
print(M1_DotMultiply_M2new)
print()
print('================================================')


M1_Divde_M2new = myMatrix.Division(M1, M2_new)
M1_Divde_M2new = M1_Divde_M2new.round(decimals=2)
M1_Divde_M2new = pd.DataFrame(M1_Divde_M2new)
M1_Divde_M2new[M1_Divde_M2new == inf] = 'undefined'
print('Result of matrix1 divided by Modified Matrix2 (UPTO 2 DECIMAL) is:')
print(M1_Divde_M2new)
print()
print('***********END of PROGRAM************')


import numpy as np
f = open('Data.txt')
print(f.read())

#read data into matrix from file 'Data.txt'
data = np.loadtxt('Data.txt',dtype =int)
print('The original matrix is:')
print(data)
print()

#Select three columns, columns 3, 1, and 9, sort them in ascending order of column 3 and make a matrix of 10 by 3 using these three columns

#selecting 3 columns col 3,1,9
m1 = data[:,[2,0,8]]
print('Matrix 1 (m1) is: (Not sorted)')
print(m1)
print()

#sorting in ascending order of col. 3 from 'data.txt' which is here col=0
col = 0
m1 = m1[np.argsort(m1[:,col])]
print('The sorted version of Matrix1 in ascending order of its first column (column 3 of the original matrix) is:')
print('M1 is: ')
print(m1)
print()
#Select another set of three columns, columns 5, 2, 7, sort them in descending order of column 5 and make a matrix of 10 by 3 using these three columns - Call it matrix2.

#selecting col.5,2,7 from 'data.txt'
m2 = data[:,[4,1,6]]
print('matrix (m2) is: (Not sorted)')
print(m2)
print()

#sorting in descending order of col. 3 from 'data.txt' which is here col=0(1st column of m2)
col = 0
m2 = m2[m2[:,col].argsort()[::-1]]
print('Sorted version of Matrix 2 in descending order of its first column (column 5 of the original matrix) we get:')
print('M2 is:')
print(m2)
print()

#Adding matrices 'm1' and 'm2'
m3 = m1 + m2
print('M3 is: (which is addition of sorted versions of M1 and M2)')
print(m3)
print()

#adding content of each row of matrix 'm3'
m4 = np.sum(m3,axis=1)
m4 = np.vstack(m4)
print('After adding the content of matrix 3 to get the matrix 4 we get:')
print('M4 is: (not sorted)')
print(m4)
print()

#sorting matrix 'm4'
col = 0
m4 = m4[np.argsort(m4[:,col])]
print('Sorted version of M4 in Ascending order: ')
print('M4 is: ')
print(m4)
print()
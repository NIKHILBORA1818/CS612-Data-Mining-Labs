#LAB2
import pandas as pd
import numpy as np

#readthe data from file and we create dataframe first
originalmatrix = pd.read_excel('AlzheimerData.xlsx')
print('Original Matrix is:')
print(originalmatrix)
print()

#remove columns that only include zeros and find matrix M1 for this it's important to find Dataframe first and then matrix
#So, first we create dataframe of m1 with removing columns with all zeros
print("Matrix1 is:")
Matrix1 = originalmatrix.loc[:, (originalmatrix != 0).any(0)]                       #remove the columns that only include Zero
print(Matrix1)
print()

#Now we will find Matrix2 from Matrix1 using pandas

#we used for loop to loop through columns and find columns with 5 junk and columns with less than 5 junks
Matrix1 = Matrix1.fillna('wwq')
for k,col in Matrix1.iteritems():
    c = 0                                #we initialize c=0 to find the count of junk values in columns
    for val in col:
        if val == str(val):
            c+=1
            if c==5:
                print('column with 5 non-numeric value is: ',col.name)
                Matrix1.drop(axis = 1, labels = [col.name],inplace = True)
            else:
                Matrix1 = Matrix1.replace(val,'0')
                global Matrix2
                Matrix2 = Matrix1
print()
print('Matrix2 is: ')
print()
print(Matrix2)
print()

''' Now, as we got dataframe Matrix2 in which we removed columns with 5 junk values and 
replaced junk with zeros for columns with less than 5 junk,
'''

''' Now we need to find rows from Matrix2 which contains 5 junk values but as we already change the junk values to zeros 
at time of finding matrix 1,  Now, here we will find rows which contains 5 zeros '''

for index,row_val in Matrix2.iterrows():
    count = 0
    for i in row_val:
        if i == '0':
            count += 1
            if count == 5:
                print('Rows with 5 zeros: ',row_val.name)
            else:
                Matrix2 = Matrix2.replace(i,0)
                global Matrix3
                Matrix3 = Matrix2
print()
print('Matrix3 is: ')
print()
print(Matrix3)
print()

#Now, we will check mean, std.deviation, minimum and maximim of all X'es
#we store matrix3 in m variable temporary to calculate mean , std of all X'es without 'Y '
m = Matrix3.copy()
del m['Y ']
mean = m.stack().mean()
std = m.stack().std()
print("Mean of all X'es is : ",mean)
print("Standard Deviation of all X'es is : ",std)

min = m.stack().min()
max = m.stack().max()
print("Minimum of all X'es is : ",min)
print("Maximum of all X'es is : ",max)

print()
print('Standardization of matrix3 is below: ')
print()
RescaledMatrix = (Matrix3 - mean) / std
RescaledMatrix['Y '] = Matrix3['Y ']
print(RescaledMatrix)
print()

print('Normalized matrix3 is below : ')
print()
NormalizedMatrix = (Matrix3 - min) / (max - min)
NormalizedMatrix['Y '] = Matrix3['Y ']
print(NormalizedMatrix)

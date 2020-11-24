import pandas as pd
import numpy as np
import xlsxwriter

ori_file = pd.read_excel('MyGamma.xlsx')
print('Original MyGamma file is:')
print(ori_file)
print()
x = len(ori_file.columns)
print('Total no. of columns in Original MyGamma file is', x)
print()
ori_file.replace('na', np.nan, inplace=True)
print()


class Lab4:
    def __init__(self, file):
        self.file = file

    def junkvalues(self):
        self.file.dropna(axis=1, thresh=332, inplace=True)
        self.file.replace(np.nan, 0, inplace=True)
        self.file.replace('^>', 0, inplace=True, regex=True)
        return self.file

    def zeroColumns(a):
        a = a.loc[:, (a != 0).any(axis=0)]
        return a


m1 = Lab4(ori_file)
M1 = m1.junkvalues()
print('Dataframe after deleting more than 200 junks and replacing less than 200 junks with zeros is:')
print(M1)
print()
y = len(M1.columns)
z = x - y
print('Total no. of columns that have more than 200 junks and have been deleted is',z)
print()

M2 = Lab4.zeroColumns(M1)
print('Dataframe after deleting columns with all zeros is:')
print(M2)
print()
w = len(M2.columns)
q = y - w
print('Total no. of columns that sum to zero and have been deleted is: ',q)
print()

ref = M2.copy()

second = ref.copy()
second1 = second[[ref.columns[0],'NAME']]
second1.to_excel('Second.xlsx',index=False)
print()

ref.drop([ref.columns[0],'NAME'], axis=1, inplace=True)

mean = ref.stack().mean()
std = ref.stack().std()
print("Mean of all X'es is : ",mean)
print()
print("Standard Deviation of all X'es is : ",std)
print()

print('Standardization of file or The Rescaled file is below: ')
print()
Rescaledfile = (ref - mean) / std
Rescaledfile['IC50 (nM)'] = ori_file['IC50 (nM)']
co = 'IC50 (nM)'
ff = Rescaledfile.pop(co)

Rescaledfile.insert(0,co,ff)
print(Rescaledfile)
Rescaledfile.to_excel('RescaledFile.xlsx',index=False)

print('Total no. of columns deleted is: ',z+q)
print('Saved Rescaled.xlsx file')


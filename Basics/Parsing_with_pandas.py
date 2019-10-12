import pandas

## reading using read_csv in pandas
df=pandas.read_csv('hrdata.txt')
print(df)

print(type(df['Salary'][0]))
print(type(df['Hire Date'][0]))

df1=pandas.read_csv('hrdata.txt',index_col='Name')  ## use the Name field as the index
print(df1)

df2=pandas.read_csv('hrdata.txt',index_col='Name',parse_dates=['Hire Date'])  ## formating the date correctly
print(df2)
print(type(df2['Hire Date'][0]))

df3=pandas.read_csv('hrdata.txt',index_col='Employee',parse_dates=['Date'],header=0,names=['Employee','Date','Salary','Days'])
# use the user-defined name
print(df3)

## writing using read_csv in pandas
df2.to_csv('hrdata_write.csv')

import numpy as np
hrdata=np.array(df2)
print(hrdata)


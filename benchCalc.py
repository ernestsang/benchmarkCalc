import sys
import os
import pandas as pd


#data = pd.read_csv('TEST_INPUT_EFT.hml', encoding='latin1',
# skiprows=range(0, 18), usecols=range(2, 14))

#data = pd.read_csv('TEST_INPUT_EFT.hml', skiprows=range(0,18), usecols=['CPU Package'])


#getInputFile
df = pd.read_csv('TEST_INPUT_EFT.hml', skiprows=range(0,2),
		 usecols=range(2,14),  encoding='cp1252')

colNames = list(df.columns.values)

newDF = pd.DataFrame(columns=colNames)

#print column names
print(newDF.columns)
print("\n\n")



print("\n\n***End of Processing***")


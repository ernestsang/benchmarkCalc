import sys
import os
import pandas as pd


#data = pd.read_csv('TEST_INPUT_EFT.hml', encoding='latin1',
# skiprows=range(0, 18), usecols=range(2, 14))

#data = pd.read_csv('TEST_INPUT_EFT.hml', skiprows=range(0,18), usecols=['CPU Package'])

columnNames = []

#getInputFile
df = pd.read_csv('TEST_INPUT_EFT.hml', skiprows=range(0,2),
		 usecols=range(2,14),  encoding='cp1252')

print(df)

#get column names
for words in df:
	columnNames.append(words)

print(columnNames)
#newDF = pd.DataFrame(columns =)


print("**End of Processing***")


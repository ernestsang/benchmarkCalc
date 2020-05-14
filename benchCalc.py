import sys
import os
import pandas as pd


		#data = pd.read_csv('TEST_INPUT_EFT.hml', encoding='latin1',
		# skiprows=range(0, 18), usecols=range(2, 14))

		#data = pd.read_csv('TEST_INPUT_EFT.hml', skiprows=range(0,18), usecols=['CPU Package'])


#getInputFile and to trim the first two columms skipping the last two.
#dropping the first two columns with usecols2-14
#encoding helps with utf-8 error Microsoft Windows problem...
df = pd.read_csv('TEST_INPUT_EFT.hml', skiprows=range(0,2),
		 usecols=range(2,14),  encoding='cp1252')

colNames = list(df.columns.values)

		#Did not actually need to create another DataFrame. 
		#Just needed to learn to use iloc and index reset
		#newDF = pd.DataFrame(columns=colNames)

		#print column names
		#print(newDF.columns, "\n") #end new frame idea

		#print dataframe dimensions
		#print(newDF.shape, "\n")

		#stats starts at 15
		#print(df.loc[15])

		#get number of rows in dataframe
		#numOfRow = df.shape[0]

#deletes first 15 rows, reassigns dataframe back into itself
#then with reset_index, reorganizes indices.
df = df.iloc[15:,]

		#prints from 15 and til end of file.
		#print(df.iloc[15:-1])

#resets indices by shuffling
df = df.reset_index(drop=True)

print(df)

print("\n\n***End of Processing***")


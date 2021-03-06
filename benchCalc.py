import sys
import os
import pandas as pd
import math

		#data = pd.read_csv('TEST_INPUT_EFT.hml', encoding='latin1',
		# skiprows=range(0, 18), usecols=range(2, 14))

		#data = pd.read_csv('TEST_INPUT_EFT.hml', skiprows=range(0,18), usecols=['CPU Package'])


		#getInputFile and to trim the first two columms skipping the last two.
		#dropping the first two columns with usecols2-14
		#encoding helps with utf-8 error Microsoft Windows problem...
		#df = pd.read_csv('TEST_INPUT_EFT.hml', skiprows=range(0,2),
		#		 usecols=range(2,14),  encoding='cp1252')
		#used to manually get inputfile.. only use for testing

#get inputfile via command line
inputFile = sys.argv[1]
df = pd.read_csv(inputFile, skiprows=range(0,2), usecols=range(2,14),
	encoding='cp1252')

		#colNames = list(df.columns.values)
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
df = df.iloc[12:,] #12 rows for witcher, 15 for eft

		#prints from 15 and til end of file.
		#print(df.iloc[15:-1])

#resets indices by shuffling 
df = df.reset_index(drop=True)

#converts entire Dataframe to numeric values
df = df.apply(pd.to_numeric)

		#used when testing to see if all NaN's could become zero
		#print("\n\n\n", df.describe(include='all'))

		#change trim column names/scratch that don't need to trim
		#because this below prints values in series position 5 which is Framerate
		#print(df.iloc[:, [5]])
		#df.iloc[:,[5]] #this grabs series in position 5 of column

		#next, select all rows with framerate < 2. drop later

		#figured out how to use drop the rows in position 1-5 ===DONE====
		#df = df.drop(df.index[[0,1,2,3,4,5]])
		#ended up needing this as it was way more complex, not elegant too.

		#iloc[row,column] column will always be 5 since that's where Framerate sits
		#can fix later when i learn how to use strip()

		#if df.iloc[3,5] > 0:
		#	print("yea")

			#for i in len(df):
			#	if df.iloc[i,5] < 0:
			#		print("hea")

		#df = df[df!=0].dropna()

#GOLD
#finally got it, removes all rows that are less than 2
#, in the 5th column which is Framerate
df = df[df.iloc[:,5] > 2]

#reindex from all the 0's again for dropping all NaN's from 0 frames
df = df.reset_index(drop=True)

		#print(df.iloc[247,5]) 
#print(len(df))

#single brackets and double brackets around 5, gives different print out.
#but the values are the same.
print(df.iloc[:,[0]].describe()) #0position for witcher, 5 for eft

print("\n\n\n", df.describe(include='all'))
#resent index ====DONE====
#print(df.head())
#print(df.reset_index(drop=True).head())

#double brackets returns a dataframe
#single bracket returns a series, which is what I need to use in this pgm
#to calculate Low 1% and Low 0.1% FPS
frameRate = df.iloc[:,0] #0position for witcer, 5 for eft

#taking the ceiling function of the 1% of frameRate
numOfOnePercent = math.ceil(len(frameRate) * 0.01)
numOfPointOnePercent = math.ceil(len(frameRate) * 0.001)
#print(numOfOnePercent)

#sortSeries
sortedFPS = frameRate.sort_values()
#print(sortedFPS)

#grab number of 1% values
onePercentSeries = sortedFPS.iloc[0:numOfOnePercent]
#print(onePercentSeries)

#get the 1% 
result = onePercentSeries.sum() / numOfOnePercent
print("\n\nFPS 1% = ", result.round(), ". \n# of lowest FPS values used = ",
 numOfOnePercent)
if(numOfOnePercent < 200):
	print("...you should probably get more data points...")


print("\n\n***End of Processing***")


#================================================
#=============NOTES==============================
#currently this program completely relies on the fact that each 
#column will be at this exact position.
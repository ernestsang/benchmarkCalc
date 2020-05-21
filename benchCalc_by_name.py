import sys
import os
import pandas as pd
import math


#get inputfile via command line
#auto skips first 2 rows and uses the 3rd row which is 
#where the column headers would be on the next row
inputFile = sys.argv[1]
df = pd.read_csv(inputFile, skiprows=range(0,2), usecols=range(2,14),
	encoding='cp1252')

#============================================
#delete unit rows, which is the next 12
df = df.iloc[15:,] #12 rows for witcher, #15 for eft
#needs work to make sure it's dynamic, to skip rows with units
#=========================================

#converts entire Dataframe to numeric values
df = df.apply(pd.to_numeric)

#rename column names without spaces before and after column name
#then assign back into column
df = df.rename(str.strip, axis='columns')

#quick description of dataframe
print(df.describe())

fpsValues = df['Framerate'].sort_values()
fpsValues = fpsValues[fpsValues > 2] #drop all fps values below 2
fpsValues = fpsValues.reset_index(drop=True)#shouldn't need to reset_index twice..

print(fpsValues.describe())

print(fpsValues)

print("\n\n***End of Processing***")


#================================================
#=============NOTES==============================
#currently this program completely relies on the fact that each 
#column will be at this exact position.
import sys
import os
import pandas as pd
import math

FPS_MIN = 2
FPS_MAX = 402 #since CSGO max is 400

#get inputfile via command line
#auto skips first 2 rows and uses the 3rd row which is 
#where the column headers would be on the next row
inputFile = sys.argv[1]
df = pd.read_csv(inputFile, skiprows=range(0,2), usecols=range(2,14),
	encoding='cp1252')

#============================================
#delete unit rows, which is the next 12
df = df.iloc[12:,] #12 rows for witcher, #15 for eft
#needs work to make sure it's dynamic, to skip rows with units
#=========================================

#converts entire Dataframe to numeric values
df = df.apply(pd.to_numeric)

#rename column names without spaces before and after column name
#then assign back into column
df = df.rename(str.strip, axis='columns')

#quick description of dataframe before sorting and deleting, raw dataframe
print(df.describe(), "\n====================================================\n")

fpsValues = df['Framerate'].sort_values()

#store all fpsValues that are above min and below max
fpsValues = fpsValues[(fpsValues > FPS_MIN) & (fpsValues < FPS_MAX)] 

#reset index values that do not meet requirement of FPS_MIN and FPS_MAX
fpsValues = fpsValues.reset_index(drop=True)

print(fpsValues.describe())

#get num of percent lows for 1% and 0.1%
onePercentValues = math.ceil(len(fpsValues) * 0.01) #1% of total values
pointOneValues = math.ceil(len(fpsValues) * 0.001) #0.1% of total values

avgOnePercentFPS = fpsValues.iloc[0:onePercentValues].mean()
avgPointOnePercentFPS = fpsValues.iloc[0:pointOneValues].mean()

print("\n\nFPS 1% lows are = ", avgOnePercentFPS.round())
print("Values used for 1% = ", onePercentValues)

print("\nFPS 0.1% lows are = ", avgPointOnePercentFPS.round())
print("Values used for 0.1% = ", pointOneValues)

if onePercentValues < 200:
	print("...You should probably collect more data points...")


print("\n\n***End of Processing***")


#================================================
#=============NOTES==============================
#with v2, program can now grab framerate from any column
#and calculate values.
#
#
#to do in no particular order
#1. scale to columns entered by user instead of a static 12 or 15.
#
#2. use describe on dataframe after removing fps anomalies >2 && <402
#	like how v1 of benchCalc was able to do
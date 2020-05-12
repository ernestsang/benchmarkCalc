import sys
import os
import pandas as pd


#data = pd.read_csv('TEST_INPUT_EFT.hml', encoding='latin1',
# skiprows=range(0, 18), usecols=range(2, 14))

#data = pd.read_csv('TEST_INPUT_EFT.hml', skiprows=range(0,18), usecols=['CPU Package'])

df = pd.read_csv('TEST_INPUT_EFT.hml', skiprows=range(0,2),
		 usecols=range(2,14), encoding='iso-8859-1')

print(df)



print("**End of Processing***")


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib,pyploit import p
def readCsv(fileName,sep):
    return pd.read_csv(fileName,sep=sep)
bank=readCsv('C:/Users/abdif/OneDrive/Documents/prog/bank-full.csv',';')
def deleteToTestAndTarget():
    y=bank['y']
    y=y[0:len(bank)//2]
    yTest=y[len(bank)//2:len(bank)]
    x=bank.drop(columns=['y'])
    x=x[0:len(bank)//2]
    xTest=x[len(bank)//2:len(bank)]
    return [x,xTest,y,yTest]
def lenearModel(x,xTest,y,yTest):
    x=0

print(x[0:2])
print(y[0:5])
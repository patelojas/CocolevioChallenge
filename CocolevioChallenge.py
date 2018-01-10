import pandas as pd
import itertools as it
import numpy as np

#data given in the format of [Amount, Price] for each company
dictVals = [[1,1],[2, 5],[3, 8],[4, 9],[5,10],[6,17],[7,17],[8, 20],[9, 24],[10,30]]

#Company names used as indices
indexVals = ['A','B','C','D','E','F','G','H','I','J']

#Titles given to the columns
columnVals = ['Amount', 'Price']

#Wanted to read data from CSV but had trouble formatting it correctly with the index so switched to getting data from 
#a dictionary
df = pd.DataFrame(data = dictVals,index=indexVals,columns=columnVals)

#Per Unit column set equal to the per unit cost defined as Amount/Price
df['Per Unit'] = df['Amount'] / df['Price']

#Sort the data frame by Price in descending order
df.sort_values(by='Price', ascending=False, inplace=True)

#inventory is the number of stock given by the vendor
inventory = 21 #21 selected randomly, any number can be used

#companies represents a list of the indices
companies = df.index

#amounts is a series of the different amounts
amounts = df['Amount']

#prices is a series of the different prices
prices = df['Price']

#dictPrices is a dictionary with keys set to the amounts and values set to prices
dictPrices = dict(zip(amounts,prices))

#dictComps is a dictionary with keys set to the amounts and values set to companies
dictComps = dict(zip(amounts, companies))

listVals = [[],[]]

#finds every possible combination of amounts that add up to the inventory and sets that to subset
for L in range(0, len(amounts)+1):
  for subset in it.combinations(amounts, L):
    if sum(subset) == inventory:
        
        #add the subset value that sums to the inventory size
        listVals[0].append(subset)
        
        income = 0
        
        #finds the income based on that subset of clients to sell to 
        for x in subset:
            income += dictPrices[x]
        
        #appends the income from that subset to listVals[1]
        listVals[1].append(income)
        
#ind is the numbered index of the companies that will provide the most income
ind = listVals[1].index(max(listVals[1]))

#command below lists the numbered indices of the companies to sell to
#listVals[0][ind]

print("Companies to sell to:")

#print the companies to sell to
for x in listVals[0][ind]:
    print(dictComps[x])

print("\nIncome: $",max(listVals[1]))


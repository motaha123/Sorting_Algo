"""
Author : Mhd Taha Daboul
Date : 7/27/2023
"""

def selectionSortAsc(listOfNum,size):
    for i in range (0,size-1):
        for j in range (i+1,size-1):
            if(listOfNum[j]<listOfNum[i]):
                listOfNum[i],listOfNum[j] = listOfNum[j],listOfNum[i]


def selectionSortDec(listOfNum,size):
    for i in range (0,size-1):
        for j in range (i+1,size):
            if(listOfNum[j]>listOfNum[i]):
                listOfNum[i],listOfNum[j] = listOfNum[j],listOfNum[i]





listOfNumber = [2,4,3,5,1,6]
print(listOfNumber)

selectionSortAsc(listOfNumber,len(listOfNumber))
print(listOfNumber)

selectionSortDec(listOfNumber,len(listOfNumber))
print(listOfNumber)
"""
Author : Mhd Taha Daboul
Date :  7/27/2023
"""

def bubbleSortAsc(listOfNum,size):
    for i in range (0,size-1):
        for j in range (0,size-i-1):
            if listOfNum[j+1]<listOfNum[j]:
                listOfNum[j],listOfNum[j+1]=listOfNum[j+1],listOfNum[j]

def bubbleSortDec(listOfNum,size):
    for i in range (0,size-1):
        for j in range (0,size-i-1):
            if listOfNum[j+1]>listOfNum[j]:
                listOfNum[j],listOfNum[j+1]=listOfNum[j+1],listOfNum[j]

listOfNumber=[2,4,3,1,6,5]
print(listOfNumber)

bubbleSortAsc(listOfNumber,len(listOfNumber))
print(listOfNumber)

bubbleSortDec(listOfNumber,len(listOfNumber))
print(listOfNumber)
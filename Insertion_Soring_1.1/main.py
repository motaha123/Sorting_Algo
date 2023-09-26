"""
Author : Mhd Taha Daboul
Date : 7/27/23
"""


def insertionAsc(listOfNum,size) :

     for i in range(1,size-1):
        j=i-1
        current = listOfNum[i]

        while(j>=0 and listOfNum[j]>current):
            listOfNum[j+1]=listOfNum[j]
            j-=1

        if j==i-1:
            continue
        else:
            listOfNum[j+1]=current


def insertionDsc(listOfNum, size):
    for i in range(1, size):
        j = i - 1
        current = listOfNum[i]

        while (j >= 0 and listOfNum[j] < current):
            listOfNum[j + 1] = listOfNum[j]
            j -= 1

        if j == i - 1:
            continue
        else:
            listOfNumber[j + 1] = current


listOfNumber = [2, 5, 4, 1, 3, 6]
print(listOfNumber)

insertionAsc(listOfNumber,len(listOfNumber))
print(listOfNumber)

insertionDsc(listOfNumber,len(listOfNumber))
print(listOfNumber)
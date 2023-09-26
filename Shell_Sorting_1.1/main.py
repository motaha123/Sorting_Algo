"""
Author : Mhd Taha Daboul
Date : 7/30/2023
"""
def insertionAsc(listOfNum, size):
    for i in range(1, size):
        j = i - 1
        current = listOfNum[i]

        while (j >= 0 and listOfNum[j] > current):
            listOfNum[j + 1] = listOfNum[j]
            j -= 1

        if j == i - 1:
            continue
        else:
            listOfNum[j + 1] = current

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

def threeElementSorting(listOfNum,lower,mid,upper):
    if listOfNum[mid] >= listOfNum[upper]:
        listOfNum[mid], listOfNum[upper] = listOfNum[upper], listOfNum[mid]
    if listOfNum[lower] >= listOfNum[mid]:
        listOfNum[lower], listOfNum[mid] = listOfNum[mid], listOfNum[lower]

def shellSortingDivid(listOfNum,size,upper,lower):
    mid = int(upper/2)

    if(listOfNum[upper]==listOfNum[len(listOfNum)-1] and listOfNum[lower]==listOfNum[0] ):
        threeElementSorting(listOfNum,lower,mid,upper)

    else:
        if listOfNum[lower] >= listOfNum[mid]:
            listOfNum[lower], listOfNum[mid] = listOfNum[mid], listOfNum[lower]


def shellSortingAsc(listOfNum,size,upper,lower):
    if upper>lower:
        shellSortingDivid(listOfNum,size,upper,lower)
        lower+=1
        upper-=1
        shellSortingAsc(listOfNumber,size,upper,lower)

    else:
        insertionAsc(listOfNum,size)


def shellSortingDsc(listOfNum,size,upper,lower):
    if upper>lower:
        shellSortingDivid(listOfNum,size,lower,upper)
        lower+=1
        upper-=1
        shellSortingDsc(listOfNumber,size,upper,lower)

    else:
        insertionDsc(listOfNum,size)


listOfNumber = [5,4,1,6,8,2,3]
print(listOfNumber)
shellSortingAsc(listOfNumber,len(listOfNumber),len(listOfNumber)-1,0)
print(listOfNumber)
shellSortingDsc(listOfNumber,len(listOfNumber),len(listOfNumber)-1,0)
print(listOfNumber)


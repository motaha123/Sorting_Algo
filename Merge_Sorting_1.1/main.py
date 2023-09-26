"""
Author : Mhd Taha Daboul
Date : 7/30/2023
"""

def mergeSortDivid(listOfNum,lower,mid,upper):
    i=0
    k=0
    j=0
    size1 = mid-lower+1
    size2 = upper-mid
    leftList = [0]*(size1)
    rightList = [0]*(size2)
    for j in range (0,size2):
        rightList[j] = listOfNum[mid+j+1]
    for i in range (0,size1):
        leftList[i] = listOfNum[lower+i]

    i=j=0
    k=lower
    while(i<size1 and j<size2):
        if (leftList[i]>=rightList[j]):
            listOfNum[k]=rightList[j]
            j+=1
        else:
            listOfNum[k] = leftList[i]
            i += 1
        k+=1

    while(j<size2):
        listOfNum[k] = rightList[j]
        j += 1
        k += 1

    while(i<size1):
        listOfNum[k] = leftList[i]
        i += 1
        k+=1




def mergeSort(listOfNum,lower,upper):
    if upper>lower:
        mid=lower + (upper-lower)//2
        mergeSort(listOfNum,lower,mid)
        mergeSort(listOfNum,mid+1,upper)
        mergeSortDivid(listOfNum,lower,mid,upper)


listOfNum = [12, 11, 13, 5, 6, 7]
print(listOfNum)

mergeSort(listOfNum,0,len(listOfNum)-1)
print(listOfNum)
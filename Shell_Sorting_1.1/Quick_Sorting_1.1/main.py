"""
Author : Mhd Taha Daboul
Date : 7/31/2023
"""



def quickSortDivid(listOfNum,left,right):
    pivot = listOfNum[left]
    i = left
    j = right
    while i<j:
        while listOfNum[i] <= pivot and i < right:
            i+=1
        while listOfNum[j] > pivot:
            j-=1
        if i<j:
            listOfNum[i],listOfNum[j]=listOfNum[j],listOfNum[i]
        else:
            break
    if j<i:
        listOfNum[left], listOfNum[j] = listOfNum[j], listOfNum[left]
        return  j

def quickSort(listOfNum,lower,upper):
    if upper>lower:
        lordPivot = quickSortDivid(listOfNum,lower,upper)
        quickSort(listOfNum,lower,lordPivot-1)
        quickSort(listOfNum,lordPivot+1,upper)

listOfNumber = [3,2,4,1,5,7,6,8]
print(listOfNumber)
quickSort(listOfNumber,0,len(listOfNumber)-1)
print(listOfNumber)
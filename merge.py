import time
from numpy.random import randint
import matplotlib.pyplot as plt
def mergeSort(array):
    if len(array)>1:
        r=len(array)//2
        L=array[:r]
        M=array[r:]
        mergeSort(L)
        mergeSort(M)
        i=j=k=0
        while i<len(L) and j<len(M):
            if L[i]<M[j]:
                array[k]=L[i]
                i+=1
            else:
                array[k]=M[j]
                j+=1
            k+=1
        while i<len(L):
            array[k]=L[i]
            i+=1
            k+=1
        while j<len(M):
            array[k]=M[j]
            j+=1
            k+=1
def printlist(array):
    for i in range(len(array)):
        print(array[i],end="")
    print()
array=[6,5,12,10,9,1]
mergeSort(array)
print("Sorted array is:")
printlist(array)
def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            (array[i],array[j])=(array[j],array[i])
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1
def quicksort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)
data=[8,7,2,1,0,9,6]
print("unsorted array:")
print(data)
size=len(data)
quicksort(data,0,size-1)
print('Sorted array in acending order:')
print(data)
def selectionsort(array,size):
    for step in range(size):
        min_idx=step
        for i in range(step+1,size):
            if array[i]<array[min_idx]:
                min_idx=i
        (array[step],array[min_idx])=(array[min_idx],array[step])
def read_input():
    a=[]
    n=int(input("Enter no of tv channels"))
    print("Enter no of viewers")
    for i in range(0,n):
        l=int(input())
        a.append(l)
    return a
elements=list()
times=list()
global labeldata
print("1.MergeSort 2.QuickSort 3.SelectionSort")
ch=int(input("Enter the choice"))
if(ch==1):
    array=read_input()
    mergeSort(array)
    labeldata="MergeSort"
    print('Sorted array is')
    print(array)
if(ch==2):
    array=read_input()
    size=len(array)
    quicksort(array,0,size-1)
    labeldata="Quick Sort"
    print('Sorted array is')
    print(array)
if(ch==3):
    array=read_input()
    size=len(array)
    selectionsort(array,size)
    labeldata="Quick Sort"
    print('Sorted array is')
    print(array)
print("***********Running Time Analysis**********")
for i in range(1,10):
    array=randint(0,1000*i,1000*i)
    start=time.time()
    if ch==1:
        mergeSort(array)
    elif ch==2:
        size=len(array)
        quicksort(array,0,size-1)
    else:
        size=len(array)
        selectionsort(array,size)
    end=time.time()
    print(len(array),"elements sorted by",labeldata,end-start)
    element.append(len(array))
    times.append(end-start)
plt.xlabel('List length')
plt.ylabel('Time complexity')
plt.plot(elements,times,label=labeldata)
plt.grid()
plt.legend()
plt.show()
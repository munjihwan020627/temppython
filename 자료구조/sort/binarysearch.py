import random
from selection_sort import selectionSort



def rBinarySearch(A, key, low, high):
    if(low>high):
        return -1

    mid = (low + high) // 2
    print(A[mid], end=" ")

    if key == A[mid]:
        return mid
    elif key< A[mid]:
        return rBinarySearch(A,key,low,mid-1)
    elif key> A[mid]:
        return rBinarySearch(A,key,mid + 1,high)




def iBinarySearch(A,key):
    low = 0
    high = len(A)

    while(low<= high):
        mid = (low + high) // 2
        print(A[mid], end=" ")

        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        elif key > A[mid]:
            low = mid + 1

if __name__ == "__main__":

    A = []

    for i in range(15):
        A.append(random.randint(1,15))



        selectionSort(A)


    key = int(input("Input search key: "))

    print("rBinarysearch : %d" %rBinarySearch(A,key,1, 15))
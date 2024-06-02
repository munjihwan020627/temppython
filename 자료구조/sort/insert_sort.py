def printStep(L, index):
    print("        step %d : " %index, end= "")
    print(L)



def insertionSort(L):

    n = len(L)
    for i in range(1,n):
        key = L[i]
        j = i - 1
        while j>= 0 and L[j] > key:
            L[j+1] = L[j]
            j -= 1
        L[j + 1] = key
        printStep(L , i)




if __name__ == "__main__":
    data = [5,3, 8, 4,9,1,6,2,7]
    L = list(data)

    print("Before :", L)
    insertionSort(L)

    print("Selection :", L)
    print()

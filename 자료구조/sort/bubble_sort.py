def printStep(L, index):
    print("        step %d : " %index, end= "")
    print(L)



def bubbleSort(L):

    n = len(L)
    for i in range(n-1,0,-1):
        bChanged = False
        for j in range(i):
            if L[j] > L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
                bChanged = True

        if not bChanged: break;
        printStep(L, n- i)

if __name__ == "__main__":
    data = [5,3, 8, 4,9,1,6,2,7]
    L = list(data)

    print("Before :", L)
    bubbleSort(L)

    print("Selection :", L)
    print()

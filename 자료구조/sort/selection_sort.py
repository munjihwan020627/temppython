def printStep(L, index):
    print("        step %d : " %index, end= "")
    print(L)

def selectionSort(L):
    n = len(L)
    for i in range(n- 1):
        least = i
        for j in range(i + 1,n):
            if (L[j] < L[least]):
                least = j

        L[i],L[least] = L[least], L[i]
        printStep(L, i+1)



if __name__ == "__main__":
    data = [5,3, 8, 4,9,1,6,2,7]
    L = list(data)

    print("Before :", L)
    selectionSort(L)

    print("Selection :", L)
    print()


    """ 
    
    ex) 5와 1 사이에 5가 있다면 안정성에 문제가 생김
    why? -> 기존에 있던 5가 1이 있던 인덱스로 움직이기 때문에
    두번째로 존재하던 5가 먼저 연산에 참여해 안정성이 깨짐
    
    """
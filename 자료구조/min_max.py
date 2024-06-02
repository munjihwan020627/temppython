def FindMinMax(A): # 교수님은 단어의첫번째는 대문자,띄어쓰기나 언더바보단 이런 방식을 사용함

    min = A[0]
    max = A[0]
    for i in range(len(A)):
        if max < A[i] : max = A[i]
        if min > A[i] : min = A[i]
    return max,min


Data = [1, 3, 5, 7, 9, 11, 2, 5, 7, 6]

x,y = FindMinMax(Data)
print("max,min = (%d, %d)" % (x,y))

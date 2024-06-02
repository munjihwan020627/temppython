def SumRange(begin, end, step = 1):
    sum = 0
    for n in range(begin, end, step):
        sum += n


    return sum


if __name__ == "__main__":           #main함수일시 실
    print('sum = ', SumRange(1, 10))
    print('sum = ', SumRange(1, 10, 2))
    print('sum = ', SumRange(step = 3, end = 10, begin = 1))












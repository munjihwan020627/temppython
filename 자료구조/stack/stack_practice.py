
def rFact(n):
    if n == 1:
        return 1
    else:
        return n * rFact(n-1)


def iFact(n):
    result = 1
    for k in range(1,n+1):
        result = result * k
    return result

print("%d,%d" %(iFact(5),rFact(5)))
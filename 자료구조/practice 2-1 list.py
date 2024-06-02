L1 = [ 3, 5, 7, 9]
L2 = ['A', "B", "C", "D"]

for e in L1:
    print(e ,end = "")
print("\n")
print(L1[2])
L2[1] = L1[-1]

print(L2)

L1.append(11)

print(L1)

print(L1.pop())


#pop은 인덱스를 지정해주지 않을시 맨 마지막 인덱스가 튀어나옴

print(L1)


L2.extend(L1)
print(L2)
print(L1)

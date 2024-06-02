

def contains(bag,e):
    return e in bag


def insert(bag,e):
    bag.append(e)

def remove(bag,e):
    if contains(bag,e):
        bag.remove(e)


def printing(bag):
    print(bag)

def bagLen(bag):
    return len(bag)





Jihwan = []
insert(Jihwan,1)
insert(Jihwan,2)
insert(Jihwan,3)
insert(Jihwan,4)
insert(Jihwan,5)
insert(Jihwan,6)

printing(Jihwan)

remove(Jihwan,1)

print("가방속 물건의 개수는?", (bagLen(Jihwan)),"개 입니다")
printing(Jihwan)
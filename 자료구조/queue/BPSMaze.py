#너비 우선 탐색(BPS)

from CircularQueue import CircularQueue


map = [
    ['1','1','1','1','1','1'],
    ['e','0','1','0','0','1'],
    ['1','0','0','0','1','1'],
    ['1','0','1','0','1','1'],
    ['1','0','1','0','0','x'],
    ['1','1','1','1','1','1']
]

SIZE = 6

def isValidPos(x,y):

    if 0 <= x < SIZE and 0 <= y < SIZE:
        if map[x][y] =='0' or map[x][y] =='x':
            return True

    return False


def BFS():
    Q = CircularQueue(100)
    Q.enqueue((1,0))
    print('BFS : ')

    while not Q.isEmpty():
        pos = Q.dequeue()
        print(pos, end= ' -> ')

        (x , y) = pos

        if (map[x][y] == "x"):
            return True

        else:
            map[x][y] = '.'
            if isValidPos(x - 1, y): Q.enqueue((x - 1, y))
            if isValidPos(x + 1, y): Q.enqueue((x + 1, y))
            if isValidPos(x, y - 1): Q.enqueue((x, y - 1))
            if isValidPos(x, y + 1): Q.enqueue((x, y + 1))

        Q.display2()

    return False








if __name__ == "__main__":
    result = BFS()
    if result:
        print("SUCCESS")

    else:
        print("FAIL")







#상속한 class의 method를 불러와서 사용하려면? -> 클래스명(길이) 를 함수안에 한번 호출해서 사용해야함





#주의사항
"""
10시 20분까지는 타 시험중이니 정숙 유지

30분에 시험 예정

시험은 15분 후에는 입장 불가

필기시험 + 코테로 만들어짐

소스코드를 text파일로 만들어서 제출
-> 메모장으로 만들어라


"""
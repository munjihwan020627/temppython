#깊이 우선 탐색 (DFS)

from ArrayStack import Stack

map = [
    ['1','1','1','1','1','1'],
    ['e','0','0','0','0','1'],
    ['1','0','1','0','1','1'],
    ['1','1','1','0','0','x'],
    ['1','1','1','0','1','1'],
    ['1','1','1','1','1','1']
]

SIZE = 6

def isValidPos(x,y):

    if 0 <= x < SIZE and 0 <= y < SIZE:
        if map[x][y] =='0' or map[x][y] =='x':
            return True

    return False

def DFS():
    print('DFS: ')
    S = Stack(100)
    S.push((1,0))

    while not S.isEmpty():
        pos = S.pop()
        print(pos, end= ' -> ')

        (x,y) = pos
        if(map[x][y] == "x"):
            return True

        else:
            map[x][y] = '.'
            if isValidPos(x - 1, y): S.push((x - 1, y))
            if isValidPos(x + 1, y): S.push((x + 1, y))
            if isValidPos(x, y - 1): S.push((x , y - 1))
            if isValidPos(x, y + 1): S.push((x, y + 1))

            #elif로 구성하지 않은 이유는 1번째 열이 아니고 2번째 열이 true일때 3~4번째를 확인하지않고 지나가기에 모든 길을 push하지 않아서

            S.display()

    return False



if __name__== "__main__":
    result = DFS()
    if result:
        print("SUCCESS")

    else:
        print("FAIL")
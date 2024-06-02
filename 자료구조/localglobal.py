pi = 3.141592
perimeter = 0

def Calc_perimeter(radius):
    print('Pi :', pi)                   #pi는 전역변수여도 출력이 된다??? -> pi라는 변수에 변경이 일어나지 않고 그냥 호출된것이기 때문
    global perimeter
    perimeter = 2 * radius * pi      #perimeter는 대입연산자의 왼쪽에 있기 때문에 새로 지정한것으로 규정하여 pi랑 다른 결과가 나옴 (외부에서 처리된 변수를 불러오는것은 가능하지만 변수의 값을 변경하거나 새로 지정할 수는 없다)
    return perimeter


if __name__ == "__main__":
    Calc_perimeter(10)
    print(perimeter)
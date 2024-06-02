class Car: #class의 지정시 변수의 가장 첫글자는 대문자로 구현

    def __init__(self, color, speed = 0):   #멤버변수의 이름과 같게 구현하는게 일반적임
        self.color = color
        self.speed = speed


    def SpeedUp(self):
        self.speed += 10

    def SpeedDown(self):
        self.speed -= 10

    def isEqual(self, other):
        if self.color == other.color:
            return True
        else: return False

    def __eq__(self, other):
        return "Yes" if self.color == other.color else "No"

    def __str__(self):
        return "Color: %s, Speed: %d" % (self.color,self.speed)

    def __ge__(self, other):
        return "faster" if self.speed > other.speed else "slower"







if __name__ == "__main__":
    car1 = Car("Black")
    car2 = Car("Red",100)
    car3 = Car("Red")
    car4 = Car("Yellow")


    print("Color : %s - Speed  : %d" %(car1.color,car1.speed))
    print("Color : %s - Speed  : %d" %(car2.color,car2.speed))
    print("Color : %s - Speed  : %d" %(car3.color,car3.speed))
    print("Color : %s - Speed  : %d" %(car4.color,car4.speed))


    car1.SpeedUp()
    car2.SpeedDown()

    print("Color : %s - Speed  : %d" % (car1.color, car1.speed))
    print("Color : %s - Speed  : %d" % (car2.color, car2.speed))

    print(car2.isEqual(car4))
    print(car2 == car4)
    print(car1) #를 하면 어느 객체로 만들어져서 어디 메모리에 저장되어 있는지만 표현함 (사람이 저 정보로 객체 내부의 내용을 유추할 수 없음) but __str__ 함수를 이용해 각각의 객체정보를 출력하게 만들 수 있음
    # -> 하지만 이번 수업에서는 display 함수를 쓸 가능성이 높음

    print(car1 >= car3)



    #각 클래스 객체에 접근시 변수.???라는 형태로 호출하여 수행함









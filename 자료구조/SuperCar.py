from car import Car


class SuperCar(Car):

    def __init__(self, color, speed = 0, bTurbo = True):
        super().__init__(color,speed)       # 가장 중요(super를 통해 부모 클래스의 내용을 복사해와야함)
        self.bTurbo = bTurbo

    def setTerbo(self):
        self.bTurbo = bTurbo

    def SpeedUp(self):
        if self.bTurbo:
            self.speed += 50
        else:
            super().Speedup()


    def __str__(self):
        if self.bTurbo:
            return '[%s][speed = %s] Turbo' % (self.color, self.speed)
        else:
            return '[%s][speed = %s] Normal' % (self.color, self.speed)



if __name__ == "__main__":
    s1 = SuperCar("Gold")
    s2 = SuperCar("Silver", 50, False)
    print(s1); print(s2)
    s1.SpeedUp()
    s2.SpeedUp()
    print(s1); print(s2)





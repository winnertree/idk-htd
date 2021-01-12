class Unit:
    def __init__(self):
        print("creat Unit")

class Flyable:
    def __init__(self):
        print("creat Flyable")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        #super().__init__() #다중 상속의 경우 맨 앞에것만 상속됨
        Unit.__init__(self)
        Flyable.__init__(self)

dropship=FlyableUnit()
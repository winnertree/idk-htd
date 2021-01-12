#메소드 오버라이딩
class Unit: #부모 클래스
    def __init__(self, name, hp, speed):
         self.name=name
         self.hp=hp
         self.speed= speed
    def move(self,location):
        print("지상 유닛 이동")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name,location,self.speed))

class AttackUnit(Unit): #자식 클래스
    def __init__(self, name, hp, speed ,damage):
        Unit.__init__(self,name,hp,speed)
        self.damage=damage
    def attack(self, location):
        print("{0} : {1}방향으로 공격 {2}damage".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} damaged".format(self.name,damage))
        self.hp-=damage
        print("{0} : now hp {1}".format(self.name,self.hp))
        if self.hp<=0:
            print("{0} destroyed".format(self.name))

class Flyable: # 날 수 있는 기능을 가진 클래스
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0}이 {1}로 날아갑니다. [속도 : {2}]".format(name,location,self.flying_speed))

class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0 ,damage) #지상 speed 0
        Flyable.__init__(self,flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name,location)

#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self,name,hp, 0)
        super().__init__(name,hp, 0)
        self.location=location

#서플라이
supply_depot=BuildingUnit("서플라이", 500, "7시")


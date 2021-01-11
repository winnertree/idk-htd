#다중 상속
class Unit: #부모 클래스
    def __init__(self, name, hp):
         self.name=name
         self.hp=hp

class AttackUnit(Unit): #자식 클래스
    def __init__(self, name, hp, damage):
        Unit.__init__(self,name,hp)
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
        AttackUnit.__init__(self,name,hp,damage)
        Flyable.__init__(self,flying_speed)

valkyrie=FlyableAttackUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name,"10시")
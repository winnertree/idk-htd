#상속
class Unit:
    def __init__(self, name, hp):
         self.name=name
         self.hp=hp

class AttackUnit(Unit):
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

firebat1 =AttackUnit("firebat", 50 ,16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)
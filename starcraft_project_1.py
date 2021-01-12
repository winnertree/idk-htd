#스타크래프트 게임 프로젝트
from random import *

class Unit: #부모 클래스
    def __init__(self, name, hp, speed):
        self.name=name
        self.hp=hp
        self.speed= speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self,location):
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name,location,self.speed))

    def damaged(self, damage):
        print("{0} : {1} damaged".format(self.name,damage))
        self.hp-=damage
        print("{0} : now hp {1}".format(self.name,self.hp))
        if self.hp<=0:
            print("{0} destroyed".format(self.name))

class AttackUnit(Unit): #자식 클래스
    def __init__(self, name, hp, speed ,damage):
        Unit.__init__(self,name,hp,speed)
        self.damage=damage
    def attack(self, location):
        print("{0} : {1}방향으로 공격 {2}damage".format(self.name, location, self.damage))

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)
    #스팀팩
    def stimpack(self):
        if self.hp>10:
            self.hp-=10
            print("{0} : 스핌팩을 사용합니다. (HP 10감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스핌팩을 사용하지 않습니다.".format(self.name))

class Tank(AttackUnit):
    seize_developed = False
    def __init__(self):
        AttackUnit.__init__(self, "탱크" , 150, 1, 25)
        self.seize_mood=False
    def set_seize_mood(self):
        if Tank.seize_developed ==False:
            return

        #현재 시즈모드가 아닐때 -> 시즈모드
        if self.seize_mood==False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage*=2
            self.seize_mood=True

        #현재 시즈모드 일때 ->시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mood = False

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
        self.fly(self.name,location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False #클로킹 해제 상태
    def clocking(self):
        if self.clocked==True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked=False
        else:
            print("{0} : 클로킹 모드 실행합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

#실제 게임 시작
game_start()

#마린 3마리
m1=Marine()
m2=Marine()
m3=Marine()

#탱크 2마리
t1=Tank()
t2=Tank()

#레이스 1마리
w1=Wraith()

#유닛 일괄 관리
attack_units=[]
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

#탱크 시즈모드 개발
Tank.seize_developed=True
print("[일림] 탱크 시즈 모드 개발이 완료되었습니다.")

#공격 모드 준비 (탱크 : 시즈모드, 레이스 : 클로킹, 마린 : 스팀팩)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mood()
    elif isinstance(unit, Wraith):
        unit.clocking()

#전군 공격
for unit in attack_units:
    unit.attack("1시")

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21)) #공격을 랜덤으로 받음 (5~20)

#게임 종료
game_over()
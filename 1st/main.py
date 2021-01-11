#**은 ^
#//은 몫
#true false 10>3
# abs() 는 절댓값
# pow(4,2) 는 4^2
#max(a,b) , min(a,b)
# round(3.13) 반올림

# from math import *
# print(floor(4.99)) #내림
# print(ceil(3.14)) # 올림
# print(sqrt(16)) #제곱근

# from random import *
# print(random()) #0.0 ~ 1.0 사이의 임의의 값 생성
# print(random()*10) #0.0~10.0
# print(int(random()*10))
#
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
# print(int(random()*45)+1)
#
# print(randrange(1,46)) # 1~46 미만의 임의의 값 생성
# print(randint(1,45))

#월 4회 3번 온라인 1번은 오프라인

# from random import *
# date = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월", date, "일로 선정되었습니다.")

# sentence = '이건 뭘까요?'
# sentence2 = "이건 뭘까요?"
# sentence3 = """이건 뭘까요? 알아맞춰 보세요"""
# print(sentence + "\n" + sentence2+ "\n" + sentence3)

#슬라이싱
# jumin = "980654-1234567"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) #0부터 2직전까지
# print("월 : " + jumin[2:4])
# print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) #맨 뒤에서 7부터 끝까지

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))
# print(python)
#
# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)
#
# print(python.find("Java")) # 없으면 -1출력하고 계속 코드 돌아감
# print(python.index("Java")) # 없으면 에러남
#
# print(python.count("n"))

#문자열 포멧
# print("나는 %d살입니다" %20)
# print("나는 %s을 좋아해요" %"파이썬")
# print("Apple 은 %c로 시작해요" %"A")
# print("나는 %s색과 %s색을 좋아해요" %("파란", "빨간"))
# print("나는 {}살입니다".format(20))
# print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요" .format("파란", "빨간"))
#print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color="빨간"))

# age = 20
# color = "빨강"
# print(f"나는 {age}살이며, {color}색을 좋아해요")

#탈출문자
# print("백문이 불여일견 \n백견이 불여일타")
#
# print('저는 "이것저것"입니다')
# print("저는 \"이것저것\"입니다")
#
# print("\\")
#
# print("Red Apple\rPine") #Pine Apple
#
# print("Redd\bApple") #한글자 삭제(백스페이스)
#
# print("Red\tApple")

#사이트별로 비밀번호 만들어주는 프로그램
# url = "http://google.com"
# my_str = url.replace("http://", "")
# my_str=my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) +str(my_str.count("e")) + "!"
# print("{} 의 비밀번호는 {} 입니다.".format(url,password))

#리스트 []
# subway = ["유재석","조세호","박명수"]
# print(subway.index("박명수"))
#
# subway.append("하하") #맨뒤에 삽입
# print(subway)
#
# subway.insert(1,"정형돈") #중간에 삽입
# print(subway)
#
# print(subway.pop()) #뒤에서부터 뻄
# print(subway)

# subway = ["유재석","조세호","박명수"]
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

#리스트 정렬
# num_list=[5,3,4,1,2]
# num_list.sort() #정렬
# print(num_list)
#
# num_list.reverse() #뒤집기
# print(num_list)
#
# num_list.clear()
# print(num_list)

#다양한 자료형과 함께 사용 가능
# list=["조세호", 200 , True]
# num_list=[5,3,4,1,2]
# print(list)
#
# num_list.extend(list)
# print(num_list)

#사전 (key/value)
# cabinet={3:"유재석", 100:"김태호"} #key = 3, value = 유재석
# print(cabinet[3])
# print(cabinet[100])
# print(cabinet.get(3))
# print(cabinet.get(5))
# print(cabinet[5])
# print(cabinet.get(5, "사용 가능"))

# print(3 in cabinet)
# print(5 in cabinet)

# cabinet={"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])
#
# print(cabinet)
# cabinet["C-20"] = "조세호"
# print(cabinet)
#
# del cabinet["A-3"]
# print(cabinet)
#
# print(cabinet.keys())
#
# print(cabinet.values())
#
# print(cabinet.items())
#
# cabinet.clear()
# print(cabinet)

#리스트 [] // 사전 {:} // 튜플 () // 집합{}

#튜플 // 변경되지 않는 값들들, 늘릴수없음
# menu=("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])
#
# name,age,hobby=("김종국",20,"코딩")
# print(name,age,hobby)

#집합 // 중복 안됨, 순서 없음
# my_set={1,2,3,3,3}
# print(my_set)
#
# java={"A","B","C"}
# python=set(["A","D"])
#
# print(java&python) # 교집합
# print(java.intersection(python)) # 교집합
#
# print(java | python)
# print(java.union(python)) # 합집합
#
# print(java-python)
# print(java.difference(python)) # 차집합
#
# python.add("B")
# print(python)
#
# java.remove("B")
# print(java)

#자료구조의 변경
# menu={"커피", "우유", "주스"}
# print(menu, type(menu))
#
# menu=list(menu)
# print(menu, type(menu))

#quiz
# from random import *
# a=range(1,21) # 1부터 20까지 숫자를 생성 // range타입
# a= list(a)
# shuffle(a)
# winners = sample(a, 4)
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자  : {0}".format(winners[1:]))

#if
# weather = input("오늘 날씨? ")
# if weather == "비" or weather =="눈":
#     print("우산")
# elif weather == "미세":
#     print("마스크")
# else:
#     print("nothing")

# temp = int(input("온도? "))
# if 30<= temp:
#     print("덥다")
# elif 10<= temp:
#     print("good weather")
# else:
#     print("cold")

#for
# for i in range(5): #0~4
#     print("the number of waiting : {0}".format(i))
# for i in range(1,6):  # 1~5
#     print("the number of waiting : {0}".format(i))

# coffe = ["a","b","c"]
# for i in coffe:
#     print("{0} ready!".format(i))

#while
# customer="A"
# index=5
# while index>=1:
#     print("{0}, ready!{1}left".format(customer, index))
#     index-=1

# customer="A"
# while True:
#     print("{0}, ready!left".format(customer))

# customer="A"
# person = "unknown"
# while person!=customer:
#     print("{0}, ready!left".format(customer))
#     person = input("whats your name? ")

#continue / break
# absent = [2,5]
# no_book=[7]
# for student in range(1,11):
#     if student in absent:
#         continue #바로 다음 반복으로
#     elif student in no_book:
#         print("you better run! {0} follow me".format(student))
#         break #반복문 바로 탈출
#     print("{0} read the book".format(student))

#한줄 for문
#출석번호 1,2,3,4 -> 앞에 100을 붙이기로함 ->101,102,103,104
# student =[1,2,3,4,5]
# student = [i+100 for i in student]
# print(student)
#
# #학생 이름을 길이로 변환
# student = ["apple", "banana", "coffee"]
# student = [len(i) for i in student]
# print(student)
#
# #학생 이름을 대문자로 변환
# student = ["apple", "banana", "coffee"]
# student = [i.upper() for i in student]
# print(student)

#quiz
# from random import *
# cnt=0
# for i in range(5,51):
#     time = randint(1,50)
#     if(time>=5 and time <=15):
#         print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt+=1
#     else:
#         print("[] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
# print("the sum of customers : {0}".format(cnt))

#함수
# def oepn_account():
#     print("new account create")
#
# def deposit(balance, money):
#     print("입금 완료. 잔액 {0} 원".format(balance+money))
#     return balance+money
#
# def withdraw(balance, money):
#     if(balance<money):
#         print("출금안되")
#         return balance
#     else:
#         print("잔액 {0}원 입니다".format(balance-money))
#         return balance - money
#
# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance-money-commission
# balance=0
# balance = deposit(balance, 1000)
# print(balance)
# balance = withdraw(balance, 2000)
# print(balance)
# commission , balance = withdraw_night(balance, 500)
# print("commission = {0}, balance = {1}".format(commission,balance))

#기본값
# def profile(name,age,main_lang):
#     print("name : {0}\tage : {1}\tlan : {2}".format(name,age,main_lang))
# profile("a",20,"A")
# profile("b",25,"B")

# def profile(name,age=17,main_lang="A"):
#      print("name : {0}\tage : {1}\tlan : {2}".format(name,age,main_lang))
# profile("A")
# profile("B")

#키워드값
# def profile(name,age,main_lang):
#      print(name,age,main_lang)
#
# profile(name = "A", main_lang="B", age=15) #순서 바껴도 상관없음

#가변인자 // *로 나타내는 인자
# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("name : {0}\tage : {1}\t".format(name,age), end=" ")#end=" "쓰면 이어서 출력
#     print(lang1,lang2,lang3,lang4,lang5)
#
# profile("A",20,"A","B","C","D","E")
# profile("A",15,"A","B","C","","")

# def profile(name,age,*lang):
#     print("name : {0}\tage : {1}\t".format(name,age), end=" ")#end=" "쓰면 이어서 출력
#     for i in lang:
#         print(i, end=" ")
#     print()
# profile("A",20,"A","B","C","D","E","F")
# profile("A",15,"A","B","C")

#지역변수와 전역변수
# gun = 10
# def checkpoint(soldiers):
#     global gun #전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("the sum of guns : {0}".format(gun))
# checkpoint(2)
# print("{}".format(gun))

#quiz
# def std_weight(height, gender):
#     if gender == "man":
#         print("height {0}cm man's middle weight is {1}kg.".format(height,round((height*0.01)**2*22,2)))
#     else:
#         print("height {0}cm woman's middle weight is {1}kg.".format(height,(height*0.01)**2*21))
# std_weight(175, "man")

#표준 입출력
# print("A","B","C", sep=" vs ") #sep로 사이에 뭐 넣을지 정함
# print("A"+"B")
# print("A","B", sep=",", end="? ") #end로 문장의 끝부분을 정할수있음
# print("what is better?")
#
# import sys
# print("A","B", file=sys.stdout) #표준 출력으로 처리
# print("A","B", file=sys.stderr) #표준 애러로 처리
#
# score = {"A":0, "B":50, "C":100} #dictionary
# for subject,scores in score.items():
#     #print(subject, scores)
#     print(subject.ljust(8), str(scores).rjust(4), sep=":") #왼쪽으로 공백 8개 만들고 정렬
#
# for num in range(1,21):
#     print("the num : "+str(num).zfill(3)) #3크기를 0으로 채워넣음

# answer = input("anything you want : ") #문자열로 입력받음
# print(type(answer))
# print(answer)

# #다양한 출력포멧
# #빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# #양수일 땐 + 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# #왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# #3자리마다 콤마를 찍어주기
# print("{0:,}".format(5000000000))
# #3자리마다 콤마를 찍어주기 + 부호도
# print("{0:+,}".format(5000000000))
# #3자리마다 콤마를 찍어주기 + 부호도, 자리수도 확보, 빈 자리는 ^로 채우기, 왼쪽정렬
# print("{0:^<+30,}".format(5000000000))
#
# #소수점 출력
# print("{0:f}".format(5/3))
# #소수점을 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))

#파일 입출력
# score_file=open("score.txt","w",encoding="utf8") #utf8로 한글 불러오는거 애러없이
# print("math : 0", file=score_file)
# print("eng : 50", file=score_file)
# score_file.close()

# score_file=open("score.txt","a",encoding="utf8") #a는 파일 뒤에 계속 쓸때
# score_file.write("science : 80")
# score_file.write("\ncoding : 100")
# score_file.close()

# score_file=open("score.txt", "r", encoding="utf8") #r로 읽기 w로 쓰기
# print(score_file.read())
# score_file.close()

# score_file=open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 일고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file=open("score.txt", "r", encoding="utf8")
# while True: #몇 줄인지 모를 때
#     line = score_file.readline()
#     if not line: #읽어온 내용이 없으면
#         break
#     print(line, end="")
# score_file.close()

# score_file=open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() #list 형태로 저장
# for line in lines:
#     print(line,end="")
# score_file.close()

#pickle
# import pickle
# # profile_file = open("profile.pickle", "wb") #b는 바이너리고 피클쓸때 꼭 써야댐
# # profile = {"name":"A", "age":20, "hobby":["a","b","c"]}
# # print(profile)
# # pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
# # profile_file.close()
#
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

#with : 편하게 파일을 읽고 쓸 수 있음 close 필요 없음
# import pickle
#
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))
#
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("studying python")
#
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

#quiz
# for i in range(1,51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("{0} 주차 주간보고 : ".format(i))
#         report_file.write("\n부서 : ")
#         report_file.write("\nname : ")
#         report_file.write("\n요약 : ")

#class *********
#마린 : 공격유닛, 군인, 총을 쏨
# name = "marin"
# hp = 40
# damage = 5
#
# #tank : 공격 유닛, 일반 모드 / 시즈 모드
# tank_name = "tank"
# tank_hp = 150
# tank_damage = 30
#
# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 공격합니다. [공격력 {2}]".format(name,location,damage))
#
# attack(name,"1시", damage)
# attack(tank_name,"1시", tank_damage)

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name=name
#         self.hp=hp
#         self.damage=damage
#         print("{0} unit create".format(self.name))
#         print("hp {0}, damage {1}".format(self.hp,self.damage))
#
# marine1 = Unit("marine",40,5)
# marine2 = Unit("marine",40,5)
# tank = Unit("tank",150,35)

#맴버 변수 / 클래스 내에서 생성된 변수
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name=name
#         self.hp=hp
#         self.damage=damage
#         print("{0} unit create".format(self.name))
#         print("hp {0}, damage {1}".format(self.hp,self.damage))
#
# wraith1 = Unit("레이스", 80 ,5)
# print("{0}, {1}".format(wraith1.name,wraith1.damage))
#
# wraith2 = Unit("빼앗은 레이스",80,5)
# wraith2.clocking = True #클래스 밖에서 변수를 만들어서 사용 가능
#
# if wraith2.clocking==True:
#     print("{0} 는 현재 클로킹 상태입니다".format(wraith2.name))

#메소드
# class Unit:
#     def __init__(self, name, hp, damage):
#          self.name=name
#          self.hp=hp
#          self.damage=damage
#          print("{0} unit create".format(self.name))
#          print("hp {0}, damage {1}".format(self.hp,self.damage))
#
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#          self.name=name
#          self.hp=hp
#          self.damage=damage
#     def attack(self, location):
#         print("{0} : {1}방향으로 공격 {2}damage".format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} damaged".format(self.name,damage))
#         self.hp-=damage
#         print("{0} : now hp {1}".format(self.name,self.hp))
#         if self.hp<=0:
#             print("{0} destroyed".format(self.name))
#
# firebat1 =AttackUnit("firebat", 50 ,16)
# firebat1.attack("5시")
#
# firebat1.damaged(25)
# firebat1.damaged(25)
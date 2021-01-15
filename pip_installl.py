# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

#내장함수
# language = input("what's your favorite language?")
# print("{} is very good language".format(language))

#dir : 어떤 객체를 넘겼을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random #외장함수
# print(dir())
# import pickle
# print(dir())
# print(dir(random))

# list=[1,2,3]
# print(dir(list))
#
# name= "jim"
# print(dir(name))

#외장함수
#glob : 경로 내의 폴더, 파일 목록 조회
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일

#os : 운영체제에서 제공하는 기본 기능
import os
# print(os.getcwd()) # 현재 디렉토리 표시
#
# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder,"폴더를 삭제했습니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성했습니다.")

#print(os.listdir())

#time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("today is", datetime.date.today())
# today = datetime.date.today()
# td = datetime.timedelta(days=100) # 오늘부터 100일 뒤 날짜
# print(today + td)

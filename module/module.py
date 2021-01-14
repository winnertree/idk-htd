#모듈 // 함수 정의나 클래스 등의 정보를 담고있는 것
def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people,people*10000))

def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people * 7000))

def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원 입니다.".format(people, people * 6000))
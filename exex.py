#예외처리
# try:
#     print("나누기 전용 계산기입니다.")
#     num1=int(input("enter the 1st number : "))
#     num2=int(input("enter the 2nd number : "))
#     print("{}/{} = {}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("애러가 발생했습니다!")
#
# except ZeroDivisionError as err:
#     print(err)
#
# except Exception as err:
#     print("알수없는 애러가 발생했습니다.")
#     print(err)

#애러 발생시키기
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     n1 = int(input("enter the 1st number : "))
#     n2 = int(input("enter the 2nd number : "))
#     if n1>=10 or n2>=10:
#         raise ValueError
#     print("{} / {} = {}".format(n1,n2,int(n1/n2)))
#
# except ValueError:
#     print("error! error!")

#사용자 정의 애러 처리
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg=msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    n1 = int(input("enter the 1st number : "))
    n2 = int(input("enter the 2nd number : "))
    if n1>=10 or n2>=10:
        raise BigNumberError("입력값 : {}, {}".format(n1,n2))
    print("{} / {} = {}".format(n1,n2,int(n1/n2)))

except ValueError:
    print("error! error!")

except BigNumberError as err:
    print("error! error!")
    print(err)

finally: #finally //애러가 나도 무조건 실행되게 해줌
    print("계산기를 이용해주셔서 감사합니당.")

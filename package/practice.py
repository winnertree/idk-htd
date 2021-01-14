# import  package.thailand  #모듈이나 패키지만 호출 가능, 클래스는 안됨
# trip_to=package.thailand.ThailandPackage()
# trip_to.detail()

# from package.thailand import ThailandPackage #from import로는 클래스 호출가능
# trip_to=ThailandPackage()
# trip_to.detail()

# from package import vietnam
# trip_to=vietnam.VietnamPackage()
# trip_to.detail()

# from package import * # __init__ 에서 __all__에 모듈을 넣어주면 사용할 수 있음
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

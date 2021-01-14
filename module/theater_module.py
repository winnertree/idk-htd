# import module
#
# module.price(3)
# module.price_morning(4)
# module.price_soldier(5)

# import module as mv #모듈 명을 사용하기 쉽게
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from module import * #똑같이 모듈 불러오는거임
# price(3)
# price_soldier(4)
# price_morning(5) #바로 호출 가능

# from module import price,price_morning #필요한 함수만 가져와서 쓸 수 있음
# price(5)
# price_morning(4)

from module import price_soldier as price #하나 가져와서 쓸때는 별명 바꿔줄수있음
price(5)
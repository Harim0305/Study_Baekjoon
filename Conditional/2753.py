# 윤년
year = int(input()) # int 함수 이용해서 정수로 변환

# if 조건문
if (year % 4 == 0 and  year % 100 != 0) or (year % 400 == 0): # 윤년 조건, 나머지연산자 -> %, 같지 않다 -> !=
  print(1)
else: # 그 외
  print(0)
# 시험 성적

# int 함수 이용해서 정수로 변환하여 변수 선언
score = int(input())

# if 조건문
if score >= 90: # 90 ~ 100 일 경우
  print('A')
elif score >= 80: # 80 ~ 89 일 경우
  print('B')
elif score >= 70: # 70 ~ 79 일 경우
  print('C')
elif score >= 60: # 60 ~ 69 일 경우
  print('D')
else: # 나머지 점수
  print('F')
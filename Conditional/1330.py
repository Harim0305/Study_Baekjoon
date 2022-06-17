# 두 수 비교하기

A, B = map(int, input().split()) 
# 두 개의 수를 가운데 공백 포함한 하나의 문자열로 입력받는다.
# input 함수로 입력받고 split 함수로 나눈다.
# 아무것도 입력하지 않으면 공백을 기준으로 문자를 나눌 수 있다.
# map 함수로 문자를 int(정수)로 변환

# if 조건문
if A > B:
  print('>') # if 조건문이 참일 때 
elif A < B:
  print('<') # if 조건문이 거짓이고, elif 조건문이 참일 때
else:
  print('==') # 위 조건이 모두 거짓일 때
# 사분면 고르기

# input 함수로 입력받고 int 함수로 문자열을 숫자로 변환
x = int(input())
y = int(input())

if x > 0 and y > 0: # x, y 양수 -> 1사분면
  print(1)
elif x < 0 and y > 0: # x 음수, y 양수 -> 2사분면
  print(2)
elif x < 0 and y < 0: # x, y 음수 -> 3사분면
  print(3)
else: # x 양수, y 음수 -> 4사분면 (나머지)
  print(4)
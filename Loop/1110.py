# 더하기 사이클

n = int(input())
num = n
cnt = 0

while True:
  a = num // 10 # 정수 부분의 몫
  b = num % 10 # 나머지 부분
  c = (a + b) % 10 # 새로운 수 더한 값의 나머지
  num = (b * 10) + c # 십의 자리로 만들고 새로운 나머지 더해서 새로운 수 생성

  cnt = cnt + 1 # 새로운 수 만들때마다 1씩 더하기
  if(num == n): # 처음 수와 같아지면 멈추기
    break

print(cnt)
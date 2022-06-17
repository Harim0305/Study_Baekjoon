# 합

n = int(input())

sum = 0

#  range(초기값, 종료값, 증가값)
for i in range(n+1): # 종료값은 해당 값을 포함하지 않기 때문에 +1
  sum = sum + i
print(sum)
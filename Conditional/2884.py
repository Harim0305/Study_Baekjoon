# 알람 시계

H, M = map(int, input().split()) # H: 시간, M: 분

if M < 45: # 분이 45분다 작을 때
  if H == 0: # 0시면
    H = 23
    M += 60
  else: # 0시 아니면
    H -= 1
    M += 60

print(H, M-45)
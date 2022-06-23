# OX 퀴즈

a = int(input()) # 테스트 케이스 개수 입력

for i in range(a):
  b = input() # 테스트 케이스 입력
  score = list(b) # 리스트 형태로 변환
  sum = 0
  c = 1

  for i in score:
    if i == 'O': # O를 만나게 되면
      sum += c # sum에 c를 더해주고
      c += 1 # c는 1씩 증가
    else: # X를 만나게 되면
      c = 1 # c는 1로 돌아옴

  print(sum) # 테스트 케이스마다 점수 출력
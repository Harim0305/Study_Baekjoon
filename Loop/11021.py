# A+B - 7

T = int(input())

for i in range(1, T+1): # 1부터 T까지
  # 두 수를 입력받고
  a, b = map(int, input().split())
  # f-string 이용해서 출력문 작성
  print(f'Case #{i}: {a + b}')
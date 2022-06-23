# 숫자의 개수

A = int(input())
B = int(input())
C = int(input()) # A, B, C 숫자 받기

ans = list(str(A*B*C)) # 문자열로 변환하고 각각의 문자를 요소로 가지게 하기 위해 리스트로 변환

for i in range(10): # 0부터 9까지
  print(ans.count(str(i))) # 리스트 문자 개수 count
# A+B - 3

# 테스트 케이스 개수 T 입력받음
# int 함수를 이용해 정수로 변환
T = int(input())

# T 만큼 반복하는 것이 중요하기 때문에 변수를 언더바로 표현
for _ in range(T):
  # 두 수를 입력받고
  a, b = map(int, input().split())
  # 두 수의 합 출력
  print(a + b)
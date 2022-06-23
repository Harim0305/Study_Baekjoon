# 평균은 넘겠지

n = int(input()) # 테스트 케이스 개수

for _ in range(n):
  nums = list(map(int, input().split())) # 학생수, 점수 순서대로 부여
  avg = sum(nums[1:])/nums[0] # 점수들 평균 구하기
  cnt = 0

  for score in nums[1:]:
    if score > avg:
      cnt += 1 # 평균 넘는 학생 수 1씩 추가
  
  rate = cnt/nums[0] * 100 # 평균보다 높은 점수 받은 학생 비율
  print(f'{rate:.3f}%') # f-string 표기법으로 작성, 중괄호 안에 변수 삽입 가능
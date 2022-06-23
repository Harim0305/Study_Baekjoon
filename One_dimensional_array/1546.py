# 평균

n = int(input()) # 과목의 개수 입력
test_list = list(map(int, input().split())) # 현재 성적
max_score = max(test_list) # 점수 중 최댓값 고르기
new_list = [] # 빈 리스트 생성, 새로운 점수 추가

for score in test_list:
  new_list.append(score/max_score * 100) # 새로운 성적 계산 방법

test_avg = sum(new_list)/n # 새로운 평균
print(test_avg)
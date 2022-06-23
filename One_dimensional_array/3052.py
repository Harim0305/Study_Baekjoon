# 나머지

arr = [] # 빈 리스트 생성

for i in range(10): 
  n = int(input()) # n 입력받고
  arr.append(n%42) # 42로 나눈 나머지들 추가

arr = set(arr) # set로 집합 자료형으로 만들어주기, set 함수는 중복을 제거하기 위한 필터 역할
print(len(arr)) # 리스트 개수 출력
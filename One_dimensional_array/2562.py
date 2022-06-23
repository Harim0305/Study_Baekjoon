# 최댓값

num_list = [] # 리스트 선언

for i in range(9): # 첫째 줄부터 아홉 번째 줄까지
  num_list.append(int(input())) # 자연수 추가

print(max(num_list)) # 최댓값 출력
print(num_list.index(max(num_list))+1) # 몇 번째 수인지 출력, 0부터 시작하므로 +1
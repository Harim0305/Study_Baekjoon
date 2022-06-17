# A+B

# input 함수로 입력받고, split으로 나누어 저장
# map(function, iterable) -> 두번째 인자(리스트나 튜플)를 첫번째 인자로 들어온 함수에 하나씩 넣어서 함수 수행
a, b = map(int, input().split()) 

print(a+b)
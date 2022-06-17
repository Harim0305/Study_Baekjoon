# 구구단

# input 함수 사용하면 문자열로 입력되기 때문에 int 함수를 이용해서 정수로 변환
n = int(input())

# range 함수로 일정한 규칙을 가진 숫자 범위 지정
for i in range(1, 10): # 1~9
    print(n, '*', i, '=', n*i)
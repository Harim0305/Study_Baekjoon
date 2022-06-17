# 곱셈
a = int(input()) # 숫자로 변환
b = input() # 문자열 그대로 

# 하나씩 숫자로 반환하면서 A랑 곱하기
a_b2 = a*int(b[2])
a_b1 = a*int(b[1])
a_b0 = a*int(b[0])
a_b = a*int(b)

print(a_b2, a_b1, a_b0, a_b, sep='\n')
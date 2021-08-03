# 최대값, 최소값 구하기

n = list(map(int, input("숫자입력 : ").split())) 

n.sort(reverse=1)
print(n[0],n[-1])
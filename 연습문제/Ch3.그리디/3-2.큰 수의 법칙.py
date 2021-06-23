# 그리디 실전문제 3-2
# 큰 수의 법칙

while True : 
    n, m, k = map(int, input("숫자입력(n m k), m >= k : ").split())
    if m >= k : 
        break

data = list(map(int, input("숫자입력(n개) : ").split())) 

data.sort()

num1 = data[n - 1]
num2 = data[n - 2]

result = 0

while True : 
    for i in range(k) : 
        if m == 0 : 
            break
        result += num1
        m -= 1

    if m == 0 : 
        break
    result += num2
    m -= 1

print(result)

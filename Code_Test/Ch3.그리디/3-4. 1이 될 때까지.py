# 그리디 실전문제 3-4
# 1이 될 때까지

result = 0

n, k = map(int, input("숫자입력(n k) : ").split())


while n >= k : # != 1 : 이 되면 종료
    
    while n % k != 0 :
        n -= 1
        result += 1
            
    n //= k
    result += 1

while n > 1 :
    n -= 1
    result += 1

print(result)
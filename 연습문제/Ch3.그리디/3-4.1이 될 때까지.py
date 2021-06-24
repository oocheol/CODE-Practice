# 그리디 실전문제 3-4
# 1이 될 때까지

result = 0

n, k = map(int, input("숫자입력(n k) : ").split())


while !=1 :
    if n % k == 0 :
        n += n//k
        result += 1
            

    else :
        n -= 1
        result += 1


print(result)
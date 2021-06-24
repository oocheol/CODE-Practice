# 그리디 실전문제 3-4
# 1이 될 때까지

result = 0

while True :
    n, k = map(int, input("숫자입력(n k) : ").split())
        if n >= 2 :
            break

            if k >= 2 :
                break


    if n % k == 0 :
        result += n//k

    else :
        n -= 1
        result += 1

        if n % k == 0 :
            result += n//k

print(result)
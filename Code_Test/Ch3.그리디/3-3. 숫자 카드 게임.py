# 그리디 실전문제 3-3
# 숫자 카드 게임


n, m = map(int, input("숫자입력(n m) : ").split())


result = 0

for x in range(n) : 
    data = list(map (int, input("숫자입력(m 개) : ").split()))
        
    min_data = min(data)
    result = max(result, min_data)

print(result)

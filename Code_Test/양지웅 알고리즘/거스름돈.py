n = int(input())

N = 1000 - n
c = 0
change = [500, 100, 50, 10, 5, 1]

for i in change : 
    c += N // i # N을 i(500~10)으로 나눈 몫을 c에 count한다
    N %= i      # 나머지값을 N에 다시 더한다
    
print(c)
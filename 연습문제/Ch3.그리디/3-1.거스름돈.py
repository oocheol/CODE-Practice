#그리디 예제 3-1
#거스름돈

N = int(input())
c = 0
change = [500, 100, 50, 10]

for i in change : 
    c += N // i # N을 i(500~10)으로 나눈 몫을 c에 count한다
    N %= i      # 나머지값을 N에 다시 더한다
    
print(c)
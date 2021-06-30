a, b, R = map(int,input("a, b, N : ").split())

N = int(input("N : "))

# 리스트 이용하여 한번에 출력
arr = []
for _ in range(N) :
    arr.append(list(map(int,input("x, y : ").split())))

for i in arr :
    x, y = i

    if ((x-a)**2) + ((y-b)**2) >= R**2 :
        print("silent")

    else :
        print("noisy")


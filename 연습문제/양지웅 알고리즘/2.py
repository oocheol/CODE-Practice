a, b, R = map(int,input("a, b, N : ").split())

N = int(input("N : "))

for i in range(N) :
    x, y = map(int, input("x, y : ").split())
    
    if ((x-a)**2) + ((y-b)**2) >= R**2 :
        print("silent")

    else :
        print("noisy")


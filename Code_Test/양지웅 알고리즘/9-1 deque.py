# 큐 추가문제(2) - 회전하는 큐
# deque

from collections import deque

n, m = map(int, input().split())
x = list(map(int,input().split()))

a = deque(z for z in range(1, n+1))
print(a)

f_idx = 0
b_idx = 0


for i in range(len(x)-1):
    if a.index(x[i]) == 0 :
            a.popleft()
            print(a)
            
    elif a.index(x[i]) <= a.index(x[i+1]) :
            while True:
                a.rotate(-1)
                f_idx += 1
                if a.index(x[i]) == 0 :
                    a.popleft()
                    print(a)
                    break    
                
    elif a.index(x[i]) > a.index(x[i+1]) :
           while True:
               a.rotate(1)
               b_idx +=1
               if a.index(x[i]) == 0 :
                   a.popleft()
                   print(a)
                   break
    
    if i == len(x)-2 :
        if a.index(x[i+1]) == 0 :
            a.popleft()
            print(a)

        elif a.index(x[i+1]) < len(a)/2:
            while True:
                a.rotate(-1)
                f_idx += 1
                if a.index(x[i+1]) == 0 :
                    a.popleft()
                    print(a)
                    break    

        else:
            while True:
               a.rotate(1)
               b_idx +=1
               if a.index(x[i+1]) == 0 :
                   a.popleft()
                   print(a)
                   break

print("f_idx :", f_idx)
print("b_idx :", b_idx)
print("final : ", a)
print("output : ", f_idx+ b_idx)
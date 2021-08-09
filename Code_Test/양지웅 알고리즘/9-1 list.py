# 큐 추가문제(2) - 회전하는 큐
# list

n, m = map(int, input().split())
x = list(map(int,input().split()))

a = [z for z in range(1, n+1)]
print(a)

f_idx = 0   
b_idx = 0

for i in range(len(x)-1):
    if a.index(x[i]) == 0 :
            a.pop(0)
            print(a)
            
    
    elif a.index(x[i]) <= a.index(x[i+1]) :
            while True:
                a.append(a.pop(0))
                f_idx += 1
                if a.index(x[i]) == 0 :
                    a.pop(0)
                    print(a)
                    break    
                
    elif a.index(x[i]) > a.index(x[i+1]) :
           while True:
               a.insert(0,a.pop(-1))
               b_idx +=1
               if a.index(x[i]) == 0 :
                   a.pop(0)
                   print(a)
                   break
    
    if i == len(x)-2 :
        if a.index(x[i+1]) == 0 :
            a.pop(0)
            print(a)

        elif a.index(x[i+1]) < len(a)/2:
            while True:
                a.append(a.pop(0))
                f_idx += 1
                if a.index(x[i+1]) == 0 :
                    a.pop(0)
                    print(a)
                    break    

        else:
            while True:
               a.insert(0,a.pop(-1))
               b_idx +=1
               if a.index(x[i+1]) == 0 :
                   a.pop(0)
                   print(a)
                   break

print("f_idx :", f_idx)
print("b_idx :", b_idx)
print("final : ", a)
print("output : ", f_idx+ b_idx)
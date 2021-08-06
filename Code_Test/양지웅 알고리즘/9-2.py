# 큐 추가문제(2) - 회전하는 큐

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 2, 9, 5
x = [2, 9 ,5]
f_idx = 0
b_idx = 0
i = 0

while i <= len(x):
    if i+1 < len(x):
        if a.index(x[i]) == 0 :
            a.pop(0)

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
        i += 1
    break

print(f_idx)
print(b_idx)
print(a)
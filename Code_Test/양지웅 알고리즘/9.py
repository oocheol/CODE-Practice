# 알고리즘 8
# 큐 추가문제 (1) - 카드2

n = int(input("N : "))
num_list = [x for x in range(1,n+1)]
i = 0

while i < n+3 :
    if i % 2 == 0:
        num_list.pop(0)
        i += 1
    
    num_list.append(num_list.pop(0))
    i += 1

print(num_list)


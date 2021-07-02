steps = [(-2, -1),(-1, -2),(1, -2),(2, -1),(2, 1),(1, 2),(-1, 2),(-2, 1)]

result = 0 

for step in steps :
    x = 1 + step[0]
    y = 1 + step[1]
    if x >= 1 and x <= 8 and y >= 1 and y <= 8 :
        result +=1
    print(x,y)
print(result)
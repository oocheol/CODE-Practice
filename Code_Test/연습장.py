res = []
i = 1
for x in range(1, 6) :
    for j in range(1, 6) :
        res.append(x * j)
        if j == 5 :
            print(res[0], res[1], res[2], res[3], res[4])
            res = []
            
        



    
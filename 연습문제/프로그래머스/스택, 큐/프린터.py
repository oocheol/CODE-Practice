
def solution(pr, loc):
    res = []
    idx = []
    for i, _ in enumerate(pr) :
        idx.append(i)
    
    n = 0
    
    while n < len(pr) :

        if pr[0] > max(pr[1:]) :
            res.append(idx.pop(0))
            pr.pop(0)
            n += 1

        else :
            pr.append(pr.pop(0))
            idx.append(idx.pop(0))
            n += 1

    
    return idx[loc]

a1 = [2, 1, 3, 2]
a2 = [1, 1, 9, 1, 1, 1]

print(solution(a1,2))
print(solution(a2,0))
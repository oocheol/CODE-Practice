## 스택 / 큐   : 프린터

a1 = [2, 1, 3, 2]
a2 = [1, 1, 9, 1, 1, 1]

def solution(pr, loc):
    a = []
    n = 0
    
    
    while n < len(pr) :
        if pr[0] > max(pr[1:]) :
            a.append(pr.pop(0))
            n += 1
        else :
            pr.append(pr.pop(0))    
            n += 1

    print(a)
    print(pr)

solution(a1,2)
solution(a2,0)
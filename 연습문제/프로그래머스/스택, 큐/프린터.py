## 스택 / 큐   : 프린터

a1 = [2, 1, 3, 2]
a2 = [1, 1, 9, 1, 1, 1]

def solution(pr, loc):
    
    c = pr[loc]
    for i in range(len(pr)) :
        for z in range(1,len(pr)-1) :
            if pr[i] < pr[z] :
                pr.insert(-1,pr[i])
                pr.remove(pr[i])
            else :
                
            
    print(pr)

            
    

solution(a1,2)
solution(a2,0)
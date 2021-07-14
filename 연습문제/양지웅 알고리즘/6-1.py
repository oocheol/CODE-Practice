# 6 

que = []

class run
def process_que(x) :
    if x[0] == "push" :
        que.append(x[1])

    elif x[0] == "pop" :
        if len(que) >= 1 :
            que.reverse()
            print(que.pop())
            que.reverse()
        else :
            print(-1)

    elif x[0] == "size" :
        print(len(que))

    elif x[0] == "empty" :
        if len(que) == 0 :
            print(1)
        else :
            print(0)

    elif x[0] == "front" :
        if len(que) >= 1 :
            print(que[0]) 
        else :
            print(-1)
    
    elif x[0] == "back" :
        if len(que) >= 1 :
            print(que[-1]) 
        else :
            print(-1)

             
n = int(input())

for _ in range(n) :
    x = input().split(" ")
    process_que(x)
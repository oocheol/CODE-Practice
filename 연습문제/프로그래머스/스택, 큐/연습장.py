import math

def solution(progresses, speeds):
    a = []
    res = []
    for i in range(len(progresses)) :
        b = math.ceil((100 - progresses[i]) / speeds[i])
        a.append(int(b))
    
    print(a[0]>a[1])

prog1 = [93, 30, 55]
spd1 = [1, 30, 5]
prog2 = [95, 90, 99, 99, 80, 99]
spd2 = [1, 1, 1, 1, 1, 1]

solution(prog1, spd1)
solution(prog2, spd2)
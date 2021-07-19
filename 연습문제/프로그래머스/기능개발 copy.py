import math

def solution(progresses, speeds):

    a = math.ceil((100-progresses[0])/speeds[0])

    answer = [0]

    for i,j in zip(progresses,speeds):
        b = math.ceil((100-i)/j)
        if(a >= b):
            answer.append(answer.pop()+1)
        if(a < b):
            a=math.ceil((100-i)/j)
            answer.append(1)

    return answer   

prog1 = [93, 30, 55]
spd1 = [1, 30, 5]
prog2 = [95, 90, 99, 99, 80, 99]
spd2 = [1, 1, 1, 1, 1, 1]

print(solution(prog1, spd1))
print(solution(prog2, spd2))
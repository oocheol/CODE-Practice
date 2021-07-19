# import math

# def solution(progresses, speeds):
#     a = []
#     res = []
#     n = 0
    
#     for i in range(len(progresses)) :
#         b = math.ceil((100 - progresses[i]) / speeds[i])
#         a.append(b)
    
#     while n+1 < len(a) :
#             if a[n] < a[n+1] :
#                 res.append(len(a[:n]))
#                 n += 1
            
#             else :
#                 n += 1
        
#     print(a)    
#     print(res)


# prog1 = [93, 30, 55]
# spd1 = [1, 30, 5]
# prog2 = [95, 90, 99, 99, 80, 99]
# spd2 = [1, 1, 1, 1, 1, 1]

# solution(prog1, spd1)
# solution(prog2, spd2)
# etc

def solution(number, k):
    a = []
    for i in number:
        for _ in range(k):
            if a and a[-1] < i :
                a.pop()
        a.append(i)
    return "".join(a)

print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
# stack

def solution(number, k):
    a = []
    for i in number:
        while a and a[-1] < i and k >0:
            k-=1
            a.pop()
        a.append(i)
    return "".join(a[:len(a)-k])

print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
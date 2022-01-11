from random import randint


def generate_numbers(n):
    result = []
    while True :
        if len(set(result)) == n :
            result = set(result)
            break
        result.append(randint(1,45))
        
    return result


def draw_winning_numbers():
    temp = []
    
    result = generate_numbers(7)
    result = list(result)
    temp.append(result.pop())
    result.sort()
    result.append(temp[0])

    return result

print(draw_winning_numbers())
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

def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for i in numbers :
        if i in winning_numbers:
            count += 1
        
    return count


def check(numbers, winning_numbers):
    goal = count_matching_numbers(numbers, winning_numbers[:6])
    bonus = count_matching_numbers(numbers, winning_numbers[-1:])
    if goal == 6 :
        return 1000000000
    
    elif goal == 5 and bonus == 1:
        return 50000000
    
    elif goal == 5:
        return 1000000
    
    elif goal == 4:
        return 50000
    
    elif goal == 3:
        return 5000

    else :
        return 0
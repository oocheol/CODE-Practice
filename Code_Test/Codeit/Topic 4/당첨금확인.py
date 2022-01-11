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


# 테스트
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))
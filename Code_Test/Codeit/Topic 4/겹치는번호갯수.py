def count_matching_numbers(list_1, list_2):
    temp = []
    for i in list_1 :
        if i in list_2:
            temp.append(i)
    
    return len(temp)


# 테스트
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))
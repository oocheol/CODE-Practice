# 재귀문제 - 진법 전환 1

# 입력예제 1
# ZZZZZ 36
# 출력예제 1
# 60466175

whole_num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, m = input().split()
def change_num(input_num, num):
    res = []    
    result = 0
    temp_list = list(input_num)
    temp_list.reverse()
    for x in temp_list:
        res.append(whole_num.index(x))
    for idx, y in enumerate(res):
        result += int(num) ** idx * y
    return result
    
print(change_num(n, m))
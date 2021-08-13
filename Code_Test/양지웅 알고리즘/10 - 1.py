# 재귀문제 - 진법전환 2

# 입력 예제 1
# 60466175 36
# 출력 예제 1
# ZZZZZ

whole_num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, m = map(int, input().split())
def change_num(input_num, num):
    temp = []
    
    while input_num > num:
        if input_num // num == 0 :
            temp.append(whole_num[input_num])    
            print(temp)
        temp.append(whole_num[input_num % num])
        input_num = input_num // num
        print(temp)

    return temp        
    
    
print(change_num(n, m))
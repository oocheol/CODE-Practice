# 재귀문제 - 진법 전환 1
# 재귀 사용

# 입력예제 1
# ZZZZZ 36
# 출력예제 1
# 60466175

whole_num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, m = input().split()
length = len(n)

def recursion(x, len):
    idx = 0
    temp_list = list(x)
    temp_list.reverse()

    if len == 0 :
        return 
    
    temp_list[len]
    
    

    